# GOAL.md - Hợp Đồng Mục Tiêu Cho AI Agent

## 1. Bản Chất

`GOAL.md` là hợp đồng thực thi giữa con người và AI agent. Nó biến một mong muốn mơ hồ thành một nhiệm vụ có ranh giới, có điều kiện hoàn tất, có lệnh kiểm chứng và có bằng chứng để audit.

AI agent không nên được giao việc bằng kiểu: "sửa cho tốt hơn", "tối ưu đi", "refactor lại". Những câu này thiếu tiêu chuẩn đúng/sai. Agent sẽ tự suy diễn, sửa lan, tạo API giả, hoặc lặp vòng đoán lỗi. `GOAL.md` giải quyết vấn đề đó bằng cách khóa 6 điểm:

| Thành phần | Ý nghĩa |
|---|---|
| Objective | Kết quả cuối cùng phải đạt, viết sao cho đo được |
| Scope | Vùng agent được phép làm việc |
| Locked files | File/folder được phép hoặc không được phép sửa |
| DoD | Definition of Done, điều kiện hoàn tất không thể thương lượng |
| Validation commands | Lệnh kiểm chứng bắt buộc chạy |
| Evidence | Bằng chứng phải nộp để reviewer/manager tin kết quả |

Nguyên tắc cốt lõi: **agent được tự do trong hộp, nhưng hộp phải do con người thiết kế**.

## 2. Khi Nào Cần Dùng

Dùng `GOAL.md` khi task có một trong các điều kiện sau:

- Agent có thể sửa code, config, test, tài liệu hoặc workflow.
- Task có nguy cơ regression nếu sửa lan.
- Task cần chạy nhiều vòng compile/test/fix.
- Task liên quan performance, UI, ML, embedded, security hoặc dữ liệu thật.
- Task sẽ được giao cho agent chạy tương đối tự trị.

Không cần dùng bản đầy đủ nếu task chỉ là hỏi đáp, đọc code, hoặc viết nháp không chạm repository.

## 3. Phương Pháp Viết Objective

Objective tốt phải có 4 đặc điểm:

| Tiêu chí | Câu hỏi kiểm tra | Ví dụ tốt | Ví dụ yếu |
|---|---|---|---|
| Cụ thể | Kết quả là gì? | "Thêm endpoint upload audio target speaker" | "Cải thiện audio feature" |
| Đo được | Biết pass/fail bằng gì? | "Post-test pass, file audio replay được trong UI" | "Hoạt động tốt" |
| Hẹp | Có thể hoàn tất trong một task? | "Sửa overflow ở slide 23" | "Làm lại toàn bộ deck" |
| Gắn giá trị | Vì sao cần làm? | "Để reviewer kiểm target speaker trước khi inference" | "Cho sạch hơn" |

Mẫu câu:

```text
Hoàn thành [kết quả cụ thể] cho [phạm vi/module] sao cho [điều kiện đo được], được kiểm chứng bằng [lệnh/gate/evidence].
```

Ví dụ:

```text
Hoàn thành upload và replay target speaker audio trong Web UI sao cho người dùng có thể upload hoặc record audio, phát lại audio đã chọn, và test mock realtime voice pass bằng command npm test.
```

## 4. Scope Và Locked Files

Scope là vùng hành động hợp pháp của agent. Locked files là cơ chế ngăn agent "giải quyết vấn đề" bằng cách sửa những nơi không nên sửa.

### 4.1 Allowed Scope

Ghi rõ file/folder được sửa:

