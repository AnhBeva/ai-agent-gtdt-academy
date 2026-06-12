# Giáo Trình Đào Tạo: AI Agent - Bounded Autonomy Cho Dev/Tech Lead

**Nguồn tham khảo:** `AI agent.pdf` - AI Agent Story: A Developer's Journal with Autonomous Agents.

**Đối tượng:** Dev, Tech Lead, R&D Engineer, Engineering Manager hands-on.

**Ngành áp dụng:** Công ty phần mềm/kỹ thuật có codebase thật, CI/CD, test suite, sản phẩm hoặc hệ thống nội bộ cần tăng tốc phát triển bằng AI agent.

**Thời lượng:** 2 ngày intensive + lộ trình áp dụng 30-60-90 ngày.

**Mục tiêu doanh nghiệp:** Tăng tốc phát triển phần mềm nhưng vẫn kiểm soát chất lượng, giảm hallucination, giảm regression, chuẩn hóa cách team giao việc và kiểm chứng AI agent.

---

## 1. Tuyên Bố Mục Tiêu Đào Tạo

### Học viên sẽ biết gì?

- Vì sao AI code generation nhanh nhưng dễ làm phình codebase, tạo regression và lặp lỗi nếu thiếu ranh giới kiểm chứng.
- Khác biệt giữa "prompt để sinh code" và "thiết kế hệ thống thực thi tự trị có kiểm soát".
- Cấu trúc một vòng agent đáng tin cậy: Planner -> Executor -> Reviewer -> Gate -> Evidence.
- Cách dùng sandbox, scope lock, Definition of Done, test gate, visual gate, benchmark gate và SOL target.
- Cách phân loại nhiệm vụ: mainstream task, edge-case task, rare/custom domain task.
- Cách biến yêu cầu mơ hồ thành engineering contract có thể kiểm chứng bằng máy.

### Học viên sẽ làm được gì?

- Viết được `GOAL.md` cho một task AI agent với objective, scope, locked files, DoD, validation command và evidence requirement.
- Thiết kế được workflow tuyến tính có planner, engineer/executor, reviewer và fail-back loop.
- Xây được verification gate cho compile, lint, unit test, integration test, visual QA, benchmark và security review.
- Chia một project phức tạp thành module nhỏ có interface rõ, giúp agent làm trong "hộp" thay vì tự quyết kiến trúc rộng.
- Đo hiệu quả agent bằng dữ liệu: defect rate, cycle count, test pass rate, latency, throughput, lead time, rework rate.
- Chạy một pilot AI-agent workflow trong repo thật và tạo evidence đủ để lead/manager audit.

### Sau khóa học doanh nghiệp nhận được giá trị gì?

- Chuẩn vận hành AI agent thống nhất cho team kỹ thuật.
- Giảm thời gian làm boilerplate, test iteration và performance tuning.
- Giảm rủi ro agent sửa lan, hallucinate API, bỏ qua edge case hoặc tự tối ưu sai hướng.
- Tăng khả năng reuse prompt, contract, checklist và QA gate giữa các project.
- Có lộ trình 90 ngày để chuyển từ thử nghiệm cá nhân sang team operating model.

---

## 2. Khung Năng Lực Đầu Ra

| Nhóm năng lực | Năng lực | Mô tả | Bằng chứng quan sát được | Phương pháp đánh giá |
|---|---|---|---|---|
| Kiến thức | Bounded autonomy | Hiểu tự trị có kiểm soát là thiết kế ranh giới, không phải tin agent mù quáng | Giải thích được velocity trap, hallucination loop, verification gate | Post-test, thảo luận case |
| Kiến thức | Verification loop | Hiểu planner-executor-reviewer, fail-back và evidence-driven audit | Vẽ được loop cho một task thật trong team | Bài tập nhóm |
| Kiến thức | Task complexity spectrum | Phân biệt task phổ biến, task edge-case, task domain hiếm | Chọn đúng mức steering cho 5 task mẫu | Scenario quiz |
| Kỹ năng | Goal contract design | Viết `GOAL.md` rõ objective, scope, DoD, command, evidence | Một file goal contract dùng được cho repo thật | Rubric 100 điểm |
| Kỹ năng | Acceptance gate design | Thiết kế gate compile/test/visual/benchmark/security | Checklist gate có command và pass/fail rule | Peer review |
| Kỹ năng | Modular decomposition | Chia hệ thống thành module nhỏ với interface chặt | Module map và interface contract | Trainer review |
| Kỹ năng | Agent orchestration | Tổ chức planner, engineer, reviewer theo pipeline tuyến tính | `WORKFLOW.md` hoặc `AGENTS.md` mẫu | Simulation |
| Kỹ năng | Evidence audit | Thu thập log, screenshot, benchmark, test report | Evidence pack cho một pilot task | Applied evaluation |
| Tư duy | Control before speed | Không đánh đổi kiểm soát lấy tốc độ sinh code | Biết dừng agent khi thiếu spec hoặc gate | Role play |
| Tư duy | Process over model | Ưu tiên process, sandbox, compiler gate hơn việc đổi model liên tục | Đề xuất governance model phù hợp team | Case analysis |
| Hành vi | Test before implementation | Đặt test/spec trước khi agent viết code | Task plan có test command trước edit | Observation |
| Hành vi | Escalate unknowns | Khi agent mắc lỗi lặp, chuyển sang đọc docs, đo đạc, hỏi người phụ trách | Failure log có decision point | Simulation |
| Kết quả | Pilot vận hành được | Chạy một AI-agent workflow nhỏ, có gate và evidence | 1 pilot hoàn tất với pass/fail report | 30 ngày follow-up |
| Kết quả | Năng suất có kiểm soát | Lead time giảm nhưng defect/rework không tăng | Dashboard KPI trước/sau | Kirkpatrick Level 4 |

---

## 3. Lộ Trình Đào Tạo Tổng Thể

