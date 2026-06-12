# Agent Task Complexity Matrix - Ma Trận Độ Phức Tạp Nhiệm Vụ AI Agent

## 1. Bản Chất

Không phải task nào cũng phù hợp để giao AI agent ở cùng mức tự trị. Ma trận độ phức tạp giúp team quyết định:

- Task này agent có thể tự làm đến đâu?
- Cần con người steering ở mức nào?
- Gate tối thiểu là gì?
- Có nên chia nhỏ task trước khi giao không?
- Khi nào nên dừng autonomous mode?

Nguyên tắc: **mức tự trị phải tỷ lệ nghịch với độ mơ hồ và độ đặc thù domain**.

Task càng phổ biến, có nhiều tài liệu, có test rõ, interface chuẩn thì agent càng tự trị được. Task càng custom, ít tài liệu, phụ thuộc business logic, hardware, ML data hoặc kiến trúc lớn thì cần steering chặt hơn.

## 2. Hai Trục Đánh Giá

### 2.1 Độ phổ biến của nhiệm vụ

| Mức | Mô tả | Ví dụ |
|---|---|---|
| Mainstream | Có nhiều pattern, docs, example online | CRUD, form UI, REST endpoint, standard auth flow |
| Semi-custom | Có framework phổ biến nhưng business rule riêng | Billing rule, data sync, internal workflow |
| Custom/domain | Ít tài liệu, phụ thuộc hệ thống riêng | Custom IoT DB, VAD tiếng Việt, hardware board |
| Novel/research | Chưa rõ giải pháp, cần thử nghiệm | New ML architecture, GPU kernel tuning, protocol design |

### 2.2 Độ rủi ro thay đổi

| Mức | Mô tả | Ví dụ |
|---|---|---|
| Low | Sửa cục bộ, dễ rollback | Text, style, small utility |
| Medium | Chạm logic hoặc nhiều component | API, data transform, UI flow |
| High | Chạm production path, auth, data, performance | Payment, permission, DB migration |
| Critical | Có thể ảnh hưởng an toàn, dữ liệu, khách hàng lớn | Security, embedded hardware, realtime inference |

## 3. Ma Trận Chính

| Loại task | Ví dụ | Required steering | Acceptable autonomy level | Gate tối thiểu |
|---|---|---|---|---|
| Mainstream/simple | UI form, CRUD endpoint, docs update | Goal + scope + command | High autonomous | Build, lint, unit test |
| Mainstream/edge | Auth callback, file upload, concurrency bug | Spec + negative cases + reviewer | Medium autonomous | Integration, security, edge test |
| Semi-custom/business | Pricing rule, approval workflow, report logic | Business examples + acceptance cases | Assisted | Unit + integration + business scenario |
| Custom/codebase-specific | Internal SDK, legacy refactor, custom protocol | Architecture note + interface skeleton | Assisted/low autonomous | Module test + regression suite |
| Hardware/embedded | ESP32 board, UART/I2S/GPIO | Pin map, physical setup, logs | Low autonomous | Build + hardware evidence |
| ML/audio | VAD, speaker detection, ONNX export | Dataset, metric, latency target | Assisted | Accuracy + latency + export gate |
| Performance/SOL | DB tuning, GPU kernel, relay throughput | Baseline, profiler, target, SOL worksheet | Assisted | Correctness + benchmark + stability |
| Architecture-wide | Split service, redesign pipeline | Human architecture first | Low autonomous | Phase gates per module |
| Security-sensitive | Auth, secrets, permissions, upload | Threat model + negative tests | Low autonomous | Security review + abuse cases |
| Research/unknown | No clear solution yet | Human-in-the-loop research | Manual-assisted | Experiment log + decision review |

## 4. Cấp Độ Tự Trị

| Level | Tên | Mô tả | Khi dùng |
|---|---|---|---|
| L0 | Human only | Con người tự làm, agent chỉ tham khảo | Rủi ro cao, spec chưa rõ |
| L1 | Suggestion | Agent phân tích/đề xuất, không sửa file | Research, design review |
| L2 | Assisted edit | Agent sửa nhưng human steer liên tục | Semi-custom, thiếu test |
| L3 | Bounded autonomous | Agent tự chạy trong scope/gate rõ | Mainstream hoặc module hẹp |
| L4 | Goal-driven loop | Agent tự fix/test nhiều vòng trong sandbox | Task có test/gate mạnh |
| L5 | Production autonomous | Agent tự tạo PR pass CI nhưng vẫn human merge | Chỉ khi governance rất trưởng thành |

Khuyến nghị cho đa số team: bắt đầu L2-L3, chỉ lên L4 khi gate đã ổn định.

## 5. Required Steering

Steering là thông tin định hướng giúp agent không đoán.

