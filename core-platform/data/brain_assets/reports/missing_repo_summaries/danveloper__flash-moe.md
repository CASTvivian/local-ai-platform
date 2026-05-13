# Missing Repo Summary Source: danveloper/flash-moe

- URL: https://github.com/danveloper/flash-moe
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/danveloper__flash-moe
- Clone Status: cloned
- Language: Objective-C
- Stars: 3844
- Topics: 
- Description: Running a big model on a small laptop

## Extracted README / Docs / Examples



# FILE: README.md

# Flash-MoE: Running a 397B Parameter Model on a Laptop

> **[Read the paper](paper/flash_moe.pdf)** — Full technical details, 90+ experiments, and the story of how an AI and a human built this in 24 hours.

Pure C/Metal inference engine that runs **Qwen3.5-397B-A17B** (a 397 billion parameter Mixture-of-Experts model) on a MacBook Pro with 48GB RAM at **4.4+ tokens/second** with production-quality output including tool calling.

The entire 209GB model streams from SSD through a custom Metal compute pipeline. No Python. No frameworks. Just C, Objective-C, and hand-tuned Metal shaders.

## Results

![Progress](progress.png)

| Configuration | tok/s | Quality | Notes |
|--------------|-------|---------|-------|
| 4-bit experts, FMA kernel | **4.36** | Excellent | Current best. Full tool calling. 209GB on disk. |
| 4-bit experts, baseline | 3.90 | Excellent | Before FMA kernel optimization. |
| 2-bit experts, trust OS | 5.74 | Good* | 120GB on disk. *Breaks JSON/tool calling. |
| 2-bit peak single token | 7.05 | Good* | Warm cache burst. *Not suitable for tool use. |

*2-bit quantization produces `\name\` instead of `"name"` in JSON output, making tool calling unreliable. 4-bit is the production configuration.

## Hardware

- **Machine**: MacBook Pro, Apple M3 Max
- **Chip**: 16-core CPU (12P + 4E), 40-core GPU, 16-core ANE
- **Memory**: 48 GB unified (~400 GB/s bandwidth)
- **SSD**: 1TB Apple Fabric, **17.5 GB/s sequential read** (measured)
- **macOS**: 26.2 (Darwin 25.2.0)

## Architecture

The model has 60 transformer layers: 45 GatedDeltaNet (linear attention) + 15 standard full attention. Each layer has 512 experts, of which K=4 are activated per token (plus one shared expert). Hidden dimension is 4096.

### Key Techniques

1. **SSD Expert Streaming** — Expert weights (209GB at 4-bit) are read from NVMe SSD on demand via parallel `pread()` with GCD dispatch groups. Only the K=4 active experts per layer are loaded (~6.75MB each). The OS page cache manages caching — no custom cache needed ("Trust the OS" principle). Inspired by Apple's "LLM in a Flash" paper.

2. **FMA-Optimized Dequant Kernel** — The inner loop of the 4-bit dequantized matrix-vector multiply rearranges the math from `(nibble * scale + bias) * x` to `fma(nibble, scale*x, bias*x)`. Pre-computing `scale*x` and `bias*x` lets the GPU fused multiply-add unit do dequant+multiply in one instruction. 12% faster than the naive formulation.

3. **Metal Compute Shaders** — Hand-written Metal kernels for:
   - 4-bit and 2-bit dequantized matrix-vector multiply (tiled, SIMD-reduced, shared input cache, FMA-optimized)
   - Fused SwiGLU activation
   - RMS normalization (two-pass: sum-of-squares reduction + apply)
   - Batched GPU attention (Q@K^T, softmax, scores@V) for full attention layers
   - GPU RoPE (fused with Q deinterleave and K normalization)
   - MoE combine + residual + sigmoid gate (fused kernel)

4. **Deferred GPU Expert Compute** — CMD3 (expert forward pass) is submitted without waiting. The GPU executes it while the CPU prepares the next layer. The combine + residual + norm are also on GPU, feeding directly into the next layer's attention projections.

5. **Accelerate BLAS for Linear Attention** — The GatedDeltaNet recurrence uses `cblas_sscal`, `cblas_sgemv`, and `cblas_sger` for the 64-head × 128×128 state matrix update. 64% faster than scalar code.

6. **Trust the OS** — No custom expert cache. The OS page cache (~35GB) manages expert data caching via standard LRU. Every custom caching approach we tested (Metal LRU, malloc cache, LZ4 compressed cache) was slower due to GPU memory pressure or overhead. The page cache achieves ~71% hit rate naturally.

### Pipeline Per Layer (4.28ms average at 4-bit)

```
CMD3(prev) → CMD1: attention projections + delta-net  [1.22ms GPU]
           → CPU: flush results                       [0.01ms CPU]
           → CMD2: o_proj + norm + routing + shared    [0.55ms GPU]
           → CPU: softmax + topK routing               [0.003ms]
           → I/O: parallel pread K=4 experts           [2.41ms SSD]
           → CMD3: expert forward + combine + norm     [0.04ms encode, DEFERRED]