| Module | Thời lượng | Mục tiêu | Nội dung chính | Đầu ra mong đợi |
|---|---:|---|---|---|
| 1. Mindset: Từ code generation sang bounded autonomy | 2h | Nhận diện rủi ro khi dùng AI agent không có boundary | Software complexity, velocity trap, AI agent vs junior developer, control vs speed | Bản đồ rủi ro AI agent của team |
| 2. Knowledge: Verification loop và agent boundary | 3h | Hiểu cơ chế làm AI agent đáng tin cậy | Planner-executor-reviewer, mathematical verification loop, sandbox, final gate | Sơ đồ loop cho một workflow thật |
| 3. Skill: Viết goal contract và acceptance gate | 3h | Chuyển yêu cầu thành contract có thể kiểm chứng | `GOAL.md`, locked scope, DoD, validation command, evidence | Một `GOAL.md` hoàn chỉnh |
| 4. Practice: Orchestrate agent team tuyến tính | 3h | Thiết kế pipeline đơn giản, dễ audit | `WORKFLOW.md`, role specialization, handoff, fail-back, reviewer gate | Workflow planner-engineer-reviewer |
| 5. Application: Áp dụng vào project thật | 4h | Chọn pilot và chia module cho agent thực thi | Modular autonomy, interface contract, test-first, case IoT/DB/VAD/inference | Pilot plan cho repo/team |
| 6. Measurement: QA, benchmark, visual gate, SOL | 3h | Đo chất lượng, tốc độ và giới hạn vật lý | Compile/lint/test, screenshot gate, benchmark, Speed of Light target | Rubric đo agent execution |
| 7. Competency: Chuẩn hóa AI Agent Engineer | 2h | Chốt chuẩn năng lực và plan 90 ngày | Competency model, manager follow-up, KPI Kirkpatrick, 30-60-90 plan | Action plan cá nhân/team |

---

## 4. Chi Tiết Từng Bài Học

### Bài 1. Velocity Trap: Vì Sao AI Sinh Code Nhanh Nhưng Dễ Tạo Regression?

**Mục tiêu bài học**

- Nhận diện hallucination loop: Error -> Guess -> Fix -> Compile Fail.
- Hiểu vì sao tốc độ không có direction chỉ làm regression nhanh hơn.
- Biết khi nào phải dừng sinh code và chuyển sang đọc docs, đo đạc, kiểm chứng giả định.

**Kiến thức cốt lõi**

- AI agent có tốc độ rất cao nhưng shallow recall và dễ bỏ qua edge case.
- Junior developer thường dừng lại hỏi khi mắc kẹt; agent có thể lặp vô hạn nếu không bị chặn.
- "Define success before generating code" là nguyên tắc khởi đầu.

**Nguyên lý First Principles**

- Code đúng không được xác định bởi vẻ hợp lý của output, mà bởi contract và evidence.
- Nếu không có tiêu chí pass/fail, không thể phân biệt tiến bộ thật với thay đổi ngẫu nhiên.

**Sai lầm thường gặp**

- Prompt một yêu cầu lớn rồi để agent tự sửa đến khi "có vẻ chạy".
- Chỉ review diff thủ công, không bắt buộc test hoặc evidence.
- Đổi model khi lỗi nằm ở thiếu boundary, thiếu spec hoặc thiếu dữ liệu kiểm chứng.
- Cho agent quyền sửa toàn repo với mục tiêu mơ hồ.

**Best Practices**

- Mỗi task phải có objective, scope, DoD và validation command.
- Khi lỗi lặp hơn 2 vòng, bắt buộc đọc docs/log/spec thay vì đoán.
- Luôn yêu cầu evidence: test output, benchmark, screenshot, log, trace.
- Tách task lớn thành module có interface rõ.

**Checklist áp dụng**

| Câu hỏi | Có/Không |
|---|---|
| Task có mục tiêu đo được chưa? | |
| Có biết file/module nào được phép sửa chưa? | |
| Có test hoặc command kiểm chứng chưa? | |
| Có định nghĩa evidence phải nộp chưa? | |
| Có điều kiện dừng hoặc escalation chưa? | |

**Ví dụ thực tế**

Một agent được giao "optimize inference pipeline" bằng một prompt rộng. Kết quả: compile error, hallucinated interface, thay đổi nhiều layer. Khi đổi sang module boundary rõ: Python coordinator, shared memory, C++ compute core, agent làm tốt từng hộp và tăng throughput đáng kể.

**Tình huống thực chiến**

Team backend muốn dùng agent sửa lỗi export PDF bị overflow layout. Học viên phải biến yêu cầu "fix layout overflow" thành goal có locked files, visual gate và screenshot evidence.

**Bài tập thực hành**

Viết lại yêu cầu mơ hồ sau thành bounded task: "Tối ưu API này cho nhanh hơn và sạch hơn".

**Tiêu chí đánh giá**

- Objective có metric: 20 điểm.
- Scope rõ: 20 điểm.
- Validation command cụ thể: 20 điểm.
- Evidence requirement rõ: 20 điểm.
- Có escalation rule: 20 điểm.

### Bài 2. Verification Gate: Thiết Kế Ranh Giới Thay Vì Micro-Manage Code

**Mục tiêu bài học**

- Hiểu vì sao gate quan trọng hơn việc đọc từng dòng code agent viết.
- Thiết kế verification loop có Planner, Executor, Reviewer.
- Phân biệt gate tự động và gate cần người audit.

**Kiến thức cốt lõi**

- Sequential verification loop có khả năng chịu lỗi tốt hơn parallel code dump.
- Reviewer độc lập phải kiểm compile, test, visual QA và evidence.
- Black-box coding có thể chấp nhận nếu interface và gate đủ chặt.

**Nguyên lý First Principles**

- Một module là hộp đen có thể tin được khi input, output, invariant và test được định nghĩa.
- Review không phải cảm nhận; review là kiểm chứng kết quả so với contract.

**Sai lầm thường gặp**

- Cho nhiều agent chạy song song trên cùng codebase không có owner/scope.
- Không có fail-back loop; reviewer phát hiện lỗi nhưng không có cơ chế trả về executor.
- Chỉ dùng lint/compile, bỏ qua functional test hoặc visual test.

**Best Practices**

- Pipeline đơn giản: Planner -> Executor -> Reviewer -> Gate.
- Reviewer không sửa thay executor trừ khi scope rất nhỏ; reviewer trả failure report.
- Gate phải non-negotiable: fail thì chưa xong.
- Evidence lưu vào PR, issue, task log hoặc report.

**Checklist áp dụng**

| Thành phần gate | Cần có |
|---|---|
| Compile/lint command | |
| Unit/integration test | |
| Visual/screenshot check nếu có UI | |
| Benchmark nếu là performance task | |
| Security/static audit nếu chạm auth/data | |
| Evidence path hoặc log | |

