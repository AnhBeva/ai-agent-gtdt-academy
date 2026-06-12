# Manager Follow-up Form - Theo Dõi Áp Dụng AI Agent Sau Đào Tạo

## 1. Bản Chất

Đào tạo AI agent không kết thúc khi học viên hiểu khái niệm. Năng lực thật chỉ xuất hiện khi team thay đổi hành vi trong công việc:

- Có dùng `GOAL.md` trước khi giao task cho agent không?
- Có chạy QA gate không?
- Có evidence để review không?
- Có giảm lead time mà không tăng defect không?
- Có biết khi nào phải dừng agent và steering lại không?

Manager Follow-up Form là công cụ biến đào tạo thành vận hành. Nó giúp manager theo dõi evidence, KPI, blocker và quyết định tiếp theo trong 30-60-90 ngày.

## 2. Vai Trò Của Manager

Manager không cần micro-manage prompt hoặc từng dòng code. Manager cần quản trị 5 việc:

| Vai trò | Câu hỏi manager cần hỏi |
|---|---|
| Chọn pilot | Task nào đủ giá trị nhưng không quá rủi ro? |
| Bắt buộc evidence | Task này có goal, gate và evidence không? |
| Theo dõi KPI | Tốc độ tăng có làm chất lượng giảm không? |
| Gỡ blocker | Team thiếu spec, test, data, quyền tool hay reviewer? |
| Ra quyết định | Scale, steer, stop hay redesign workflow? |

## 3. Evidence Cần Theo Dõi

| Evidence | Mục đích | Ví dụ |
|---|---|---|
| Goal contract | Chứng minh task có boundary | `GOAL.md` |
| Workflow log | Chứng minh role/handoff rõ | Planner/engineer/reviewer notes |
| Test output | Chứng minh correctness | CI log, local test output |
| Visual evidence | Chứng minh UI/PDF không vỡ | Screenshot desktop/mobile |
| Benchmark | Chứng minh performance | before/after latency/throughput |
| Review report | Chứng minh review độc lập | pass/fail report |
| Decision record | Chứng minh manager đã ra quyết định | merge/steer/stop note |

Evidence không cần dài, nhưng phải đủ để một người ngoài task hiểu vì sao output được chấp nhận.

## 4. KPI Cần Theo Dõi

### 4.1 KPI Hành Vi

| KPI | Cách đo | Target 30 ngày | Target 60 ngày | Target 90 ngày |
|---|---|---:|---:|---:|
| Task AI có `GOAL.md` | Số task có goal / tổng task AI | 50% | 70% | 85% |
| Task AI có evidence | Số task có evidence / tổng task AI | 50% | 70% | 85% |
| Review gate được chạy | Số task pass gate / tổng task cần gate | 40% | 70% | 80% |
| Pilot hoàn tất | Số pilot pass DoD | 1/team | 2/team | 3+/team |

### 4.2 KPI Kết Quả

| KPI | Ý nghĩa | Cảnh báo |
|---|---|---|
| Lead time | Tốc độ hoàn thành task | Giảm nhưng defect tăng là không đạt |
| Defect rate | Chất lượng output | Tăng sau khi dùng agent là phải siết gate |
| Rework rate | Mức sửa lại sau review | Cao nghĩa là goal/gate yếu |
| Cycle count | Số vòng agent tự sửa | Quá cao nghĩa là thiếu spec hoặc agent đang guessing |
| Throughput | Số task hoàn tất/sprint | Chỉ tốt nếu quality ổn định |
| Template reuse | Mức chuẩn hóa | Thấp nghĩa là mỗi người tự prompt |

## 5. Blocker Thường Gặp

| Blocker | Dấu hiệu | Hành động của manager |
|---|---|---|
| Thiếu test | Reviewer không có gì để kiểm | Ưu tiên viết test/gate trước task agent |
| Task quá rộng | Agent sửa lan, review khó | Chia module, giảm autonomy |
| Thiếu domain context | Agent hallucinate logic | Bổ sung docs, examples, data, owner |
| Thiếu reviewer | Task pass bằng lời agent | Phân công reviewer độc lập |
| Thiếu benchmark | Performance không chứng minh được | Chuẩn hóa benchmark command |
| Security risk | Chạm auth/data không có review | Bắt buộc security gate |
| Không có time follow-up | Sau khóa học không đổi hành vi | Lên lịch review cố định |

## 6. Next Steering Decision

Sau mỗi follow-up, manager phải chọn một quyết định rõ:

