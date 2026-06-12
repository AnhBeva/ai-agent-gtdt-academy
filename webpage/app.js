(function () {
  const progressBar = document.getElementById("progressBar");
  const readPercent = document.getElementById("readPercent");
  const sidebar = document.getElementById("sidebar");
  const menuBtn = document.getElementById("menuBtn");
  const printBtn = document.getElementById("printBtn");
  const searchInput = document.getElementById("searchInput");
  const toTop = document.getElementById("toTop");
  const tocLinks = Array.from(document.querySelectorAll(".toc-link"));
  const sections = Array.from(document.querySelectorAll("[id]"))
    .filter((el) => /^(H1|H2|SECTION)$/.test(el.tagName))
    .filter((el) => el.id);

  function updateProgress() {
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const max = document.documentElement.scrollHeight - window.innerHeight;
    const pct = max > 0 ? Math.min(100, Math.max(0, (scrollTop / max) * 100)) : 0;
    progressBar.style.width = pct.toFixed(1) + "%";
    readPercent.textContent = Math.round(pct) + "%";
    toTop.classList.toggle("show", scrollTop > 900);
  }

  function updateActiveToc() {
    let current = sections[0] && sections[0].id;
    const offset = 120;
    for (const section of sections) {
      const top = section.getBoundingClientRect().top;
      if (top <= offset) current = section.id;
      else break;
    }
    tocLinks.forEach((link) => {
      link.classList.toggle("active", link.dataset.target === current);
    });
  }

  function onScroll() {
    updateProgress();
    updateActiveToc();
  }

  function copyCode(button) {
    const card = button.closest(".code-card");
    const code = card && card.querySelector("pre code");
    if (!code) return;
    navigator.clipboard.writeText(code.textContent || "").then(() => {
      const old = button.textContent;
      button.textContent = "Đã sao chép";
      setTimeout(() => {
        button.textContent = old;
      }, 1400);
    });
  }

  function runSearch(value) {
    const query = value.trim().toLowerCase();
    const docs = Array.from(document.querySelectorAll(".doc-section"));
    docs.forEach((section) => {
      section.classList.remove("search-hit");
      if (!query) {
        section.classList.remove("search-hidden");
        return;
      }
      const hit = section.textContent.toLowerCase().includes(query);
      section.classList.toggle("search-hidden", !hit);
      section.classList.toggle("search-hit", hit);
    });
  }

  document.addEventListener("click", (event) => {
    const target = event.target;
    if (target.matches(".copy-code")) copyCode(target);
    if (target.matches(".toc-link") && sidebar.classList.contains("open")) {
      sidebar.classList.remove("open");
      menuBtn.setAttribute("aria-expanded", "false");
    }
    const templateCard = target.closest(".template-card");
    if (templateCard && templateCard.dataset.jumpSource) {
      event.preventDefault();
      const first = document.querySelector(`.source-${templateCard.dataset.jumpSource}`);
      if (first) first.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  });

  menuBtn.addEventListener("click", () => {
    const open = sidebar.classList.toggle("open");
    menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
  });

  printBtn.addEventListener("click", () => window.print());
  searchInput.addEventListener("input", (event) => runSearch(event.target.value));
  toTop.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll);

  updateProgress();
  updateActiveToc();
})();