**Ví dụ thực tế**

Trong slide deck, visual QA pipeline dùng headless screenshot để phát hiện overlap, text clipping, SVG squish. Agent tự sửa layout cho đến khi gate pass.

**Tình huống thực chiến**

Một dashboard React bị overlap ở mobile. Học viên thiết kế gate gồm Playwright screenshot desktop/mobile, DOM overflow check và acceptance rule "zero overlap, 10-15% padding".

**Bài tập thực hành**

Thiết kế verification gate cho task: "Thêm endpoint upload audio target speaker vào web UI".

**Tiêu chí đánh giá**

- Gate phủ đúng rủi ro: 30 điểm.
- Command/evidence cụ thể: 30 điểm.
- Fail-back rõ: 20 điểm.
- Không over-engineer: 20 điểm.

### Bài 3. Goal Contract: Biến Yêu Cầu Thành `GOAL.md`

**Mục tiêu bài học**

- Viết được goal contract đủ để agent chạy tự trị trong sandbox.
- Khóa phạm vi file, tool, command và Definition of Done.
- Biết dùng checklist để chống scope creep.

**Kiến thức cốt lõi**

- `GOAL.md` là hợp đồng kỹ thuật, không phải mô tả mong muốn.
- Contract tốt có objective hẹp, file boundary, validation command, evidence.
- Checklist giúp theo dõi trạng thái và ngăn agent bỏ sót bước.

**Nguyên lý First Principles**

- Không thể kiểm soát hành vi agent nếu không kiểm soát không gian hành động.
- Autonomy hữu ích khi mục tiêu hẹp, môi trường có sandbox và gate có thể chạy lại.

**Sai lầm thường gặp**

- Viết goal kiểu "improve code quality" không có metric.
- Không khóa file nên agent refactor lan.
- Không nói rõ output evidence.
- Không nêu những thứ không được làm.

**Best Practices**

- Bắt đầu bằng outcome có thể kiểm chứng.
- Tách allowed files và forbidden files.
- Ghi command kiểm chứng dạng copy-ready.
- Ghi pass standard, không chỉ "run tests".

**Checklist áp dụng**

| Mục | Nội dung cần điền |
|---|---|
| Goal | Một câu outcome đo được |
| Mode | manual-assisted/autonomous |
| Allowed scope | File/folder được sửa |
| Forbidden scope | File/folder không được đụng |
| DoD | Điều kiện hoàn tất |
| Validation | Command phải chạy |
| Evidence | Log/screenshot/benchmark/report |
| Escalation | Khi nào dừng và hỏi |

**Ví dụ thực tế**

Goal từ PDF: WhisperCompressProcessor chuyển mono audio samples thành features và trả lengths; validation bằng `cargo test`.

**Tình huống thực chiến**

Học viên chọn một issue trong repo thật và viết goal contract cho agent hoàn thành trong 60-90 phút.

**Bài tập thực hành**

Tạo `GOAL.md` cho task: "Tối ưu VAD pipeline để latency <30ms và không giảm accuracy".

**Tiêu chí đánh giá**

- Objective đo được: 20 điểm.
- Scope lock rõ: 20 điểm.
- DoD testable: 25 điểm.
- Evidence rõ: 20 điểm.
- Escalation hợp lý: 15 điểm.

### Bài 4. Modular Autonomy: Chia Hệ Thống Thành Khối Lego

**Mục tiêu bài học**

- Biết chia hệ thống phức tạp thành module agent có thể xử lý.
- Thiết kế interface đủ chặt để black-box implementation an toàn.
- Phân biệt phần con người nên quyết và phần agent nên làm.

**Kiến thức cốt lõi**

- Agent yếu ở kiến trúc rộng nhưng mạnh khi làm trong hộp có skeleton interface.
- Human giữ vai trò strategic: architecture, contract, audit, steering.
- Agent giữ vai trò tactical: boilerplate, test cycle, profiling, optimization.

**Nguyên lý First Principles**

- Độ tin cậy của hệ thống phức tạp đến từ interface và invariant, không đến từ việc mọi thành phần đều hoàn hảo.
- Complexity nên nằm trong code module, không nằm trong mạng chat giữa nhiều agent.

**Sai lầm thường gặp**

- Dùng swarm agent không có thứ tự, gây hallucination cascade.
- Giao agent tự thiết kế toàn bộ architecture.
- Không có skeleton nên agent tự tạo interface mới.

**Best Practices**

- Thiết kế module map trước khi triển khai.
- Mỗi module có input/output, invariant, owner và test riêng.
- Dùng sequential pipeline thay vì swarm chaos.
- Với domain hiếm, cung cấp steering coordinates chi tiết.

**Checklist áp dụng**

| Câu hỏi | Trả lời |
|---|---|
| Module này có một trách nhiệm chính chưa? | |
| Input/output có typed contract chưa? | |
| Invariant nào không được phá? | |
| Test nào chứng minh module đúng? | |
| Agent có đủ context domain chưa? | |

**Ví dụ thực tế**

Case inference pipeline: một prompt rộng thất bại; khi chia thành Python coordinator, shared memory và C++ compute core, agent xây từng module hiệu quả hơn.

**Tình huống thực chiến**

Team cần thêm batch processing vào service hiện hữu. Học viên phải chia task thành skeleton interface, test gate và executor task.

**Bài tập thực hành**

Vẽ module map cho một feature trong sản phẩm hiện tại, chọn 1 module phù hợp giao agent.

**Tiêu chí đánh giá**

- Module có boundary rõ: 30 điểm.
- Interface có input/output cụ thể: 25 điểm.
- Test/invariant phù hợp: 25 điểm.
- Phân quyền human-agent hợp lý: 20 điểm.

### Bài 5. Operational Control: Team Orchestration Và Fail-Back Loop

**Mục tiêu bài học**

- Thiết kế workflow có role rõ: planner, engineer, reviewer, user/auditor.
- Viết `WORKFLOW.md`/`AGENTS.md` cho agent team tuyến tính.
- Thiết kế fail-back khi compile/test/visual gate fail.

**Kiến thức cốt lõi**

- Orchestration không cần phức tạp; markdown-defined teams đủ hiệu quả cho nhiều use case.
- Planner tạo/cập nhật checklist, engineer code/benchmark, reviewer kiểm đúng/sai.
- User hoặc lead audit quyết định merge, steering hoặc dừng.