| Quyết định | Khi nào chọn | Hành động |
|---|---|---|
| Continue | Pilot pass, KPI ổn | Tiếp tục thêm task tương tự |
| Scale | Nhiều pilot pass, template ổn | Mở rộng sang team/workflow khác |
| Steer | Output gần đạt nhưng còn blocker | Bổ sung spec/gate/context |
| Reduce autonomy | Agent sửa lan hoặc fail nhiều | Hạ từ L3/L4 xuống L2 |
| Stop | Rủi ro cao, defect tăng | Dừng pilot, review lại design |
| Redesign | Workflow/gate sai bản chất | Thiết kế lại contract/pipeline |

## 7. Weekly Follow-up Form

```markdown
# AI Agent Follow-up Form

## Basic Info
- Team:
- Manager:
- Week:
- Pilot/task:
- Owner:

## Goal & Scope
- Goal link:
- Task type:
- Autonomy level:
- Allowed scope:
- Reviewer:

## Evidence
| Evidence type | Link/path | Status | Notes |
|---|---|---|---|
| GOAL.md | | present/missing | |
| Workflow log | | present/missing | |
| Test output | | pass/fail/missing | |
| Visual evidence | | pass/fail/not-needed | |
| Benchmark | | pass/fail/not-needed | |
| Security check | | pass/fail/not-needed | |
| Review report | | pass/fail/missing | |

## KPI
| KPI | Baseline | Current | Target | Status |
|---|---:|---:|---:|---|
| Lead time | | | | |
| Defect count | | | | |
| Rework count | | | | |
| Agent cycle count | | | | |
| Test pass rate | | | | |
| Template reuse | | | | |

## Blockers
- Blocker 1:
- Blocker 2:
- Support needed:

## Manager Decision
- Decision: continue | scale | steer | reduce-autonomy | stop | redesign
- Reason:
- Next action:
- Owner:
- Due date:

## Lessons Learned
- What worked:
- What failed:
- Template/gate update needed:
```

## 8. 30-60-90 Follow-up Cadence

| Giai đoạn | Mục tiêu manager | Câu hỏi trọng tâm | Output |
|---|---|---|---|
| 0-30 ngày | Có pilot thật | Team có dùng goal/gate/evidence không? | 1 pilot report |
| 31-60 ngày | Chuẩn hóa hành vi | Template nào được reuse? Gate nào thiếu? | Team template pack |
| 61-90 ngày | Đo kết quả business | Lead time/defect/rework thay đổi thế nào? | Adoption decision |

## 9. Mẫu Review 30 Phút Hàng Tuần

| Thời lượng | Nội dung |
|---:|---|
| 5' | Nhắc lại pilot goal và KPI |
| 10' | Xem evidence: goal, gate, test, review |
| 5' | Xem blocker và cycle count |
| 5' | Chọn decision: continue/steer/stop |
| 5' | Chốt next action, owner, due date |

Manager nên yêu cầu evidence trước cuộc họp. Không dùng 30 phút để nghe kể lại toàn bộ quá trình.

## 10. Dấu Hiệu Adoption Đúng

- Học viên tự viết goal trước khi prompt agent.
- Reviewer hỏi evidence thay vì hỏi "agent nói gì".
- Task lớn được chia module trước khi giao.
- Manager nhìn dashboard KPI, không chỉ nghe cảm nhận.
- Team reuse template thay vì mỗi người tự chế prompt.
- Agent được dùng nhiều hơn ở task phù hợp, ít hơn ở task rủi ro.

## 11. Dấu Hiệu Cần Can Thiệp

- Lead time giảm nhưng bug tăng.
- Agent cycle count cao bất thường.
- Nhiều task không có goal/evidence.
- Reviewer bị bỏ qua vì "agent đã test rồi".
- Task security/performance không có gate riêng.
- Team dùng AI nhiều nhưng không có template reuse.

## 12. Manager Scorecard

| Tiêu chí | 0 điểm | 1 điểm | 2 điểm |
|---|---|---|---|
| Pilot | Không có | Có nhưng mơ hồ | Có goal/gate/evidence |
| Evidence | Không lưu | Lưu rời rạc | Lưu đủ để audit |
| KPI | Không đo | Đo activity | Đo behavior/result |
| Follow-up | Không có lịch | Có nhưng không đều | Đều và có decision |
| Template reuse | Không có | Cá nhân dùng | Team dùng chung |

Tổng 0-4: adoption yếu. Tổng 5-7: đang hình thành. Tổng 8-10: có thể scale.
