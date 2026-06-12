# WORKFLOW.md - Quy Trình Điều Phối AI Agent Tuyến Tính

## 1. Bản Chất

`WORKFLOW.md` mô tả cách nhiều vai trò phối hợp để biến một `GOAL.md` thành output đã được kiểm chứng. Nếu `GOAL.md` là hợp đồng mục tiêu, thì `WORKFLOW.md` là quy trình vận hành.

Mục tiêu của workflow không phải tạo thật nhiều agent. Mục tiêu là tạo một chuỗi trách nhiệm rõ:

```text
Planner -> Engineer/Executor -> Reviewer -> Human Lead -> Merge/Steer/Stop
```

Workflow tốt giúp team tránh 3 lỗi phổ biến:

- Một agent vừa lập kế hoạch, vừa code, vừa tự review nên không có kiểm chứng độc lập.
- Nhiều agent chạy song song không scope lock, tạo xung đột và hallucination cascade.
- Reviewer phát hiện lỗi nhưng không có fail-back rule để trả task về executor.

Nguyên tắc: **pipeline tuyến tính, role rõ, handoff rõ, gate rõ**.

## 2. Role Sequence

| Role | Trách nhiệm chính | Input nhận vào | Output phải tạo | Không được làm |
|---|---|---|---|---|
| Planner | Hiểu goal, chia bước, khóa scope, chuẩn bị checklist | User intent, repo context, `GOAL.md` | Plan, task checklist, risk note | Không tự ý sửa code nếu workflow không cho phép |
| Engineer/Executor | Thực thi trong allowed scope, chạy validation sơ bộ | Plan, allowed files, context, commands | Code/config/test changes, execution log | Không mở rộng scope, không skip test |
| Reviewer | Kiểm độc lập output so với DoD và gate | Diff, logs, commands, evidence | Pass/fail report, rework request | Không pass khi thiếu evidence |
| Human Lead | Quyết định merge, steer, stop hoặc mở scope | Review report, evidence, business context | Decision record | Không micro-manage từng dòng nếu gate đủ |
| Manager/Owner | Theo dõi adoption và KPI sau task | Task report, KPI, blocker | Follow-up action | Không chỉ đo cảm nhận |

## 3. Handoff Rule

Handoff là điểm bàn giao giữa các vai trò. Handoff yếu làm agent sau phải đoán lại bối cảnh.

### 3.1 Planner -> Engineer

Planner chỉ bàn giao khi có:

- Objective rõ.
- Allowed/forbidden scope.
- Checklist từng bước.
- Validation commands.
- Known risks.
- Expected evidence.

Mẫu handoff:

```markdown
## Planner Handoff
- Goal:
- Allowed scope:
- Forbidden scope:
- Implementation sequence:
- Validation commands:
- Evidence required:
- Risks:
```

### 3.2 Engineer -> Reviewer

Engineer chỉ bàn giao khi có:

- Diff summary.
- Files changed.
- Commands đã chạy.
- Kết quả pass/fail.
- Evidence path.
- Known limitations.

Mẫu handoff:

```markdown
## Engineer Handoff
- Summary:
- Files changed:
- Commands run:
- Results:
- Evidence:
- Known risks:
```

### 3.3 Reviewer -> Engineer

Nếu fail, reviewer phải trả failure report có thể hành động được:

```markdown
## Failure Report
- Failed gate:
- Evidence:
- Expected behavior:
- Actual behavior:
- Likely area:
- Required rework:
- Do not change:
```

Reviewer không nên viết kiểu "fix it" vì executor sẽ lại đoán.

### 3.4 Reviewer -> Human Lead

Nếu pass, reviewer bàn giao:

- DoD status.
- Evidence summary.
- Residual risk.
- Merge recommendation.

## 4. Fail-Back Rule

Fail-back là quy tắc khi output không pass gate. Đây là phần bắt buộc trong bounded autonomy.

| Tình huống fail | Hành động | Ai quyết định |
|---|---|---|
| Compile/lint fail do lỗi rõ | Trả về Engineer sửa trong scope | Reviewer |
| Test fail do behavior sai | Trả failure report, yêu cầu sửa logic/test | Reviewer |
| Visual fail | Trả screenshot + vị trí lỗi + viewport | Reviewer |
| Benchmark không đạt | Yêu cầu profiler/baseline hoặc đổi hypothesis | Reviewer/Human Lead |
| Cần sửa ngoài scope | Dừng và xin mở scope | Human Lead |
| Fail cùng lỗi quá 2 vòng | Dừng guessing, chuyển sang docs/log/research | Human Lead |
| Spec mơ hồ | Dừng và hỏi người sở hữu business/technical intent | Human Lead |