**Nguyên lý First Principles**

- Một workflow vận hành được khi mỗi vai trò có input, output và quyền hạn rõ.
- Fail-back là một phần của thiết kế, không phải ngoại lệ.

**Sai lầm thường gặp**

- Planner vừa lập kế hoạch vừa code vừa tự review.
- Reviewer chỉ nói "looks good" không có evidence.
- Không ghi state, khiến lần chạy sau mất bối cảnh.

**Best Practices**

- Dùng checklist trạng thái: pending, in_progress, completed, blocked.
- Reviewer phải trích dẫn evidence.
- Mọi steering hint phải được ghi lại.
- Không thêm agent nếu pipeline 3 vai trò đã đủ.

**Checklist áp dụng**

| Role | Input | Output | Không được làm |
|---|---|---|---|
| Planner | Goal, context, constraints | Plan, checklist, scope | Sửa code nếu không được giao |
| Engineer | Plan, allowed files, tests | Code, logs, benchmark | Mở rộng scope |
| Reviewer | Diff, test result, evidence | Pass/fail report | Bỏ qua gate |
| User/Lead | Business intent, risk | Merge/steer/stop decision | Micro-manage từng dòng |

**Ví dụ thực tế**

Workflow trong PDF: Developer nhận plan và sửa code; Reviewer kiểm visual QA; User audit UX/layout boundary trong cùng sandbox.

**Tình huống thực chiến**

Học viên mô phỏng một PR agent-generated: planner tạo task, engineer đề xuất thay đổi, reviewer phát hiện thiếu test và trả failure report.

**Bài tập thực hành**

Viết `WORKFLOW.md` cho task "fix slide overflow" hoặc task thật trong repo.

**Tiêu chí đánh giá**

- Role rõ: 25 điểm.
- Handoff rõ: 25 điểm.
- Fail-back rõ: 25 điểm.
- Evidence/audit rõ: 25 điểm.

### Bài 6. Measurement: QA Gate, Benchmark Và SOL Optimization

**Mục tiêu bài học**

- Thiết kế metric đúng cho correctness, speed, stability và cost.
- Biết khi nào dùng benchmark và khi nào cần SOL target.
- Không tối ưu mù; biết xác định compute-bound, I/O-bound, network-bound.

**Kiến thức cốt lõi**

- Final gate phải kiểm trong môi trường thật hoặc gần thật: DOM click, microphone, serial/GPIO, real audio stream.
- SOL là giới hạn lý thuyết của phần cứng: CPU/GPU FLOPs, memory bandwidth, network latency.
- Agent performance tuning cần profiler, benchmark script và target rõ.

**Nguyên lý First Principles**

- Tối ưu chỉ có nghĩa khi biết bottleneck và giới hạn vật lý.
- "Nhanh hơn" không phải metric; latency p95, throughput, CPU%, memory leak, contention mới là metric.

**Sai lầm thường gặp**

- Benchmark không cố định input nên kết quả không so sánh được.
- Tối ưu logic khi bottleneck là I/O hoặc network.
- Dừng ở "good enough" dù còn xa giới hạn phần cứng.
- Không đo correctness sau tối ưu.

**Best Practices**

- Luôn có baseline trước tối ưu.
- Ghi benchmark script, input size, machine spec, commit hash.
- Correctness gate chạy trước performance gate.
- Với task ML/audio, đo latency và false positive/false negative.

**Checklist áp dụng**

| Mục đo | Ví dụ |
|---|---|
| Correctness | Test pass, accuracy, false positive |
| Stability | 25h run, memory leak, crash count |
| Latency | p50/p95/p99, <30ms target |
| Throughput | requests/s, generations/s, channels |
| Resource | CPU, GPU, memory bandwidth |
| SOL gap | current vs theoretical limit |

**Ví dụ thực tế**

Case database tuning: agent chạy profiling, phát hiện lock contention, thay global lock bằng fine-grained `RwLock`, sửa memory leak và benchmark 25 giờ.

**Tình huống thực chiến**

Một VAD service cần latency <30ms. Học viên thiết kế benchmark gồm audio dataset, noise profile, accuracy target, ONNX export và p95 latency.

**Bài tập thực hành**

Tạo SOL worksheet cho một pipeline: API, audio inference hoặc database write-heavy.

**Tiêu chí đánh giá**

- Baseline đúng: 20 điểm.
- Bottleneck hypothesis rõ: 20 điểm.
- Metric đo được: 25 điểm.
- SOL target hợp lý: 20 điểm.
- Correctness không bị bỏ qua: 15 điểm.

### Bài 7. Competency: Chuẩn Hóa Cách Team Làm Việc Với AI Agent

**Mục tiêu bài học**

- Chuyển kỹ năng cá nhân thành team operating model.
- Thiết kế KPI và manager follow-up.
- Lập kế hoạch 30-60-90 ngày.

**Kiến thức cốt lõi**

- Governance quan trọng hơn raw model intelligence.
- Team cần shared templates, shared gates và shared dashboard.
- Năng lực thật được chứng minh bằng evidence trong repo thật.

**Nguyên lý First Principles**

- Một năng lực tổ chức chỉ tồn tại khi có chuẩn hành vi, công cụ lặp lại và dữ liệu đo lường.
- Nếu không đo Level 3/Level 4, đào tạo chỉ dừng ở cảm nhận.

**Sai lầm thường gặp**

- Đào tạo xong nhưng không có pilot.
- Không có manager review nên hành vi cũ quay lại.
- Chỉ đo satisfaction, không đo defect/rework/lead time.

**Best Practices**

- Sau khóa học phải có 1 pilot trong 30 ngày.
- Mỗi team có 1 owner quản trị template và QA gate.
- Review hàng tuần dựa trên evidence, không dựa trên cảm nhận.

**Checklist áp dụng**

| Câu hỏi | Có/Không |
|---|---|
| Team có template chung chưa? | |
| Có pilot owner chưa? | |
| Có KPI baseline trước đào tạo chưa? | |
| Manager có lịch follow-up chưa? | |
| Có criteria để scale sau 60 ngày chưa? | |

**Ví dụ thực tế**

Team R&D áp dụng AI agent cho nhiều domain: IoT SDK, eBPF relay, GPU kernels, slide deck generation. Điểm chung không phải model, mà là goal contract, sandbox, verification gate và evidence.

