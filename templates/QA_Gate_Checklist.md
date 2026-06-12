# QA Gate Checklist - Cổng Kiểm Chứng Chất Lượng Cho AI Agent

## 1. Bản Chất

QA Gate là hàng rào kiểm chứng trước khi output của AI agent được coi là hoàn tất. Nếu không có gate, team chỉ đang đánh giá bằng cảm giác: code nhìn hợp lý, agent nói đã xong, hoặc demo chạy một lần.

QA Gate chuyển câu hỏi từ:

```text
"Agent có vẻ làm đúng không?"
```

thành:

```text
"Output có pass các kiểm chứng đã định nghĩa không?"
```

Một gate tốt phải:

- Có thể chạy lại.
- Có pass/fail rõ.
- Gắn với rủi ro thật của task.
- Tạo evidence để reviewer audit.
- Không quá nặng đến mức không ai dùng.

## 2. Các Loại Gate Chính

| Gate | Mục đích | Khi bắt buộc dùng |
|---|---|---|
| Compile/build | Chứng minh code build được | Mọi task code |
| Unit test | Chứng minh logic nhỏ đúng | Logic, parser, utility, business rule |
| Integration/e2e test | Chứng minh nhiều module phối hợp đúng | API, workflow, user journey |
| Lint/typecheck | Chứng minh type/style/static rule ổn | TypeScript, Rust, Go, Python project có lint |
| Visual screenshot | Chứng minh UI không vỡ | Frontend, slide, PDF, dashboard |
| Benchmark | Chứng minh performance | Optimization, DB, inference, real-time system |
| Security check | Chứng minh không mở rủi ro bảo mật | Auth, permission, data, file upload, external API |

## 3. Phương Pháp Chọn Gate

Không phải task nào cũng cần mọi gate. Chọn gate theo rủi ro.

| Nếu task chạm vào | Gate tối thiểu |
|---|---|
| Logic thuần | Unit test + lint/typecheck |
| API endpoint | Unit + integration + negative cases |
| UI layout | Build + visual screenshot + interaction test |
| PDF/slide export | Export command + screenshot/PDF review |
| Performance | Correctness test + benchmark baseline/after |
| ML/audio | Dataset test + accuracy + latency |
| Embedded/IoT | Build + serial/GPIO/audio physical evidence |
| Auth/security/data | Security review + permission tests + negative tests |

Nguyên tắc: **gate phải kiểm đúng failure mode quan trọng nhất**.

## 4. Compile/Build Gate

### Mục tiêu

Xác nhận code không phá build. Đây là gate tối thiểu, nhưng không đủ để chứng minh behavior đúng.

### Checklist

| Câu hỏi | Pass/Fail | Evidence |
|---|---|---|
| Build command đã chạy chưa? | | |
| Build có chạy trên môi trường sạch hoặc gần sạch không? | | |
| Có warning nghiêm trọng không? | | |
| Agent có sửa config build ngoài scope không? | | |

### Ví dụ command

```bash
npm run build
cargo build --workspace
go test ./...
python -m pytest
```

## 5. Unit Test Gate

### Mục tiêu

Kiểm tra logic nhỏ, deterministic, chạy nhanh.

### Test tốt cần có

- Happy path.
- Edge cases.
- Error cases.
- Regression case liên quan bug đang sửa.

### Checklist

| Câu hỏi | Pass/Fail | Evidence |
|---|---|---|
| Có test mới cho behavior mới/bug fix không? | | |
| Test fail được trước khi fix không, nếu có thể kiểm? | | |
| Test có edge case không? | | |
| Có skip hoặc xóa test không? | | |

## 6. Lint/Typecheck Gate

### Mục tiêu

Phát hiện lỗi static: type mismatch, unused code, formatting rule, import sai, API misuse.

### Checklist

| Câu hỏi | Pass/Fail | Evidence |
|---|---|---|
| Typecheck pass chưa? | | |
| Lint pass chưa? | | |
| Có disable lint rule không? | | |
| Có any/cast/hack đáng nghi không? | | |