```markdown
## Allowed Scope
- `src/features/audio-upload/**`
- `src/components/TargetSpeakerRecorder.tsx`
- `tests/audio-upload.test.ts`
```

### 4.2 Forbidden Scope

Ghi rõ vùng cấm:

```markdown
## Forbidden Scope
- Không sửa authentication middleware.
- Không đổi database schema.
- Không sửa public API contract ngoài endpoint đã nêu.
- Không xóa hoặc skip test hiện có.
```

### 4.3 Scope Tốt Và Scope Xấu

| Loại | Ví dụ | Rủi ro |
|---|---|---|
| Scope quá rộng | "Sửa trong toàn repo nếu cần" | Agent refactor lan, khó review |
| Scope quá hẹp | "Chỉ sửa 1 file" trong khi test cần cập nhật | Agent bị kẹt hoặc hack |
| Scope vừa đủ | "Sửa feature folder, test file liên quan, không chạm auth/schema" | Review được, vẫn đủ không gian xử lý |

## 5. Definition Of Done

DoD là danh sách điều kiện bắt buộc để task được coi là hoàn tất. DoD không nên là cảm nhận. Nó phải kiểm chứng được.

### DoD Tốt

```markdown
## Definition of Done
- Người dùng upload được file `.wav` hoặc `.mp3` nhỏ hơn 10MB.
- Người dùng record được audio tối thiểu 3 giây từ microphone.
- Audio đã upload/record có thể replay trong UI.
- Mock realtime voice test pass.
- Không có TypeScript error.
- Không có visual overflow ở viewport 390px và 1440px.
```

### DoD Yếu

```markdown
## Definition of Done
- UI đẹp.
- Code clean.
- Feature chạy ổn.
```

DoD yếu không có tiêu chuẩn kiểm chứng. Reviewer không thể biết agent đã xong thật hay chưa.

## 6. Validation Commands

Validation command là lệnh bắt buộc agent hoặc reviewer chạy để chứng minh output đúng. Mỗi command nên có mục đích rõ.

| Loại command | Mục đích | Ví dụ |
|---|---|---|
| Build | Kiểm compile/bundle | `npm run build` |
| Unit test | Kiểm logic nhỏ | `npm test -- audio-upload` |
| Integration test | Kiểm nhiều module | `npm run test:e2e` |
| Lint/typecheck | Kiểm style/type | `npm run lint && npm run typecheck` |
| Benchmark | Kiểm performance | `cargo bench --bench write_path` |
| Visual | Kiểm UI | `npx playwright test visual.spec.ts` |

Nếu không có command sẵn, ghi rõ "phải bổ sung test nào" hoặc "manual verification nào được chấp nhận".

## 7. Evidence

Evidence là thứ làm cho kết quả có thể audit. Không có evidence, reviewer chỉ đang tin lời agent.

| Loại task | Evidence tối thiểu |
|---|---|
| Backend/API | Test output, request/response mẫu, error case |
| Frontend/UI | Screenshot desktop/mobile, console error check, interaction result |
| Performance | Baseline, benchmark sau tối ưu, machine spec, input size |
| ML/audio | Dataset/sample, latency, accuracy/FPR/FNR, export artifact |
| Embedded/IoT | Serial log, GPIO/FFT/audio proof, hardware setup note |
| Security | Threat note, negative tests, dependency/static scan |

Evidence phải đủ để một người không trực tiếp làm task vẫn hiểu vì sao task được pass.

## 8. Template Copy-Ready

````markdown
# Goal: [Tên task ngắn]

## Objective
[Outcome đo được trong một câu. Nêu rõ module, hành vi, metric hoặc gate.]

## Business/Engineering Value
[Vì sao task này đáng làm. Gắn với quality, speed, reliability, UX, cost hoặc risk.]

## Mode
autonomous | assisted | manual-review-required

## Allowed Scope
- `[file/folder được phép sửa]`

## Forbidden Scope
- `[file/folder không được sửa]`
- Không xóa/skip test hiện có nếu chưa được phép.
- Không đổi public API ngoài phạm vi đã mô tả.

## Inputs Available
- Spec:
- Logs:
- Screenshots:
- Dataset/sample:
- Related docs:

## Definition of Done
- [Điều kiện hoàn tất 1, đo được]
- [Điều kiện hoàn tất 2, đo được]
- [Không regression X]

## Validation Commands
```bash
[command build/test/lint/benchmark]
```

## Evidence Required
- Diff summary:
- Test/build output:
- Screenshot/video nếu có UI:
- Benchmark report nếu có performance:
- Known risks hoặc assumptions:

## Escalation Rules
- Dừng và hỏi nếu phải sửa ngoài `Allowed Scope`.
- Dừng và hỏi nếu validation fail quá 2 vòng cùng một lỗi.
- Dừng và hỏi nếu thiếu tài liệu/spec để xác định đúng sai.

## Completion Standard
Task chỉ được coi là hoàn tất khi toàn bộ DoD pass và evidence được ghi lại.
````

## 9. Ví Dụ Áp Dụng

````markdown
# Goal: Fix PDF Export Layout Overflow

## Objective
Sửa lỗi text overflow trong PDF export slide 23 sao cho nội dung không bị cắt ở desktop và mobile preview, được kiểm chứng bằng visual screenshot gate.

## Business/Engineering Value
Đảm bảo tài liệu xuất bản có chất lượng trình bày ổn định, giảm lỗi thủ công trước khi publish.

## Mode
assisted

## Allowed Scope
- `slides/SLIDES.md`
- `src/export/pdf.ts`
- `src/styles/export.css`
- `tests/visual/pdf-export.spec.ts`

## Forbidden Scope
- Không đổi theme toàn cục.
- Không sửa nội dung các slide khác nếu không cần.
- Không skip visual test.

## Inputs Available
- Screenshot lỗi slide 23.
- Existing visual test suite.
- Export command hiện tại.

## Definition of Done
- Slide 23 không có text clipping.
- Desktop 1440px và mobile 390px đều không overflow.
- PDF export chạy thành công.
- Không có regression visual ở 3 slide liền trước và sau slide 23.

## Validation Commands
```bash
npm run build
npm run test:visual -- pdf-export
npm run export:pdf
```

## Evidence Required
- Screenshot trước/sau.
- Test output.
- Đường dẫn file PDF export.
- Ghi chú nếu phải thay đổi layout rule.

## Escalation Rules
- Dừng nếu cần đổi global typography scale.
- Dừng nếu visual regression xuất hiện ngoài slide 20-26.
````

## 10. Rubric Đánh Giá GOAL.md

| Tiêu chí | Điểm tối đa | Mô tả đạt chuẩn |
|---|---:|---|
| Objective | 20 | Cụ thể, đo được, hẹp, gắn kết quả |
| Scope/locked files | 20 | Allowed và forbidden scope rõ |
| DoD | 20 | Điều kiện hoàn tất kiểm chứng được |
| Validation | 15 | Command copy-ready hoặc manual gate rõ |
| Evidence | 15 | Bằng chứng đủ để audit |
| Escalation | 10 | Biết khi nào dừng/hỏi/không tự mở rộng |

Chuẩn pass: từ 70/100. Chuẩn xuất sắc: từ 90/100 và có evidence policy rõ.