**Tình huống thực chiến**

Học viên xây team adoption plan: chọn 3 workflow phù hợp, định nghĩa templates, chọn KPI và lịch audit.

**Bài tập thực hành**

Hoàn thành 30-60-90 day plan cho team mình.

**Tiêu chí đánh giá**

- Plan thực tế: 25 điểm.
- KPI đo được: 25 điểm.
- Manager follow-up rõ: 25 điểm.
- Có điều kiện scale/stop: 25 điểm.

---

## 5. Case Study

### 3 Case Thành Công

| Case | Bối cảnh | Quyết định | Kết quả | Bài học |
|---|---|---|---|---|
| Rust IoT Board trên ESP32-S3 | Board custom có mic, speaker, ML307 4G, thiếu tài liệu chính thức | Cung cấp hardware link, C reference, pin photo; để agent map register/AT command trong scope hẹp | Boot, record audio, stream TCP qua 4G, playback bằng Rust | Domain hiếm vẫn làm được nếu biến phần cứng thành compiler contract và evidence vật lý |
| Autonomous DB Performance Tuning | Custom IoT DB write-heavy cần chạy ổn định 25h | Cho agent profiler, benchmark script, auto-commit trong boundary; bắt buộc performance evidence | Tìm lock contention, thay global lock bằng `RwLock`, sửa memory leak, giảm spike latency | Agent mạnh ở vòng compile-profile-patch nếu goal và metric rõ |
| Inference Pipeline Optimization | Pipeline audio realtime bị nghẽn khi prompt kiến trúc quá rộng | Chia skeleton thành Python coordinator, shared memory, C++ compute core | TTS tăng từ khoảng 200 lên 800 generations/s; VAD concurrency tăng từ khoảng 10 lên 800 channels | Agent thất bại ở architecture rộng nhưng mạnh khi build trong module box |

### 3 Case Thất Bại

| Case | Bối cảnh | Quyết định sai | Kết quả | Bài học |
|---|---|---|---|---|
| One-shot architecture prompt | Muốn agent decouple toàn bộ inference layer một lần | Prompt rộng, không skeleton, không interface contract | Compile errors, hallucinated APIs, khó audit | Human phải thiết kế contract trước; agent không nên tự quyết kiến trúc lớn |
| Swarm chaos | Nhiều agent cùng xử lý project không có pipeline tuyến tính | Chạy song song nhiều role không scope lock | Cascading hallucination, bug khó truy vết, token cost cao | Pipeline đơn giản, tuần tự, có gate tốt hơn swarm phức tạp |
| Unguided compile loop | Agent gặp lỗi build và tự đoán sửa liên tục | Không bắt đọc docs/log/spec, không escalation | Error -> guess -> fix -> compile fail lặp lại | Khi unknown xuất hiện, chuyển từ guessing sang research và verification |

---

## 6. Bộ Câu Hỏi Tư Duy Theo Bloom's Taxonomy

| Mức Bloom | Câu hỏi |
|---|---|
| Remember | Velocity trap là gì? |
| Remember | Ba vai trò trong verification loop là gì? |
| Understand | Vì sao agent giống junior developer ở edge case nhưng khác ở tốc độ lặp lỗi? |
| Understand | Vì sao "process over raw intelligence" quan trọng hơn đổi model? |
| Apply | Viết DoD cho task "fix PDF export overflow". |
| Apply | Chọn gate phù hợp cho task UI, backend API, ML inference và embedded system. |
| Analyze | Phân tích vì sao one-shot prompt thất bại trong inference pipeline optimization. |
| Analyze | Xác định bottleneck của một service là compute-bound, I/O-bound hay network-bound từ metric cho trước. |
| Evaluate | Khi nào nên cho agent chạy autonomous, khi nào phải giữ human-in-the-loop? |
| Evaluate | Một workflow có 5 agent song song có đáng dùng hơn pipeline 3 bước không? Dựa vào tiêu chí nào? |
| Create | Thiết kế `GOAL.md` và `WORKFLOW.md` cho một pilot trong repo thật của team. |
| Create | Thiết kế dashboard KPI đo hiệu quả AI agent sau 60 ngày. |

### Câu hỏi phản biện

- Nếu test pass nhưng code khó maintain, gate hiện tại thiếu gì?
- Nếu agent tăng throughput nhưng tăng false positive, có được coi là thành công không?
- Nếu model mới mạnh hơn nhưng không có sandbox, rủi ro nào vẫn giữ nguyên?
- Nếu task không có tài liệu online, cần tăng steering như thế nào?

### Câu hỏi phân tích

- Tách một yêu cầu lớn thành 3 module agent-safe.
- Chỉ ra acceptance gate tối thiểu cho từng module.
- Phân tích một failure log để quyết định: retry, read docs, ask human hay stop.

### Câu hỏi đánh giá

- Đánh giá một `GOAL.md` mẫu theo thang 100 điểm.
- Đánh giá một benchmark report có đủ evidence để merge chưa.
- Đánh giá mức sẵn sàng scale AI agent từ cá nhân sang team.

### Câu hỏi ứng dụng

- Chọn một issue thật và viết goal contract.
- Thiết kế fail-back loop cho reviewer.
- Lập plan 30 ngày cho một pilot.

---

## 7. Bộ Workshop Thực Hành