### Ví dụ command

```bash
npm run lint
npm run typecheck
cargo clippy -- -D warnings
ruff check .
mypy .
```

## 7. Visual Screenshot Gate

### Mục tiêu

Kiểm chứng UI, slide, PDF hoặc visual output không bị overlap, clipping, overflow, blank state, sai layout.

### Khi cần

- Sửa giao diện.
- Tạo dashboard.
- Xuất PDF/slide.
- Render canvas/3D/map.
- Có responsive behavior.

### Checklist

| Câu hỏi | Pass/Fail | Evidence |
|---|---|---|
| Có screenshot desktop không? | | |
| Có screenshot mobile không? | | |
| Có kiểm console error không? | | |
| Có kiểm text clipping/overflow không? | | |
| Có kiểm interaction chính không? | | |

### Viewport khuyến nghị

| Loại | Viewport |
|---|---|
| Mobile | 390x844 |
| Tablet | 768x1024 |
| Desktop | 1440x900 |
| Wide | 1920x1080 |

## 8. Benchmark Gate

### Mục tiêu

Chứng minh performance thay đổi theo hướng mong muốn mà không làm hỏng correctness.

### Benchmark bắt buộc có

| Thành phần | Ý nghĩa |
|---|---|
| Baseline | Kết quả trước tối ưu |
| After | Kết quả sau tối ưu |
| Input | Dataset/request size/audio length |
| Environment | Machine, CPU/GPU, memory, OS |
| Metric | Latency, throughput, memory, CPU/GPU |
| Correctness | Test chứng minh kết quả vẫn đúng |

### Checklist

| Câu hỏi | Pass/Fail | Evidence |
|---|---|---|
| Có baseline không? | | |
| Có input cố định không? | | |
| Có chạy đủ số lần để tránh nhiễu không? | | |
| Có correctness gate trước benchmark không? | | |
| Kết quả có so với target không? | | |

## 9. Security Check Gate

### Mục tiêu

Ngăn agent vô tình mở lỗ hổng khi sửa auth, upload, data access, secrets, dependency hoặc external API.

### Checklist

| Rủi ro | Câu hỏi | Pass/Fail | Evidence |
|---|---|---|---|
| Auth | Endpoint có kiểm user/session không? | | |
| Authorization | User có truy cập dữ liệu người khác được không? | | |
| Input validation | Input/file upload có validate size/type không? | | |
| Secrets | Có log hoặc commit secret không? | | |
| Injection | Query/shell/path có sanitize không? | | |
| Dependency | Có thêm package rủi ro không? | | |
| Data privacy | Log có chứa PII/token/audio nhạy cảm không? | | |

## 10. QA Gate Template

````markdown
# QA Gate Checklist

## Task
- Goal:
- Owner:
- Reviewer:
- Date:

## Required Gates
- [ ] Compile/build
- [ ] Unit test
- [ ] Integration/e2e
- [ ] Lint/typecheck
- [ ] Visual screenshot
- [ ] Benchmark
- [ ] Security check

## Commands
```bash
[command 1]
[command 2]
```

## Results
| Gate | Command/Method | Result | Evidence | Reviewer note |
|---|---|---|---|---|
| Build | | pass/fail | | |
| Unit test | | pass/fail | | |
| Lint/type | | pass/fail | | |
| Visual | | pass/fail | | |
| Benchmark | | pass/fail | | |
| Security | | pass/fail | | |

## Decision
- Recommendation: pass | rework | stop | ask-human
- Required rework:
- Residual risks:
````

## 11. Tiêu Chuẩn Pass

Một task chỉ được pass khi:

- Gate bắt buộc theo loại task đã chạy.
- Không có gate fail chưa giải thích.
- Evidence đủ cho reviewer độc lập đọc lại.
- Residual risk được ghi rõ.
- Nếu task performance: correctness không bị giảm.
- Nếu task UI: có ít nhất desktop/mobile evidence.
- Nếu task security-sensitive: có negative test hoặc review note.
