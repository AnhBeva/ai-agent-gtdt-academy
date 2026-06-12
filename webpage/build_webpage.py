#!/usr/bin/env python3
from __future__ import annotations

import html
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "webpage"

SOURCE_FILES = [
    ("academy", "Giáo trình tổng", ROOT / "Giao_trinh_AI_Agent_Bounded_Autonomy.md"),
    ("goal", "GOAL.md", ROOT / "templates" / "GOAL.md"),
    ("workflow", "WORKFLOW.md", ROOT / "templates" / "WORKFLOW.md"),
    ("qa-gate", "QA Gate Checklist", ROOT / "templates" / "QA_Gate_Checklist.md"),
    ("sol", "SOL Worksheet", ROOT / "templates" / "SOL_Worksheet.md"),
    (
        "complexity",
        "Agent Task Complexity Matrix",
        ROOT / "templates" / "Agent_Task_Complexity_Matrix.md",
    ),
    ("manager", "Manager Follow-up Form", ROOT / "templates" / "Manager_Follow_up_Form.md"),
]


@dataclass
class Heading:
    level: int
    text: str
    slug: str
    source_id: str
    source_label: str


class MarkdownRenderer:
    def __init__(self) -> None:
        self.headings: list[Heading] = []
        self.slug_counts: dict[str, int] = {}

    def slugify(self, text: str) -> str:
        raw = re.sub(r"`([^`]+)`", r"\1", text)
        raw = raw.replace("đ", "d").replace("Đ", "D")
        normalized = unicodedata.normalize("NFKD", raw)
        ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
        slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_text.lower()).strip("-")
        if not slug:
            slug = "section"
        count = self.slug_counts.get(slug, 0)
        self.slug_counts[slug] = count + 1
        return slug if count == 0 else f"{slug}-{count + 1}"

    def inline(self, text: str) -> str:
        placeholders: list[str] = []

        def stash_code(match: re.Match[str]) -> str:
            placeholders.append(f"<code>{html.escape(match.group(1))}</code>")
            return f"\u0000{len(placeholders) - 1}\u0000"

        escaped = html.escape(text)
        escaped = re.sub(r"`([^`]+)`", stash_code, escaped)
        escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
        escaped = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', escaped)

        def restore(match: re.Match[str]) -> str:
            return placeholders[int(match.group(1))]

        return re.sub("\u0000(\\d+)\u0000", restore, escaped)

    def render_table(self, lines: list[str], start: int) -> tuple[str, int]:
        rows: list[list[str]] = []
        i = start
        while i < len(lines) and lines[i].strip().startswith("|"):
            raw = lines[i].strip().strip("|")
            rows.append([cell.strip() for cell in raw.split("|")])
            i += 1
        if len(rows) >= 2 and all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in rows[1]):
            header = rows[0]
            body = rows[2:]
        else:
            header = []
            body = rows

        out = ['<div class="table-wrap"><table>']
        if header:
            out.append("<thead><tr>")
            out.extend(f"<th>{self.inline(cell)}</th>" for cell in header)
            out.append("</tr></thead>")
        out.append("<tbody>")
        for row in body:
            out.append("<tr>")
            out.extend(f"<td>{self.inline(cell)}</td>" for cell in row)
            out.append("</tr>")
        out.append("</tbody></table></div>")
        return "\n".join(out), i

    def render_list(self, lines: list[str], start: int, ordered: bool) -> tuple[str, int]:
        tag = "ol" if ordered else "ul"
        out = [f"<{tag}>"]
        i = start
        pattern = r"^\s*\d+\.\s+(.*)$" if ordered else r"^\s*[-*]\s+(.*)$"
        while i < len(lines):
            match = re.match(pattern, lines[i])
            if not match:
                break
            out.append(f"<li>{self.inline(match.group(1).strip())}</li>")
            i += 1
        out.append(f"</{tag}>")
        return "\n".join(out), i

    def render_fence(self, lines: list[str], start: int) -> tuple[str, int]:
        opener = lines[start].strip()
        match = re.match(r"^(`{3,}|~{3,})([A-Za-z0-9_-]+)?", opener)
        assert match
        fence = match.group(1)
        lang = match.group(2) or "text"
        close_pattern = re.compile(rf"^{re.escape(fence[0])}{{{len(fence)},}}\s*$")
        code_lines: list[str] = []
        i = start + 1
        while i < len(lines):
            if close_pattern.match(lines[i].strip()):
                i += 1
                break
            code_lines.append(lines[i])
            i += 1
        code = html.escape("\n".join(code_lines))
        return (
            '<div class="code-card">'
            f'<div class="code-head"><span>{html.escape(lang)}</span><button class="copy-code" type="button">Sao chép</button></div>'
            f'<pre><code class="language-{html.escape(lang)}">{code}</code></pre>'
            "</div>",
            i,
        )

    def paragraph_class(self, text: str) -> str:
        lower = text.lower()
        if any(key in lower for key in ["nguyên tắc", "best practices", "evidence", "decision", "lưu ý"]):
            return ' class="callout callout-good"'
        if any(key in lower for key in ["sai lầm", "red flags", "rủi ro", "stop", "dừng"]):
            return ' class="callout callout-warn"'
        return ""

    def render(self, markdown: str, source_id: str, source_label: str) -> str:
        lines = markdown.splitlines()
        out: list[str] = []
        i = 0
        while i < len(lines):
            line = lines[i]
            stripped = line.strip()
            if not stripped:
                i += 1
                continue
            if re.match(r"^(`{3,}|~{3,})", stripped):
                html_block, i = self.render_fence(lines, i)
                out.append(html_block)
                continue
            if stripped == "---":
                out.append("<hr>")
                i += 1
                continue
            heading = re.match(r"^(#{1,3})\s+(.+)$", stripped)
            if heading:
                level = len(heading.group(1))
                text = heading.group(2).strip()
                slug = self.slugify(f"{source_id}-{text}")
                self.headings.append(Heading(level, text, slug, source_id, source_label))
                if level == 1:
                    out.append(
                        f'<section class="doc-section source-{html.escape(source_id)}" id="{slug}">'
                        f'<div class="source-label">{html.escape(source_label)}</div>'
                        f'<h1>{self.inline(text)}</h1>'
                    )
                else:
                    out.append(f'<h{level} id="{slug}">{self.inline(text)}</h{level}>')
                i += 1
                continue
            if stripped.startswith("|"):
                html_block, i = self.render_table(lines, i)
                out.append(html_block)
                continue
            if re.match(r"^\s*[-*]\s+", line):
                html_block, i = self.render_list(lines, i, ordered=False)
                out.append(html_block)
                continue
            if re.match(r"^\s*\d+\.\s+", line):
                html_block, i = self.render_list(lines, i, ordered=True)
                out.append(html_block)
                continue

            para = [stripped]
            i += 1
            while i < len(lines):
                nxt = lines[i].strip()
                if (
                    not nxt
                    or re.match(r"^(`{3,}|~{3,})", nxt)
                    or nxt.startswith("|")
                    or re.match(r"^#{1,3}\s+", nxt)
                    or re.match(r"^\s*[-*]\s+", lines[i])
                    or re.match(r"^\s*\d+\.\s+", lines[i])
                    or nxt == "---"
                ):
                    break
                para.append(nxt)
                i += 1
            text = " ".join(para)
            out.append(f"<p{self.paragraph_class(text)}>{self.inline(text)}</p>")
        if out and out[-1] != "</section>":
            out.append("</section>")
        return "\n".join(out)