| Hoạt động | Hình thức | Objective | Hướng dẫn | Timebox | Materials | Deliverable | Scoring Guide | Debrief Questions |
|---|---|---|---|---:|---|---|---|---|
| Risk Map | Cá nhân | Nhận diện rủi ro AI agent trong team | Liệt kê 5 workflow đang dùng AI, đánh giá scope/test/evidence | 30' | Risk map template | Bản đồ rủi ro | Rõ workflow 30%, đúng rủi ro 40%, hành động 30% | Rủi ro nào đang bị xem nhẹ nhất? |
| Rewrite Prompt to Goal | Cá nhân | Biến prompt mơ hồ thành contract | Chọn 1 yêu cầu thật, viết objective/scope/DoD/evidence | 45' | `GOAL.md` template | Goal contract | Objective 20%, scope 20%, DoD 25%, evidence 20%, escalation 15% | Điều gì khiến contract này agent-safe? |
| Verification Gate Design | Nhóm | Thiết kế gate cho nhiều loại task | Mỗi nhóm nhận UI/API/ML/embedded scenario và tạo gate | 60' | QA gate checklist | Gate matrix | Risk coverage 35%, command 30%, pass/fail 20%, practicality 15% | Gate nào nên tự động hóa trước? |
| Planner-Engineer-Reviewer Role Play | Role play | Thực hành handoff và fail-back | 3 người đóng vai planner, engineer, reviewer; reviewer trả failure report | 75' | Scenario cards | Failure report + rework plan | Role clarity 25%, evidence 30%, fail-back 25%, communication 20% | Handoff bị thiếu thông tin ở đâu? |
| SOL Optimization Simulation | Simulation | Đo và tối ưu theo bottleneck | Nhận metric giả lập, xác định bottleneck, đặt SOL target | 90' | Benchmark dataset giả lập | SOL worksheet | Baseline 20%, bottleneck 25%, target 25%, validation 30% | Khi nào nên dừng tối ưu? |
| Pilot Design Lab | Nhóm | Tạo plan áp dụng repo thật | Chọn 1 pilot, module map, goal, workflow, KPI | 120' | Pilot plan template | Pilot pack | Feasibility 30%, gate 25%, KPI 25%, adoption plan 20% | Pilot này có thể chạy trong 30 ngày không? |

---

## 8. Bộ Template Dùng Ngay

### 8.1 Checklist: AI Agent Task Readiness

| Hạng mục | Câu hỏi kiểm tra | Pass/Fail | Ghi chú |
|---|---|---|---|
| Objective | Outcome có đo được không? | | |
| Scope | File/folder được phép sửa có rõ không? | | |
| Forbidden scope | Có vùng cấm sửa không? | | |
| Context | Agent có đủ docs/spec/log không? | | |
| Test | Có command kiểm chứng không? | | |
| Evidence | Có yêu cầu log/screenshot/benchmark không? | | |
| Escalation | Có điều kiện dừng/hỏi không? | | |
| Owner | Ai review và quyết định merge? | | |

### 8.2 SOP: Vận Hành Một AI Agent Task

| Bước | Người phụ trách | Hành động | Output | Gate |
|---|---|---|---|---|
| 1 | Human/Planner | Chọn task phù hợp, phân loại complexity | Task brief | Task không quá rộng |
| 2 | Planner | Viết `GOAL.md` và checklist | Goal contract | Lead review |
| 3 | Executor | Chạy trong sandbox, sửa đúng scope | Code/log | Scope check |
| 4 | Reviewer | Chạy compile/test/lint/visual/benchmark | Review report | Pass/fail |
| 5 | Executor | Rework nếu fail | Updated output | Gate rerun |
| 6 | Human/Lead | Audit evidence và quyết định merge | Merge/stop/steer | Evidence đủ |
| 7 | Manager | Ghi KPI và lesson learned | Follow-up note | Dashboard update |

### 8.3 Form: `GOAL.md`

````markdown
# Goal: [Tên task ngắn]

## Objective
[Outcome đo được trong một câu]

## Mode
autonomous | assisted | manual-review-required

## Allowed Scope
- [file/folder được sửa]

## Forbidden Scope
- [file/folder không được sửa]

## Definition of Done
- [Điều kiện hoàn tất 1]
- [Điều kiện hoàn tất 2]
- [Không regression X]

## Validation Commands
```bash
[command build/test/lint/benchmark]
```

## Evidence Required
- Test output:
- Screenshot/video nếu có UI:
- Benchmark report nếu có performance:
- Notes về assumption hoặc blocker:

## Escalation Rules
- Dừng và hỏi nếu [điều kiện].
- Không tự mở rộng scope nếu [điều kiện].
````

### 8.4 Form: `WORKFLOW.md`

```markdown
# AI Agent Workflow

## Roles
- Planner: đọc context, viết plan/checklist, khóa scope.
- Engineer: thực hiện thay đổi trong allowed scope, chạy validation.
- Reviewer: kiểm output, chạy gate, tạo pass/fail report.
- Human Lead: audit evidence, quyết định merge/steer/stop.

## Sequence
1. Planner tạo hoặc cập nhật GOAL.md.
2. Engineer thực thi task trong sandbox.
3. Reviewer chạy gate độc lập.
4. Nếu fail, reviewer gửi failure report cho engineer.
5. Nếu pass, human lead audit evidence.

## Required Evidence
- Diff summary.
- Test/lint/build output.
- Screenshot/benchmark nếu liên quan.
- Known risks.
```

### 8.5 Biểu Mẫu Đánh Giá Goal Contract

| Tiêu chí | Điểm tối đa | Điểm đạt | Nhận xét |
|---|---:|---:|---|
| Objective đo được | 20 | | |
| Scope/forbidden scope rõ | 20 | | |
| DoD testable | 25 | | |
| Validation command copy-ready | 15 | | |
| Evidence requirement rõ | 10 | | |
| Escalation rule hợp lý | 10 | | |
| Tổng | 100 | | |

### 8.6 Biểu Mẫu Báo Cáo Agent Task

| Mục | Nội dung |
|---|---|
| Task ID | |
| Goal | |
| Owner | |
| Agent/model/tool | |
| Start/End | |
| Files changed | |
| Validation commands | |
| Pass/fail result | |
| Evidence links | |
| Cycle count | |
| Defects found | |
| Rework needed | |
| Merge decision | |
| Lesson learned | |

### 8.7 Agent Task Complexity Matrix

| Loại task | Ví dụ | Mức autonomy | Steering cần thiết | Gate tối thiểu |
|---|---|---|---|---|
| Mainstream/simple | CRUD, standard API, UI form | Cao | Template + scope | Build/lint/unit test |
| Mainstream/edge | Auth, payment, concurrency | Trung bình | Spec + negative cases | Integration/security test |
| Custom/domain | IoT board, ML pipeline, custom DB | Thấp đến trung bình | Docs, logs, hardware/data, metric | Physical/benchmark gate |
| Architecture-wide | Refactor nhiều service | Thấp | Human design skeleton trước | Module-by-module gates |

### 8.8 Manager Follow-Up Form

| Tuần | Pilot | Evidence đã có | KPI chính | Blocker | Quyết định tiếp theo |
|---|---|---|---|---|---|
| W1 | | | | | |
| W2 | | | | | |
| W3 | | | | | |
| W4 | | | | | |

---

## 9. Bộ Đánh Giá Năng Lực 100 Điểm

