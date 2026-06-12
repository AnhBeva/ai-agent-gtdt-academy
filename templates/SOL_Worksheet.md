# SOL Worksheet - Speed Of Light Optimization

## 1. Bản Chất

SOL trong bối cảnh engineering là giới hạn lý thuyết của hệ thống dựa trên phần cứng và đường dữ liệu. Nó trả lời câu hỏi:

```text
"Nhanh nhất có thể, về mặt vật lý, là bao nhiêu?"
```

Không có SOL, team dễ tối ưu theo cảm giác:

- Dừng quá sớm ở mức "có vẻ nhanh".
- Tối ưu sai tầng vì không biết bottleneck.
- Đòi target không thể đạt vì vượt giới hạn CPU/GPU/memory/network.
- Cho agent loop vô hạn mà không biết gần tới trần hay chưa.

SOL không phải lúc nào cũng cần độ chính xác tuyệt đối. Nó là neo định hướng để biết hệ thống đang cách trần bao xa và nên tối ưu ở đâu.

## 2. Khi Nào Dùng SOL Worksheet

Dùng khi task liên quan:

- Database write/read throughput.
- Inference latency hoặc concurrency.
- Audio/video realtime processing.
- GPU kernel tuning.
- Network relay, streaming, WebRTC.
- Embedded/IoT loop có giới hạn CPU, memory, bus, GPIO, UART, I2S.
- Bất kỳ task nào có yêu cầu "tối ưu đến gần giới hạn".

Không cần SOL chi tiết cho task UI thường, CRUD đơn giản, hoặc bug fix không liên quan performance.

## 3. Ba Loại Bound Chính

| Bound | Bản chất | Metric thường dùng | Ví dụ |
|---|---|---|---|
| Compute-bound | Nghẽn ở năng lực tính toán CPU/GPU | FLOPs, ops/s, CPU%, GPU utilization | Matrix multiply, DSP, ML inference |
| I/O-bound | Nghẽn ở đọc/ghi memory/disk/bus | GB/s, IOPS, cache miss, disk latency | Database, mmap, file processing |
| Network-bound | Nghẽn ở RTT, bandwidth, packet processing | Mbps/Gbps, p95 latency, packets/s | WebRTC, relay, TCP stream |

Một hệ thống có thể có nhiều bound ở các pha khác nhau. Ví dụ VAD audio pipeline có thể I/O-bound ở decode, compute-bound ở inference, network-bound ở stream.

## 4. Phương Pháp Xác Định Bottleneck

### Bước 1. Đo baseline

Ghi lại hiện trạng trước khi tối ưu.

| Mục | Cần ghi |
|---|---|
| Commit/version | |
| Machine spec | CPU/GPU/RAM/disk/network |
| Input workload | Size, duration, concurrency |
| Metric chính | latency, throughput, memory, CPU/GPU |
| Command | benchmark command |
| Kết quả | số liệu thô |

### Bước 2. Quan sát tài nguyên

| Dấu hiệu | Khả năng bottleneck |
|---|---|
| CPU 95-100%, memory bandwidth thấp | Compute-bound CPU |
| GPU utilization cao, CPU thấp | Compute-bound GPU |
| CPU thấp nhưng disk/memory wait cao | I/O-bound |
| Latency tăng theo RTT/bandwidth | Network-bound |
| Lock contention spike | Concurrency/synchronization bottleneck |
| GC/memory growth | Memory allocation/leak bottleneck |

### Bước 3. Ước lượng trần lý thuyết

Không cần công thức phức tạp ngay từ đầu. Bắt đầu bằng phép chia đơn giản:

```text
theoretical_max = hardware_capacity / work_per_unit
```

Ví dụ:

- Nếu mỗi request cần 10MB memory scan, memory bandwidth 50GB/s, trần I/O lý thuyết khoảng 5.000 request/s trước overhead.
- Nếu mỗi inference cần 2 GFLOPs, GPU có 10 TFLOPs, trần compute lý thuyết khoảng 5.000 inference/s trước overhead.
- Nếu mỗi audio stream cần 64kbps, network 1Gbps, trần bandwidth lý thuyết khoảng 15.625 stream trước overhead.

### Bước 4. Tính gap

```text
SOL efficiency = current_performance / theoretical_max
```

| Efficiency | Diễn giải |
|---|---|
| <10% | Có thể đang sai kiến trúc, overhead lớn, chưa optimize |
| 10-40% | Còn nhiều dư địa, cần profiling |
| 40-70% | Tối ưu đã có hiệu quả, cần tìm bottleneck cụ thể |
| 70-90% | Gần trần thực tế, tối ưu tiếp khó hơn |
| >90% | Có thể đã gần giới hạn hoặc estimate quá thấp |