Nguyên tắc: fail không phải thất bại; fail là tín hiệu để thu hẹp giả định và tăng evidence.

## 5. Review Checklist

| Nhóm kiểm tra | Câu hỏi | Pass/Fail | Evidence |
|---|---|---|---|
| Scope | Agent có chỉ sửa allowed files không? | | |
| Objective | Output có đạt outcome trong goal không? | | |
| DoD | Từng DoD đã pass chưa? | | |
| Build | Build/compile có pass không? | | |
| Test | Unit/integration/e2e test có pass không? | | |
| Lint/type | Lint/typecheck có pass không? | | |
| Visual | Screenshot có overflow/clipping không? | | |
| Performance | Benchmark có baseline và target không? | | |
| Security | Có chạm auth/data/permission không? Nếu có, đã kiểm chưa? | | |
| Evidence | Evidence đủ cho người khác audit không? | | |
| Risk | Có residual risk nào cần ghi lại không? | | |

## 6. Template Copy-Ready

```markdown
# AI Agent Workflow

## Workflow Objective
[Mục tiêu quy trình: ví dụ chạy AI agent task có kiểm chứng trong repo thật]

## Roles
- Planner:
- Engineer/Executor:
- Reviewer:
- Human Lead:
- Manager/Owner:

## Sequence
1. Planner đọc `GOAL.md`, repo context và tạo checklist.
2. Engineer thực thi trong allowed scope.
3. Engineer chạy validation command sơ bộ và ghi evidence.
4. Reviewer kiểm diff, chạy lại gate độc lập nếu có thể.
5. Nếu fail, Reviewer tạo failure report và trả về Engineer.
6. Nếu pass, Reviewer gửi pass report cho Human Lead.
7. Human Lead quyết định merge, steer, stop hoặc mở scope.
8. Manager/Owner ghi KPI và follow-up nếu là pilot/adoption task.

## Planner Handoff
- Goal:
- Allowed scope:
- Forbidden scope:
- Implementation sequence:
- Validation commands:
- Evidence required:
- Risks:

## Engineer Handoff
- Summary:
- Files changed:
- Commands run:
- Results:
- Evidence:
- Known risks:

## Reviewer Report
- Scope compliance:
- DoD status:
- Validation result:
- Evidence reviewed:
- Failed gates:
- Residual risks:
- Recommendation: pass | rework | stop | ask-human

## Fail-Back Rules
- Compile/lint/test fail: return to Engineer with exact error and expected fix area.
- Same failure repeats twice: stop guessing and request docs/log/human input.
- Out-of-scope change needed: Human Lead must approve scope expansion.
- Missing evidence: cannot pass.

## Review Checklist
- [ ] Scope respected
- [ ] DoD pass
- [ ] Build pass
- [ ] Tests pass
- [ ] Lint/typecheck pass
- [ ] Visual/benchmark/security gates checked where relevant
- [ ] Evidence recorded
- [ ] Residual risks documented
```

## 7. Ví Dụ Workflow Cho UI Visual Fix

```markdown
# AI Agent Workflow: Fix Slide Visual Overflow

## Roles
- Planner: xác định slide lỗi, viewport cần kiểm, file được sửa.
- Engineer: chỉnh layout/style trong allowed scope.
- Reviewer: chạy screenshot gate và kiểm clipping/overlap.
- Human Lead: duyệt merge nếu visual pass.

## Sequence
1. Planner tạo checklist: reproduce -> fix -> screenshot -> export.
2. Engineer sửa CSS/layout.
3. Engineer chạy `npm run build` và `npm run test:visual`.
4. Reviewer chạy lại visual test ở 390px và 1440px.
5. Nếu còn overlap, reviewer gửi screenshot và vị trí lỗi.
6. Nếu pass, Human Lead kiểm PDF export.

## Fail-Back Rules
- Nếu sửa global theme gây regression, revert phần global và tìm fix cục bộ.
- Nếu text vẫn clipping sau 2 vòng, mở lại layout constraint với Human Lead.
```

## 8. Dấu Hiệu Workflow Yếu

- Không biết ai có quyền quyết định merge.
- Reviewer không có checklist hoặc evidence.
- Engineer tự mở rộng scope.
- Planner không ghi assumption.
- Fail report chỉ nói chung chung.
- Task pass dù validation chưa chạy.
- Không có nơi ghi residual risk.

## 9. Tiêu Chuẩn Workflow Xuất Sắc

Workflow được coi là tốt khi một người mới trong team có thể đọc `GOAL.md` + `WORKFLOW.md` và hiểu:

- Việc cần làm là gì.
- Ai làm bước nào.
- Khi nào được chuyển bước.
- Khi nào phải trả về.
- Command nào chứng minh pass.
- Evidence nào cần lưu.
- Ai quyết định cuối cùng.