| Giai đoạn | Thành phần | Điểm | Evidence |
|---|---|---:|---|
| Trước đào tạo | Pre-test kiến thức AI agent, gate, risk | 10 | Quiz 15 câu |
| Trước đào tạo | Phân tích một prompt mơ hồ | 10 | Rewrite attempt |
| Sau đào tạo | Post-test concept và case | 15 | Quiz + case answers |
| Sau đào tạo | Viết `GOAL.md` | 20 | Goal contract |
| Sau đào tạo | Thiết kế verification gate | 15 | Gate matrix |
| Sau đào tạo | Role play planner-engineer-reviewer | 10 | Failure report |
| Sau áp dụng | Pilot trong repo/team thật | 15 | Evidence pack |
| Sau áp dụng | Manager review hành vi và KPI | 5 | Follow-up form |
| Tổng | | 100 | |

### Chuẩn đạt

| Mức | Điểm | Diễn giải |
|---|---:|---|
| Chưa đạt | <70 | Hiểu khái niệm nhưng chưa vận hành an toàn |
| Đạt | 70-84 | Có thể viết goal, gate và chạy pilot nhỏ |
| Khá | 85-94 | Có thể hướng dẫn team áp dụng workflow |
| Xuất sắc | 95-100 | Có thể chuẩn hóa operating model và KPI cho nhiều team |

### Rubric đánh giá thực chiến

| Tiêu chí | 1 - Yếu | 2 - Đạt cơ bản | 3 - Tốt | 4 - Xuất sắc |
|---|---|---|---|---|
| Contract clarity | Mơ hồ | Có objective nhưng thiếu scope | Đủ objective/scope/DoD | Có cả forbidden scope/evidence/escalation |
| Gate quality | Không chạy được | Có command nhưng thiếu coverage | Gate phù hợp rủi ro | Gate tự động, repeatable, có evidence |
| Modular design | Task quá rộng | Có chia nhỏ nhưng interface yếu | Module rõ | Interface/invariant/test rất chặt |
| Evidence audit | Cảm tính | Có test output | Có log/screenshot/benchmark | Evidence đủ cho manager/PR audit |
| Business result | Không đo | Đo activity | Đo quality/lead time | Đo được tác động Level 4 |

---

## 10. KPI Đánh Giá Hiệu Quả Đào Tạo Theo Kirkpatrick

| Level | KPI | Cách đo | Nguồn dữ liệu | Target | Thời điểm |
|---|---|---|---|---|---|
| Level 1: Reaction | Điểm hài lòng nội dung | Survey 1-5 | Form cuối khóa | >=4.3/5 | Ngày 2 |
| Level 1: Reaction | Mức hữu ích với công việc | Survey | Form cuối khóa | >=85% chọn hữu ích/cực hữu ích | Ngày 2 |
| Level 2: Learning | Tăng điểm pre/post-test | So sánh điểm | Quiz | +30% trung bình | Ngày 2 |
| Level 2: Learning | Tỷ lệ học viên viết `GOAL.md` đạt chuẩn | Rubric | Bài tập | >=80% đạt >=70 điểm | Ngày 2 |
| Level 2: Learning | Tỷ lệ gate design đạt chuẩn | Rubric | Workshop | >=80% đạt >=70 điểm | Ngày 2 |
| Level 3: Behavior | Số pilot AI-agent workflow chạy thật | Theo dõi task | Jira/GitHub/Linear | >=1 pilot/học viên hoặc team | 30 ngày |
| Level 3: Behavior | Tỷ lệ task agent có contract và evidence | Audit task | PR/task log | >=70% task agent | 60 ngày |
| Level 3: Behavior | Tỷ lệ reviewer gate được thực thi | Audit PR | CI/report | >=80% pilot PR | 60 ngày |
| Level 4: Results | Lead time task phù hợp giảm | So sánh baseline | Jira/GitHub | -20% đến -30% | 90 ngày |
| Level 4: Results | Defect/rework không tăng | Defect count | Bug tracker/PR review | Không tăng so với baseline | 90 ngày |
| Level 4: Results | Throughput engineering tăng có kiểm soát | Completed tasks per sprint | Delivery dashboard | +15% với chất lượng ổn định | 90 ngày |
| Level 4: Results | Knowledge reuse | Số template/gate được tái dùng | Repo docs | >=3 reusable templates/team | 90 ngày |

---

## 11. Sổ Tay Học Viên

### 10 Nguyên Lý Cốt Lõi

1. Đừng micro-manage từng dòng code; hãy thiết kế boundary và gate.
2. Tốc độ không có kiểm chứng là regression nhanh hơn.
3. Agent mạnh trong module hẹp, yếu ở kiến trúc rộng thiếu ranh giới.
4. Goal contract biến yêu cầu mơ hồ thành execution có kiểm soát.
5. Test/spec phải có trước khi agent triển khai.
6. Reviewer độc lập phải kiểm evidence, không chỉ đọc diff.
7. Pipeline tuyến tính thường tốt hơn swarm phức tạp.
8. Khi mắc unknown, dừng guessing và chuyển sang docs/log/measurement.
9. Tối ưu phải dựa trên bottleneck và SOL, không dựa trên cảm giác.
10. Governance, sandbox và compiler gate quan trọng hơn việc đổi model.

### 10 Sai Lầm Phổ Biến

1. Giao task quá rộng cho agent.
2. Không khóa file/folder được phép sửa.
3. Không có Definition of Done.
4. Không có validation command.
5. Không yêu cầu evidence.
6. Để agent tự thiết kế architecture lớn.
7. Chạy nhiều agent song song không có owner.
8. Chỉ đo tốc độ, không đo defect/rework.
9. Tối ưu performance không có baseline.
10. Đào tạo xong không có pilot 30 ngày.

### 10 Checklist Quan Trọng

| Checklist | Câu hỏi nhanh |
|---|---|
| Goal | Outcome có đo được không? |
| Scope | Agent được sửa đâu, không được sửa đâu? |
| Context | Có docs/spec/log/data đủ chưa? |
| DoD | Khi nào coi là xong? |
| Test | Command nào chứng minh đúng? |
| Evidence | Log/screenshot/benchmark ở đâu? |
| Review | Ai kiểm độc lập? |
| Fail-back | Nếu fail, quay lại executor thế nào? |
| Metric | Đo quality, speed, stability ra sao? |
| Adoption | Sau khóa học, pilot nào chạy trước? |