def build_sidebar(headings: list[Heading]) -> str:
    items: list[str] = []
    for h in headings:
        if h.level > 2:
            continue
        level_class = "toc-h1" if h.level == 1 else "toc-h2"
        items.append(
            f'<a class="toc-link {level_class}" href="#{h.slug}" data-target="{h.slug}" data-source="{html.escape(h.source_id)}">'
            f'<span>{html.escape(h.text)}</span></a>'
        )
    return "\n".join(items)


def build_template_cards() -> str:
    cards = [
        ("GOAL.md", "Hợp đồng mục tiêu: objective, scope, DoD, validation, evidence.", "goal"),
        ("WORKFLOW.md", "Quy trình planner, engineer, reviewer, fail-back và handoff.", "workflow"),
        ("QA Gate", "Cổng kiểm chứng compile, unit, lint, visual, benchmark, security.", "qa-gate"),
        ("SOL Worksheet", "Tối ưu theo compute/I/O/network bound và trần hiệu năng.", "sol"),
        ("Complexity Matrix", "Phân loại task, steering bắt buộc và mức autonomy.", "complexity"),
        ("Manager Follow-up", "Evidence, KPI, blocker và quyết định steering 30-60-90.", "manager"),
    ]
    out = []
    for title, desc, source_id in cards:
        out.append(
            f'<a class="template-card" href="#templates-section" data-jump-source="{source_id}">'
            f'<strong>{html.escape(title)}</strong><span>{html.escape(desc)}</span></a>'
        )
    return "\n".join(out)