| Loại steering | Khi cần | Ví dụ |
|---|---|---|
| Spec steering | Behavior cần đúng | API contract, acceptance criteria |
| Scope steering | Ngăn sửa lan | allowed/forbidden files |
| Architecture steering | Ngăn agent tự thiết kế rộng | skeleton interface, module map |
| Domain steering | Domain hiếm | hardware pin, audio sample, protocol docs |
| Metric steering | Performance/ML | latency target, accuracy, throughput |
| Failure steering | Khi agent lặp lỗi | logs, profiler, docs, exact error |
| Safety steering | Security/data | threat note, permission model |

Nếu task cần nhiều loại steering mà chưa có, không nên chạy autonomous.

## 6. Cách Chấm Điểm Task

Chấm mỗi tiêu chí 1-5 điểm. Điểm càng cao càng rủi ro/mơ hồ.

| Tiêu chí | 1 điểm | 3 điểm | 5 điểm |
|---|---|---|---|
| Domain familiarity | Rất phổ biến | Có phần custom | Hiếm/không có docs |
| Scope clarity | Rõ file/module | Rõ feature nhưng rộng | Mơ hồ/toàn hệ thống |
| Test availability | Test tốt | Có test thiếu coverage | Không có test |
| Blast radius | Cục bộ | Nhiều module | Production-critical |
| Data/hardware dependency | Không | Có mock | Cần dữ liệu/hardware thật |
| Performance sensitivity | Không | Có target mềm | Có SLA/SOL |
| Security sensitivity | Không | Có user data | Auth/secret/permission |

### Diễn giải tổng điểm

| Tổng điểm | Mức | Khuyến nghị |
|---:|---|---|
| 7-14 | Low complexity | L3-L4 được nếu có gate |
| 15-22 | Medium | L2-L3, reviewer chặt |
| 23-30 | High | L1-L2, cần chia nhỏ và thêm spec |
| 31-35 | Critical | Không autonomous; human design trước |

## 7. Template Matrix

```markdown
# Agent Task Complexity Assessment

## Task
- Name:
- Owner:
- Repo/module:
- Business/engineering value:

## Classification
| Dimension | Score 1-5 | Notes |
|---|---:|---|
| Domain familiarity | | |
| Scope clarity | | |
| Test availability | | |
| Blast radius | | |
| Data/hardware dependency | | |
| Performance sensitivity | | |
| Security sensitivity | | |
| Total | | |

## Decision
- Task type:
- Recommended autonomy level: L0/L1/L2/L3/L4/L5
- Required steering:
- Required gates:
- Must split before execution: yes/no

## Steering Package Needed
- Spec:
- Scope:
- Architecture skeleton:
- Domain docs/data:
- Metrics:
- Safety constraints:

## Stop Conditions
- Stop if:
- Ask human if:
- Do not change:
```

## 8. Ví Dụ Chấm Điểm

### Ví dụ 1: Thêm form UI đơn giản

| Tiêu chí | Điểm |
|---|---:|
| Domain familiarity | 1 |
| Scope clarity | 1 |
| Test availability | 2 |
| Blast radius | 1 |
| Data/hardware dependency | 1 |
| Performance sensitivity | 1 |
| Security sensitivity | 1 |
| Tổng | 8 |

Khuyến nghị: L3 bounded autonomous. Gate: build, lint, component test, screenshot.

### Ví dụ 2: Optimize VAD tiếng Việt <30ms

| Tiêu chí | Điểm |
|---|---:|
| Domain familiarity | 4 |
| Scope clarity | 3 |
| Test availability | 3 |
| Blast radius | 4 |
| Data/hardware dependency | 4 |
| Performance sensitivity | 5 |
| Security sensitivity | 2 |
| Tổng | 25 |

Khuyến nghị: L2 assisted. Cần dataset, metric latency/accuracy, SOL worksheet, benchmark gate.

### Ví dụ 3: Refactor auth permission model

| Tiêu chí | Điểm |
|---|---:|
| Domain familiarity | 3 |
| Scope clarity | 4 |
| Test availability | 3 |
| Blast radius | 5 |
| Data/hardware dependency | 2 |
| Performance sensitivity | 2 |
| Security sensitivity | 5 |
| Tổng | 24 |

Khuyến nghị: L1-L2. Human phải thiết kế permission model và abuse cases trước; agent chỉ làm module nhỏ.

## 9. Sai Lầm Khi Phân Loại

- Thấy task quen thuộc nên bỏ qua edge case security.
- Thấy agent làm nhanh nên tăng autonomy quá sớm.
- Không tính blast radius.
- Không phân biệt "có test" và "test đủ kiểm behavior".
- Không hạ autonomy khi task phụ thuộc dữ liệu/hardware thật.
- Giao architecture-wide task khi chưa có skeleton.

## 10. Tiêu Chuẩn Quyết Định Tốt

Một quyết định phân loại task tốt phải nêu rõ:

- Task thuộc loại nào.
- Vì sao mức autonomy được chọn là phù hợp.
- Steering package nào cần chuẩn bị trước.
- Gate nào bắt buộc.
- Khi nào phải dừng hoặc hỏi người.