---

## 12. Cheat Sheet 1 Trang

### Công Thức Làm Việc Với AI Agent

```text
Intent -> Goal Contract -> Sandbox -> Executor -> Reviewer -> Gate -> Evidence -> Merge/Steer
```

### 20% Kiến Thức Tạo 80% Giá Trị

- Agent không cần được tin; agent cần được kiểm chứng.
- Human thiết kế contract, architecture boundary và audit decision.
- Agent thực thi boilerplate, compile loop, test cycle, profiling và optimization.
- Mỗi task phải có: objective, scope, DoD, validation, evidence, escalation.
- Dùng pipeline tuyến tính: Planner -> Engineer -> Reviewer.
- Với UI: cần screenshot/overflow gate.
- Với backend: cần unit/integration/security gate.
- Với ML/audio: cần accuracy + latency + dataset gate.
- Với embedded: cần physical/hardware signal gate.
- Với performance: cần baseline + profiler + SOL target.

### Red Flags

- "Optimize this" nhưng không có metric.
- "Refactor whole system" nhưng không có module map.
- "Fix until it works" nhưng không có validation command.
- Agent sửa file ngoài scope.
- Reviewer không có evidence.
- Benchmark không ghi input/machine/commit.

### Metrics Nên Đo

| Nhóm | Metric |
|---|---|
| Quality | test pass rate, defect count, rework rate |
| Speed | lead time, cycle count, time to green |
| Stability | crash count, memory leak, 25h run result |
| Performance | latency p95, throughput, CPU/GPU/memory |
| Adoption | task có GOAL.md, task có evidence, manager follow-up |

### Next Actions Sau Khóa Học

1. Chọn 1 pilot nhỏ nhưng có giá trị thật.
2. Viết `GOAL.md`.
3. Thiết kế gate trước khi chạy agent.
4. Chạy planner-engineer-reviewer.
5. Lưu evidence và review với manager.
6. Chuẩn hóa template nếu pilot thành công.

---

## 13. Lộ Trình Áp Dụng Sau Đào Tạo 30-60-90 Ngày

| Giai đoạn | Việc cần làm | Kết quả mong đợi | KPI | Manager follow-up | Workplace evidence |
|---|---|---|---|---|---|
| 0-30 ngày | Chọn 1-2 pilot task phù hợp; viết `GOAL.md`; chạy workflow planner-engineer-reviewer; thu evidence | Team có trải nghiệm thật với bounded autonomy | >=1 pilot hoàn tất; >=70 điểm rubric | Weekly 30' review pilot | Goal contract, PR/task log, test output |
| 31-60 ngày | Chuẩn hóa template; áp dụng gate cho nhiều task; tạo dashboard basic | Workflow bắt đầu lặp lại được | >=70% agent tasks có contract/evidence; defect không tăng | Review KPI 2 tuần/lần | Template repo, gate checklist, dashboard |
| 61-90 ngày | Scale sang nhiều workflow; thêm benchmark/visual/security gates; đào tạo nội bộ cho người mới | Team operating model ổn định | Lead time giảm 20%; >=3 template reusable; rework không tăng | Monthly business review | Case report, KPI trend, lessons learned |

### Điều kiện scale

- Có ít nhất 3 pilot pass gate với evidence.
- Defect/rework không tăng so với baseline.
- Team dùng chung template thay vì mỗi người tự prompt.
- Manager thấy được KPI Level 3 và Level 4.

### Điều kiện dừng hoặc điều chỉnh

- Agent thường xuyên sửa ngoài scope.
- Gate không phát hiện lỗi thật.
- Lead time giảm nhưng defect tăng.
- Học viên không tạo evidence.
- Task được chọn quá custom nhưng thiếu docs/data/hardware access.

---

## Phụ Lục A. Lịch Trình 2 Ngày Gợi Ý

| Ngày | Khung giờ | Nội dung | Hoạt động |
|---|---|---|---|
| Ngày 1 | 09:00-10:30 | Mindset và velocity trap | Risk map |
| Ngày 1 | 10:45-12:00 | Verification loop | Case discussion |
| Ngày 1 | 13:30-15:00 | Goal contract | Rewrite prompt to goal |
| Ngày 1 | 15:15-17:00 | Acceptance gate | Gate design workshop |
| Ngày 2 | 09:00-10:30 | Modular autonomy | Module map |
| Ngày 2 | 10:45-12:00 | Team orchestration | Role play |
| Ngày 2 | 13:30-15:00 | Measurement và SOL | Simulation |
| Ngày 2 | 15:15-17:00 | Pilot design và 90-day plan | Final presentation |

## Phụ Lục B. Trainer Checklist

| Trước khóa | Trong khóa | Sau khóa |
|---|---|---|
| Thu thập 3-5 workflow AI hiện tại của team | Dùng case thật, không chỉ lý thuyết | Theo dõi pilot 30 ngày |
| Chuẩn bị repo/demo hoặc scenario | Bắt học viên viết goal và gate | Review evidence với manager |
| In template/rubric | Chấm theo rubric 100 điểm | Tổng hợp KPI 60/90 ngày |
| Chốt baseline KPI | Ghi lại red flags phổ biến | Chuẩn hóa template thành team standard |

## Phụ Lục C. Mapping Nội Dung PDF Sang Giáo Trình

| Nội dung trong PDF | Đưa vào giáo trình |
|---|---|
| Software evolution và project complexity | Bài 1 mindset |
| Velocity trap và sane loop | Bài 1, checklist risk |
| AI Agent vs Junior Developer | Bài 1, câu hỏi Bloom |
| Verification gate | Bài 2, QA templates |
| Mathematics of verification loops | Bài 2, roadmap |
| Modular lego-like blocks | Bài 4 |
| Planner-executor-reviewer visualization | Bài 2, 5 |
| Swarm chaos vs linear pipeline | Bài 5 |
| Final gate và SOL | Bài 6 |
| 6 production case studies | Case study và bài tập |
| Modern developer workflow | Khung năng lực, bài 4 |
| Goal-oriented contracts | Bài 3, `GOAL.md` template |
| Bounded autonomy execution | Bài 5 |
| Process over raw intelligence | Bài 7 |
| Tutorial goal/team/QA/steering/SOL | Templates, workshop, roadmap |