## 5. Current Performance

Current performance phải được đo bằng workload đại diện, không phải demo nhỏ.

| Nhóm metric | Ví dụ |
|---|---|
| Latency | p50, p95, p99, max |
| Throughput | requests/s, writes/s, generations/s, channels |
| Stability | duration, crash count, memory leak |
| Resource | CPU%, GPU%, RAM, memory bandwidth, disk I/O |
| Correctness | accuracy, error rate, false positive/negative |

Với performance task, correctness luôn đứng trước speed. Tối ưu làm sai kết quả không được tính là thành công.

## 6. Optimization Target

Target tốt phải có 3 lớp:

| Lớp | Nội dung | Ví dụ |
|---|---|---|
| Minimum acceptable | Mức đủ để business chấp nhận | p95 < 100ms |
| Target | Mức khóa học/task hướng tới | p95 < 30ms |
| SOL ambition | Mức gần giới hạn vật lý | >=70% theoretical throughput |

Không phải task nào cũng cần đạt 90% SOL. Với hệ thống production, cân bằng maintainability, cost và correctness quan trọng hơn tối ưu cực hạn.

## 7. SOL Worksheet Template

```markdown
# SOL Worksheet

## System/Task
- Task:
- Owner:
- Date:
- Commit/version:

## Workload Definition
- Input size:
- Concurrency:
- Duration:
- Dataset/sample:
- Environment:

## Baseline
| Metric | Value | Evidence |
|---|---:|---|
| p50 latency | | |
| p95 latency | | |
| Throughput | | |
| CPU usage | | |
| GPU usage | | |
| Memory usage | | |
| Error/correctness | | |

## Bound Analysis
| Bound type | Hardware capacity | Work per unit | Theoretical max | Confidence |
|---|---:|---:|---:|---|
| Compute | | | | low/medium/high |
| I/O | | | | low/medium/high |
| Network | | | | low/medium/high |

## Bottleneck Hypothesis
- Primary bottleneck:
- Evidence:
- Alternative bottleneck:
- What to profile next:

## Optimization Plan
| Step | Hypothesis | Change | Expected impact | Validation |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

## After Optimization
| Metric | Baseline | After | Delta | Target |
|---|---:|---:|---:|---:|
| p95 latency | | | | |
| Throughput | | | | |
| CPU/GPU usage | | | | |
| Correctness | | | | |

## Decision
- Continue optimizing | stop | redesign | escalate
- Reason:
- Residual risk:
```

## 8. Ví Dụ: VAD Realtime <30ms

| Mục | Giá trị mẫu |
|---|---|
| Task | Optimize Vietnamese VAD inference |
| Workload | 16kHz mono audio, 30ms frame, noisy environment |
| Minimum acceptable | p95 latency <50ms, FPR không tăng |
| Target | p95 latency <30ms |
| Bound nghi ngờ | Compute-bound ở feature extraction/inference |
| Evidence cần | Dataset, latency histogram, accuracy/FPR/FNR |
| Gate | Correctness test -> ONNX export -> benchmark |

Ví dụ decision:

```text
Nếu CPU p95 vẫn >30ms và profiler cho thấy feature extraction chiếm >60%, thử CUDA/SIMD hoặc precompute window. Nếu FPR tăng, rollback optimization dù latency đạt.
```

## 9. Ví Dụ: IoT Database Write-Heavy

| Mục | Giá trị mẫu |
|---|---|
| Task | Optimize append-only IoT database |
| Workload | 1M device writes/hour, rare reads |
| Bound nghi ngờ | I/O-bound + lock contention |
| Baseline evidence | write latency spike, CPU profile, lock contention |
| Optimization | mmap hot buffer, append-only layout, fine-grained RwLock |
| Gate | 25h stability run, memory leak check, write latency p95 |

## 10. Sai Lầm Thường Gặp

- Không có baseline trước khi tối ưu.
- Đo benchmark bằng input quá nhỏ.
- Chỉ đo average latency, bỏ qua p95/p99.
- Không ghi machine spec.
- Không kiểm correctness sau tối ưu.
- Tưởng CPU cao luôn là compute-bound, trong khi có thể là lock contention.
- Chưa biết trần lý thuyết nhưng yêu cầu target phi thực tế.

## 11. Tiêu Chuẩn Worksheet Đạt

Worksheet đạt chuẩn khi:

- Workload đại diện thực tế.
- Có baseline và evidence.
- Có bound analysis compute/I/O/network.
- Có bottleneck hypothesis rõ.
- Có target tối thiểu và target kỳ vọng.
- Có comparison before/after.
- Có decision tiếp tục/dừng/redesign/escalate.