def main() -> None:
    renderer = MarkdownRenderer()
    content_parts: list[str] = []
    manifest_rows: list[str] = []
    total_lines = 0
    for source_id, label, path in SOURCE_FILES:
        text = path.read_text(encoding="utf-8")
        line_count = len(text.splitlines())
        total_lines += line_count
        manifest_rows.append(
            f"<tr><td>{html.escape(label)}</td><td>{line_count}</td><td>{html.escape(str(path.relative_to(ROOT)))}</td></tr>"
        )
        content_parts.append(renderer.render(text, source_id, label))

    sidebar = build_sidebar(renderer.headings)
    template_cards = build_template_cards()
    manifest = "\n".join(manifest_rows)
    full_content = "\n".join(content_parts)

    html_doc = f"""<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>AI Agent: Bounded Autonomy Academy</title>
  <meta name="description" content="Webpage đào tạo AI Agent Bounded Autonomy cho Dev, Tech Lead và R&D.">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="progress-bar" id="progressBar"></div>
  <header class="topbar">
    <a class="brand" href="#top" aria-label="AI Agent Academy">
      <span class="brand-mark">⌁</span>
      <span><strong>AI Agent Academy</strong><small>Bounded Autonomy</small></span>
    </a>
    <nav class="topnav" aria-label="Điều hướng chính">
      <a href="#academy-giao-trinh-dao-tao-ai-agent-bounded-autonomy-cho-dev-tech-lead">Academy</a>
      <a href="#academy-5-case-study">Case Studies</a>
      <a href="#academy-7-bo-workshop-thuc-hanh">Workshop</a>
      <a href="#templates-section">Templates</a>
      <a href="#academy-13-lo-trinh-ap-dung-sau-dao-tao-30-60-90-ngay">Roadmap</a>
    </nav>
    <div class="top-actions">
      <label class="search"><span>⌕</span><input id="searchInput" type="search" placeholder="Tìm kiếm nội dung"></label>
      <button class="icon-btn" id="printBtn" type="button">In/PDF</button>
      <button class="menu-btn" id="menuBtn" type="button" aria-expanded="false">Mục lục</button>
    </div>
  </header>

  <aside class="sidebar" id="sidebar" aria-label="Mục lục">
    <div class="sidebar-head">
      <strong>Nội dung</strong>
      <span id="readPercent">0%</span>
    </div>
    <div class="toc">{sidebar}</div>
    <div class="sidebar-card">
      <strong>Manifest nguồn</strong>
      <span>{len(SOURCE_FILES)} file · {total_lines} dòng Markdown</span>
    </div>
  </aside>

  <main id="top" class="page">
    <section class="hero">
      <div class="hero-copy">
        <h1>AI Agent:<br>Bounded Autonomy</h1>
        <p>Thiết kế, xây dựng và vận hành AI Agent tự chủ trong ranh giới. Tập trung vào an toàn, hiệu quả và đo lường được.</p>
        <div class="hero-actions">
          <a class="primary-btn" href="#academy-1-tuyen-bo-muc-tieu-dao-tao">Bắt đầu học</a>
          <a class="secondary-btn" href="#academy-13-lo-trinh-ap-dung-sau-dao-tao-30-60-90-ngay">Xem lộ trình 30-60-90</a>
        </div>
      </div>
      <div class="hero-visual" aria-label="Agent boundary diagram">
        <div class="boundary-box">
          <div class="cube">AI<br>Agent</div>
          <span class="node node-top">Mục tiêu</span>
          <span class="node node-left">Quan sát</span>
          <span class="node node-right">Hành động</span>
          <span class="node node-bottom">Ràng buộc</span>
        </div>
      </div>
    </section>

    <section class="stats-grid" aria-label="Tổng quan nội dung">
      <div><strong>13</strong><span>Phần giáo trình</span></div>
      <div><strong>7</strong><span>Bài học chuyên sâu</span></div>
      <div><strong>6</strong><span>Template chuyên sâu</span></div>
      <div><strong>100</strong><span>Điểm đánh giá</span></div>
      <div><strong>90</strong><span>Ngày áp dụng</span></div>
    </section>

    <section class="overview-panel" id="templates-section">
      <div>
        <h2>Template Library</h2>
        <p>6 tài liệu vận hành được tách riêng, trình bày sâu về bản chất, phương pháp, biểu mẫu, ví dụ và tiêu chuẩn đánh giá.</p>
      </div>
      <div class="template-grid">{template_cards}</div>
    </section>

    <section class="source-manifest">
      <h2>Kiểm kê nội dung nguồn</h2>
      <p>HTML này được build từ toàn bộ Markdown nguồn, không fetch runtime và không rút gọn nội dung.</p>
      <div class="table-wrap"><table><thead><tr><th>Tài liệu</th><th>Số dòng</th><th>Đường dẫn</th></tr></thead><tbody>{manifest}</tbody></table></div>
    </section>

    <article class="content" id="contentRoot">
      {full_content}
    </article>
  </main>

  <button class="to-top" id="toTop" type="button" aria-label="Về đầu trang">↑</button>
  <script src="app.js"></script>
</body>
</html>
"""
    (OUT_DIR / "index.html").write_text(html_doc, encoding="utf-8")
    print(f"Wrote {OUT_DIR / 'index.html'}")
    print(f"Source files: {len(SOURCE_FILES)}")
    print(f"Source lines: {total_lines}")
    print(f"Headings: {len(renderer.headings)}")


if __name__ == "__main__":
    main()