```

### Unified Memory Constraint

On Apple Silicon, SSD DMA and GPU compute share the same memory controller and cannot be profitably overlapped. The GPU's dequant kernels are bandwidth-saturated at ~418 GiB/s. Even small background SSD DMA causes disproportionate GPU latency spikes through memory controller arbitration. The serial pipeline (GPU → SSD → GPU) is hardware-optimal.

## Quick Start

```bash
cd metal_infer
make
# 4-bit inference (needs packed_experts/ directory)
./infer --prompt "Explain quantum computing" --tokens 100

# 2-bit inference (faster but breaks tool calling)
./infer --prompt "Explain quantum computing" --tokens 100 --2bit

# Interactive chat with tool calling
./chat

# Per-layer timing breakdown
./infer --prompt "Hello" --tokens 20 --timing
```

## Project Structure

```
metal_infer/
  infer.m              # Complete inference engine (~7000 lines)
  shaders.metal        # Metal compute kernels (~1200 lines)
  chat.m               # Interactive chat TUI with tool calling
  tokenizer.h          # C BPE tokenizer (single-header, 449 lines)
  main.m               # MoE-only benchmark
  Makefile             # Build system
  extract_weights.py   # Creates model_weights.bin from safetensors
  repack_experts_2bit.py  # 4-bit → 2-bit expert requantization
  train_predictor.py   # Expert routing prediction analysis
  model_weights.bin    # Non-expert weights (5.5GB, mmap'd)
  model_weights.json   # Tensor manifest
  vocab.bin            # Vocabulary for token decoding
  tokenizer.bin        # Pre-exported BPE tokenizer data

repack_experts.py      # 4-bit expert packing from safetensors
progress.py            # Results visualization (Q2/Q4 tracks)
results.tsv            # Experiment log (58 experiments)
```

## What We Tried (and What Worked)

### Kept
| Approach | Result | Impact |
|----------|--------|--------|
| FMA dequant kernel | GPU compute -12% | **+12% tok/s** |
| Trust OS page cache | Deleted Metal LRU → +38% | **Foundational** |
| GPU combine+norm in CMD3 | Eliminates CPU round-trip | **Pipeline** |
| BLAS delta-net (Accelerate) | cpu_attn 0.78→0.28ms | **+64% attn** |
| F_NOCACHE for 2-bit | +3% from avoiding page thrash | **2-bit only** |
| GPU fused attention (RoPE) | +2% for full-attn layers | **Small** |
| C BPE tokenizer | 180ms vs 3500ms startup | **20x startup** |
| Deferred CMD3 execution | GPU/CPU overlap | **Pipeline** |

### Discarded (58 experiments, highlights)
| Approach | Result | Why |
|----------|--------|-----|
| LZ4 expert compression | -13% | Decompress overhead > warm cache savings |
| F_RDADVISE prefetch | net 0% | Unified memory: SSD DMA slows GPU -73% |
| Temporal expert prediction | -18% | 25% hit rate, SSD bandwidth waste |
| MLP routing predictor | 31% accuracy | Worse than temporal baseline |
| GPU LUT dequant kernel | -2% | Indirect register access serializes |
| GPU private buffer compression | -20% pipeline | Blit cost 4×7MB > matvec savings |
| Spin-poll GPU wait | -23% | CPU thermal competes with GPU |
| Expert file clustering | 0% | NVMe ignores scatter at 7MB granularity |
| dispatch_io | -70% | dispatch_data management overhead |
| mmap expert files | -5x | Per-page fault overhead on cold data |
| Speculative early routing | -38% | Cache pollution + overhead |
| MTP speculative decoding | break-even | MoE I/O scales per-token (unlike dense) |

## Safety

This is a primary development machine. The engine explicitly controls memory:
- Non-expert weights: 5.5GB (mmap'd, read-only)
- Metal scratch buffers: ~200MB
- Total: ~6GB, leaving 42GB for OS + page cache
- No OOM risk. Expert data streams from SSD on demand.
- No custom caches. Trust the OS.


# FILE: docs/plan-async-pread-pipeline.md

# Plan: Cross-Layer Async Pread Pipeline

## Status
- Async pread mechanism implemented and working (async_pread_start/wait in infer.m)
- Within-layer overlap tested: no improvement (only 0.1ms overlap window)
- Need: CROSS-LAYER overlap for ~2ms of pread hiding

## Current Per-Layer Sequence (4.5ms total)
```
[deferred_wait] → [CMD1 submit+wait] → [CPU attn] → [CMD2 submit+wait] → [routing] → [SYNC pread] → [CMD3 submit]
     0.87ms           0.5ms              0.27ms          0.45ms           0.003ms      2.43ms          0.03ms
```

## Target Sequence
```
Layer N:  ... → [routing] → [START async pread into BUF_A] → [CMD3 submit (using BUF_B from prev)]
Layer N+1: [deferred_wait] → [CMD1] → [CPU attn] → [CMD2] → [routing] → [WAIT async pread BUF_A] → [CMD3 submit (using BUF_A)]
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                              ~2.1ms of compute overlapping with N's pread
```

Pread for layer N runs during layer N+1's compute. By the time N+1 needs expert data, N's pread has had 2.1ms of head start.

## Implementation Steps

### 1. Double-Buffer Expert Data
Already have: `buf_multi_expert_data[MAX_K]` (set A) and `buf_multi_expert_data_B[MAX_K]` (set B).

Add a flip flag:
```c
static int g_expert_buf_flip = 0;  // 0 = use set A for current, 1 = use set B
```

Each layer alternates which buffer set it writes pread data INTO vs which set CMD3 reads FROM.

### 2. Restructure fused_layer_forward

**At layer start (after deferred_wait):**
- If async pread is in flight from previous layer: DON'T wait yet
- Continue with CMD1, CPU attn, CMD2, routing

**After routing:**
- NOW wait for the previous layer's async pread (it's had ~2ms to complete)
- Start THIS layer's async pread into the OTHER buffer set
- Encode CMD3 using the COMPLETED buffer set (from previous layer's pread)

Wait — this doesn't work because CMD3 needs THIS layer's expert data, not the previous layer's. Let me rethink.

### Correct Design

The pread for layer N needs to complete before layer N's CMD3 encodes. But we want pread for N to overlap with layer N's CMD1+attn+CMD2 (which don't use expert data).

**Revised flow:**
```
Layer N start:
  1. Wait for N-1's deferred CMD3 (or GPU combine)
  2. Submit CMD1 (attention projections)
  3. [BACKGROUND: start async pread for layer N's experts]
     - But we don't know N's experts yet! Routing hasn't happened.
```

This is the fundamental problem: we can't start pread until after routing, but routing is the LAST thing before pread in the pipeline.

### The Real Solution: Decouple Routing from Expert Loading

Split CMD2 into two parts:
- CMD2a: o_proj + residual + norm (produces h_post for routing)
- CMD2b: routing gate_proj (produces gate_scores)

Then:
```
Layer N:
  CMD1 → CPU attn → CMD2a+CMD2b → wait → routing topK → [START async pread] → CMD3 (deferred)
Layer N+1:
  [async pread from N still running]
  deferred_wait → CMD1 → CPU attn → CMD2a+CMD2b → wait → routing topK
  [NOW wait for N's async pread — it's had the entire N+1 compute time]
  → CMD3 using N+1's expert data that we NOW start loading synchronously
```

Hmm, this still doesn't help because we need N+1's experts, not N's.

### Actually Correct Solution: Pipeline Expert Data One Layer Ahead

The insight: at the end of layer N, we have N's expert data loaded. We submit CMD3 (deferred) which uses that data. CMD3 runs on GPU while we start layer N+1.

If we started loading N+1's experts AT THE SAME TIME as submitting N's CMD3:
```
Layer N end:  [submit CMD3_N using BUF_A] + [start async pread for N+1 into BUF_B]
Layer N+1:    [deferred_wait N] → [CMD1] → [attn] → [CMD2] → [routing]
              [async pread N+1 completes during this time]
              → [check: do loaded experts match routing? if yes, use BUF_B; if no, sync pread]
```

But we DON'T KNOW layer N+1's experts at the end of layer N. We'd need to PREDICT them.

Previous prediction attempts failed (53% accuracy, overhead > benefit).

### ALTERNATIVE: Overlap pread with CMD3 GPU execution

Currently CMD3 is deferred — GPU runs it while we start the next layer. But we DON'T start loading the next layer's experts during CMD3. What if we did?

After CMD3 submit for layer N:
```
[submit CMD3_N] → [start next layer's CMD1+attn+CMD2] → [routing N+1] → [pread N+1]
                  ↑ CMD3_N runs on GPU here, overlapping with N+1's compute
```

The pread for N+1 currently starts AFTER routing for N+1, which is after CMD2 for N+1, which is after deferred_wait for CMD3_N. So the pread can't start until CMD3_N is done.

But with GPU combine+norm in CMD3, we eliminated the deferred_wait. CMD1 for N+1 submits immediately after CMD3_N. The GPU executes CMD3_N → CMD1_N+1 back-to-back. The CPU is free during this time to do... nothing useful, because it's waiting for CMD1_N+1 to complete.

### THE REAL REAL SOLUTION: Start pread during CMD1 wait

CMD1_wait takes 0.87ms (includes CMD3_prev + CMD1 GPU time). During that 0.87ms, the CPU is IDLE waiting for GPU. What if the CPU started the pread during that wait?

But we don't have the routing results yet — routing happens after CMD2.

UNLESS we use the PREVIOUS TOKEN's routing for the same layer as a prediction. This is temporal locality — 20-35% overlap between tokens at the same layer.

We already have the prediction infrastructure (`g_prefetch_experts`). The issue was that F_RDADVISE predictions wasted SSD bandwidth. But what about LOADING into actual buffers?

```
Layer N, token T:
  [CMD1 submit] → [while waiting: pread PREDICTED experts into BUF_B based on token T-1]
  → [CMD1 wait returns] → [CPU attn] → [CMD2] → [routing]
  → [check predictions: how many of K=4 match?]
  → [pread only the MISSES into BUF_A (typically 2-3 instead of 4)]
  → [CMD3 using mix of BUF_A (misses) and BUF_B (hits)]
```

With 30% hit rate: 1.2 of 4 experts are pre-loaded. Saves ~30% of pread time.
With 50% hit rate: 2 of 4 pre-loaded. Saves ~50%.

The difference from before: we're not pollu

# FILE: docs/optimization-experiments-q4.md

# Q4 Expert Optimization Experiments

## Context

After discovering that 2-bit expert quantization broke tool calling (JSON quotes → backslashes), we reverted to 4-bit experts. This dropped performance from 5.74 tok/s (2-bit) to 3.50 tok/s (4-bit). The goal: recover as much speed as possible while maintaining 4-bit quality.

The 4-bit experts are 7,077,888 bytes each (6.75 MB). With K=4 active experts per layer and 60 layers, each token reads 240 experts = 1.68 GB from SSD.

## Baseline Pipeline (4-bit, K=4, trust OS page cache)

```
Per layer (4.28 ms avg):
  cmd1_wait:    1.22 ms  (28%)  GPU: CMD3(prev) + CMD1 attention projections
  cmd2_wait:    0.55 ms  (13%)  GPU: o_proj + norm + routing + shared expert
  expert_io:    2.41 ms  (56%)  SSD: 4×7MB parallel pread
  CPU work:     0.10 ms  ( 2%)  encode + attention + routing + memcpy

60 layers × 4.28 ms = 257 ms per token = 3.90 tok/s
```

Page cache hit rate: ~71% (35 GB cache, 209 GB model).
Warm cache parallel pread: 1.0 ms. Cold SSD: 5.8 ms. Mixed: 2.4 ms.

## Experiment Results

### Kept: FMA Dequant Kernel (+2.6% → 4.36 tok/s)

Rearranged the inner loop of `dequant_matvec_4bit_v3` from:
```metal
acc += (float(nibble) * scale + bias) * x;
```
to:
```metal
float sx = scale * x, bx = bias * x;
acc += fma(float(nibble), sx, bx);
```

Pre-computing `scale*x` and `bias*x` per input element allows the GPU to use the fused multiply-add unit for the dequant+multiply in one instruction. Reduces per-nibble cost from (convert + mul + add + mul + add) to (convert + fma + add).

Impact: cmd1_wait -5.4%, cmd2_wait -10.7%. Total: 3.90 → 4.36 tok/s.

### Discarded: LZ4 Expert Compression (-13%)

Repacked 209 GB of expert files to 175 GB with LZ4 compression. Apple's LZ4 decompressor runs at 41 GB/s (NEON hardware-accelerated), making decompression only 0.17 ms per expert.

Results:
- Isolated cold reads: 15-24% faster (less data from SSD)
- Isolated decompression: 0.17 ms at 41 GB/s (essentially free)
- **Full pipeline: 3.55 tok/s (-13%)** — the 0.68 ms/layer decompress cost exceeds the warm cache I/O savings. The OS page cache is efficient enough that most reads are warm.

Also tested LZFSE (2.6 GB/s, too slow), APFS transparent compression (kernel serializes read+decompress, 2× slower), and per-expert files (15% slower from VFS metadata overhead).

Key finding: Apple's M3 Max SSD is so fast that CPU-based decompression can't keep up for warm cache reads. LZ4 only wins for cold reads, but the page cache handles most reads.

### Discarded: Expert Routing Prediction (-18%)

Built a temporal prediction system: store previous token's expert routing per layer, prefetch those experts into double-buffered Metal buffers during the next token's CMD1 wait.

Results:
- Temporal hit rate: 25.6% (only 1 of 4 experts matches between tokens)
- The 75% misses waste SSD bandwidth and require sync pread after the prediction wait
- With K=4 parallel reads, wall time = max(4 reads). Need ALL 4 to hit for improvement.
- P(all 4 hit) at 25% = 0.25⁴ = 0.4%. Practically zero.

Also trained an MLP predictor (31% accuracy from pre-attention hidden state — worse than temporal baseline). The gate_proj "logit lens" approach achieves 53% from pre-attention state, but the K=4 exponential penalty still kills it.

### Discarded: F_RDADVISE Prefetch (net 0%)

Sent F_RDADVISE kernel hints between CMD1 commit and wait to prefetch next token's predicted experts during GPU compute.

Results:
- expert_io: -31% (page cache warming works!)
- cmd2_wait: +73% (GPU memory bandwidth contention from SSD DMA)
- **Net: 0% across 5 diverse prompts**

Root cause: Apple Silicon unified memory architecture. SSD DMA and GPU matvec share the same memory controller. The GPU's dequant kernels are bandwidth-saturated at 418 GiB/s. Even 17.5 GB/s of background DMA (~4%) causes disproportionate latency spikes through memory controller arbitration. This is architectural — cannot be worked around in software.

### Discarded: GPU Kernel Variants

- **LUT dequant (v5)**: Pre-compute 16-entry lookup table per group to eliminate uint→float conversions. -2% because GPU indirect register access serializes.
- **Vector load (v4)**: uint4 loads for coalesced memory access. -3% from register pressure.
- **extract_bits intrinsic**: Neutral — compiler already generates the same instruction.
- **Spin-poll GPU wait**: -23%. CPU spinning steals thermal budget from GPU on unified architecture.
- **addCompletedHandler**: Neutral in practice — isolated 20% win on micro-benchmark but real workloads have enough GPU compute to hide the wait overhead.

### Discarded: I/O Path Alternatives

- **dispatch_io**: -70%. Apple's GCD I/O framework adds dispatch_data management overhead (allocate, map, memcpy) that far exceeds any kernel scheduling benefit.
- **aio_read**: -7% (matches GCD group + pread, which we already use).
- **Expert file clustering**: 0%. NVMe doesn't care about scatter distance at 7MB read granularity. 4 reads spanning 21 MB vs 2.9 GB take the same time.
- **GPU private buffer compression**: Isolated -13.5% per matvec (GPU hardware memory compression on StorageModePrivate). But in pipeline: blitting 4×7MB shared→private costs more than the matvec savings. -20% overall.

### Analyzed but not implemented: MTP Speculative Decoding

Qwen 3.5 ships with an MTP (Multi-Token Prediction) head — a single MoE transformer layer that predicts the next-next token. The head exists in the model config (`mtp_num_hidden_layers: 1`) but weights were stripped from the MLX quantization.

Analysis showed MTP speculative decoding doesn't help for MoE with SSD streaming: each speculated token requires its OWN expert routing and I/O. Batched verification of 2 tokens costs ~1.75× expert I/O for 1.7 tokens (70% acceptance). Break-even at best.

This contrasts with dense models where verification cost is constant regardless of batch size (same weights for every token).

## The Unified Memory Constraint

The single most important finding: *

# FILE: docs/plan-io-experiments.md

# Plan: I/O Optimization Experiments

## Baseline Reference
- Per-layer: 4.28ms total, 2.41ms expert_io (56%)
- Expert read: 4 × 7MB parallel pread from 3.4GB file
- Measured: 5.8ms cold parallel, 1.0ms warm parallel, 2.4ms mixed (71% cache hit)
- Theoretical floor: 28MB / 17.5 GB/s = 1.6ms
- Gap: 0.8ms overhead per layer (kernel VFS + page cache + NVMe scheduling)

---

## Experiment 1: dispatch_io vs pread

### Isolated test
Read 4 experts (7MB each) from a layer file using:
- (A) 4 × pread on 4 pthreads (current approach)
- (B) 4 × dispatch_io_read on a DISPATCH_IO_RANDOM channel
- Both with F_NOCACHE to force SSD reads. Both with warm cache. 50 iterations each.

Measure: wall time, throughput (GB/s logical).

### What dispatch_io does differently
- Creates a kernel-side I/O channel with optimized scheduling
- The kernel sees all reads as part of one channel → can reorder NVMe commands by LBA
- Automatic cleanup handlers (no thread join overhead)
- May use a different VFS code path optimized for random access

### Pipeline contention analysis
- dispatch_io is async with completion blocks on GCD queues
- The completion block runs on a GCD thread (same as our async_pread)
- Memory path: SSD → DMA → DRAM → Metal shared buffer (same as pread)
- **No new contention** — same memory path as current approach
- Risk: dispatch_io might add GCD overhead that exceeds VFS savings
- Risk: completion blocks might have higher latency than pthread wakeup

### Expected impact
- Best case: 10-20% expert_io reduction (eliminates per-syscall VFS overhead)
- Worst case: neutral or slight regression (GCD completion overhead)
- Pipeline impact: drop-in replacement for pread, no GPU interaction

---

## Experiment 2: GPU private buffer compression

### Isolated test
- (A) GPU matvec reading from StorageModeShared buffer (current)
- (B) GPU blit shared→private, then matvec reading from StorageModePrivate buffer
- Use same expert weight data, same kernel, same dimensions
- Measure: blit time, matvec time, total. 100 iterations.

### What GPU compression does
- StorageModePrivate buffers live in GPU-managed memory
- The GPU's memory controller can apply lossless compression (similar to console GPU
  texture compression — transparent to shaders)
- For compressible data: effective bandwidth doubles (read 64B, decompress to 128B)
- 4-bit quantized weights with 2.4-3.7 bits entropy → highly compressible
- The shader code doesn't change at all — compression is hardware-transparent

### Pipeline contention analysis
- Blit (shared→private) runs on the GPU command queue
- It would go BEFORE the matvec dispatches in CMD3
- Timeline: [pread→shared buf] → [GPU blit 0.02ms] → [GPU matvec from private]
- The blit adds ~0.02ms per expert to CMD3
- But the matvec might be 30-50% faster from doubled bandwidth
- **Key contention**: the blit and matvec are both on the same GPU queue (serial)
  The blit cannot overlap with the matvec. It's purely: does the bandwidth gain
  from compression exceed the blit cost?
- **Memory**: private buffers use GPU-managed memory. 4 × 7MB = 28MB of private
  memory per layer. The GPU manages this pool — may cause memory pressure if the
  pool grows. Need to reuse/recycle the private buffers each layer.

### Expected impact
- Best case: 15-30% cmd1_wait reduction (CMD3 expert matvec faster)
- Worst case: slight regression (blit cost exceeds compression benefit)
- Pipeline impact: affects GPU phases only, no SSD interaction

---

## Experiment 3: Expert file clustering by co-occurrence

### Isolated test
- Run 500 tokens with --freq, collect per-layer expert co-occurrence matrix
- For each layer: cluster the 512 experts so frequently co-occurring experts are adjacent
- Repack each layer file with the new ordering (+ save the permutation map)
- Measure: 4-expert parallel pread with original vs clustered ordering
- Use same expert indices (mapped through permutation), F_NOCACHE, 50 iterations

### What clustering does
- NVMe SSDs read in pages (4KB-16KB). When we read expert 37 (7MB at offset 262MB),
  the SSD reads pages 262.0-269.0 MB. Expert 38 is at 269-276 MB — adjacent.
- If the routing selects experts {37, 42, 100, 205}, those are at offsets
  {262, 297, 708, 1451} MB — widely scattered
- If we reorder so co-occurring experts are adjacent: {37, 42, 100, 205} might become
  physical positions {0, 1, 2, 3} — a 28MB sequential read instead of 4 scattered reads
- Sequential 28MB at 17.5 GB/s = 1.6ms vs scattered 4×7MB at ~5.8ms

### Pipeline contention analysis
- This changes the FILE LAYOUT only — the inference code reads the same way
- Expert indices get mapped through a permutation table (one array lookup, ~0ns)
- **No contention** — purely changes which bytes are at which file offsets
- The only risk: co-occurrence patterns change with different prompts.
  If the clustering is prompt-dependent, it might help some prompts and hurt others.
- Mitigation: use a diverse set of prompts for profiling

### Expected impact
- Best case: 30-50% expert_io reduction for cold reads (scattered → near-sequential)
- Worst case: neutral (if co-occurrence is too flat/prompt-dependent)
- Pipeline impact: pure I/O improvement, no GPU/CPU interaction

---

## Experiment 4: LZ4 DRAM expert cache

### Isolated test
- Allocate 4GB of malloc'd memory
- After each expert pread, LZ4-compress and store in the cache (hash by layer+expert_id)
- On subsequent reads: check cache first. Hit = LZ4 decompress from DRAM.
- Measure: cache hit rate over 200 tokens, avg expert read time (hit vs miss)

### What this does
- Creates a second-level cache between the OS page cache and SSD
- Stores experts in compressed form → 4GB holds ~730 experts (vs ~570 raw)
- Cache hit: decompress at 41 GB/s = 0.17ms per expert
- Cache miss: pread from SSD/page cache = 0.3-1.5ms per expert
- The cache is in USERSPACE memory — doesn't interfere with OS page cache

### Pipeline contention analysis
- Cache lookup: hash table check (~0.001ms) — negligibl

# FILE: docs/io-and-gpu-exploration.md

# I/O and GPU Exploration: What We Learned Running a 397B Model from SSD

## The Problem

We're streaming a 397 billion parameter Mixture-of-Experts model from NVMe SSD on a MacBook Pro with 48GB RAM. The model's expert weights total 120GB at 2-bit quantization (209GB at 4-bit). Only 6GB fits in memory. Every generated token requires reading ~600MB of expert data from disk — 4 experts × 3.9MB × 60 layers.

The question that drove months of optimization: **where does the time actually go, and what can we do about it?**

## Part 1: The GPU Story

### What the profiler showed us

We captured a Metal GPU trace of the expert forward pass (the most compute-intensive per-token operation). The results were surprising:

- **Total GPU compute time for 20 expert matvecs: 747µs** (37µs each)
- **Wall clock time: 31.5ms** (1.58ms each)
- **GPU utilization: 2.4%**

The GPU finishes its actual math in microseconds, then sits idle waiting for the next batch of data. The "compute" bottleneck is really a **data delivery** bottleneck.

### Where GPU cycles go

The instruction cost breakdown from Metal's performance counters:

| Category | % of GPU Time | What it is |
|----------|:---:|---|
| Math (FMA/MUL/ADD) | 63.9% | The actual dequant + multiply-accumulate |
| Conversion | 25.0% | `bf16_to_f32()` calls for scale/bias lookup |
| Data Movement | 3.3% | Moving data between register files |
| Bit Manipulation | 19.0% | Extracting 2-bit values from uint32 |

**25% of GPU time is type conversion.** Every scale and bias value is stored as bfloat16 and converted to float32 on the fly. Storing them as float32 would double the scale/bias storage (negligible overall) but eliminate a quarter of the GPU work.

**19% is bit manipulation.** Extracting 16 × 2-bit values from each uint32 requires shift-and-mask operations. A lookup table or wider SIMD approach could reduce this.

But here's the kicker: even if we eliminated ALL of this overhead, saving 44% of GPU time would save 44% of 37µs = 16µs per matvec. At 720 matvecs per token (4 experts × 3 projections × 60 layers), that's 11.5ms per token. Not nothing — but the I/O bottleneck at 90ms/token makes it a secondary concern.

### Cache behavior

- **L1 Cache Read Hit Rate: 93.4%** — our threadgroup shared memory (`x_shared[4096]`) works perfectly for caching the input vector
- **L1 Cache Write Hit Rate: 100%** — all output writes hit L1
- **Last Level Cache Bandwidth: ~418 GB/s** — nearly saturating unified memory bandwidth

The GPU cache hierarchy is working well. The 6.6% L1 read miss rate corresponds to expert weight data that doesn't fit in L1 (each expert is 3.9MB, L1 is ~192KB per core). These misses go to the shared L2 / memory fabric, which runs at near-theoretical bandwidth.

### The GPU cluster affinity experiment

Apple's M3 Max has 40 GPU cores organized into clusters, each with its own L2 cache (~4MB). Our 2-bit experts are 3.9MB — almost exactly one cluster's L2 capacity.

**Hypothesis:** If we encode all 4 operations for one expert (gate → up → SwiGLU → down) into a single Metal command encoder, the GPU scheduler would keep that work on one cluster, and the expert's weight data would stay hot in that cluster's L2.

**Result:** 2% slower. The fused single-encoder approach reduced parallelism — Metal's scheduler couldn't overlap work across experts anymore. The existing 2-encoder-per-expert approach (gate+up together, SwiGLU+down together) lets the GPU interleave expert computations across clusters, which provides better throughput than L2 locality.

**Lesson:** GPU schedulers are smarter than manual NUMA pinning. Don't fight the hardware scheduler unless you have profiling data showing it's making bad decisions.

### What doesn't matter on the GPU

- **Superpages (2MB pages):** Apple Silicon ARM64 uses fixed 16KB pages. `vm_allocate` with `VM_FLAGS_SUPERPAGE_SIZE_2MB` returns `KERN_INVALID_ARGUMENT`. Not available.
- **Command buffer type:** `commandBufferWithUnretainedReferences` (skip ARC retain/release) vs `commandBuffer` — zero measurable difference.
- **Encoder count:** Batching all experts' gate+up into one encoder vs separate encoders per expert — zero difference. Metal handles both patterns efficiently.

## Part 2: The I/O Story

### The landscape

Our I/O benchmark measured raw SSD performance for the expert read pattern:

| Access Pattern | Throughput | Latency (4 experts) |
|---|:---:|:---:|
| Sequential, warm page cache | 32.1 GB/s | 0.49 ms |
| Parallel 4T, warm cache | 29.2 GB/s | 0.97 ms |
| Parallel 4T, cold (F_NOCACHE) | 5.5 GB/s | 2.84 ms |
| Sequential, cold | 4.5 GB/s | 3.46 ms |
| mmap + memcpy, cold | 0.12 GB/s | varies |

The gap between warm (32 GB/s) and cold (5.5 GB/s) is the entire optimization story. Everything we tried was about moving more data from cold to warm.

### The mmap disaster

**What:** Replace `pread()` with `mmap()` + `memcpy()` for zero-syscall access to cached data.

**Result:** 0.56 tok/s — **5x slower** than pread.

**Why:** Each 3.9MB expert spans 240 × 16KB pages. For uncached data, mmap triggers 240 individual page faults, each requiring a separate kernel trap → I/O request → page table update. A single `pread()` call issues one large NVMe command for the entire 3.9MB range.

**Lesson:** `mmap()` is designed for random access to already-cached data. For bulk reads of potentially uncached data, `pread()` is dramatically better because it lets the kernel optimize the I/O pattern.

### The custom cache trap

We built increasingly sophisticated expert caching systems:

| Cache Type | Entries | Memory | Hit Rate | tok/s | Verdict |
|---|:---:|:---:|:---:|:---:|---|
| None (pread only) | 0 | 0 | 0% | 2.86 | Baseline |
| Metal LRU (500) | 500 | 3.5 GB | 35% | 3.14 | Small win |
| Metal LRU (1000) | 1000 | 7.1 GB | 44% | 2.24 | **Worse** |
| Metal LRU (2500) | 2500 | 9.8 GB | 55% | 2.24 | **Worse** |
| Metal LRU (3000) | 3000 | 21 GB | 55% | 1.99 | **Much worse** |
| Malloc zero-copy (2581) | 2581 | 18 GB | 52% 
