---
project: gcc
subsystem: target/riscv
patch_id: null
tags:
- RISC-V
- vectorization
- optimization
- cost model
commit_hash: cfa4979a2c2f91c5077bf5d1c1500518581b2627
source_type: github
author: Robin Dapp
headline: RISC-V vector cost model includes scalar loads/stores.
tldr: RISC-V vector cost model now accounts for scalar loads/stores to avoid ratio
  mismatches.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: In `config/riscv/riscv-vector-costs.cc`, the `costs::record_type_sizes`
  function is responsible for assigning costs to various data types and operations
  for the RISC-V vector extension. The LMUL (Lane Multiplication) ratio is a key factor
  in vector instruction cost and scheduling. This commit adds `scalar_load` and `scalar_store`
  to the types recorded by this function. This ensures that when these operations
  are used, for example, within gather/scatter instructions which are costed as scalar
  loads/stores, they are correctly considered in the overall LMUL ratio calculation,
  preventing inaccura…
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on Reduced
    Instruction Set Computing principles. It is modular and extensible, with specific
    extensions for vector processing.
- term: LMUL ratio
  definition: Lane Multiplication ratio. In RISC-V vector instructions, LMUL determines
    how many elements a single vector instruction operates on. A higher LMUL means
    more elements are processed per cycle, impacting instruction cost and throughput.
- term: Vector loads/stores
  definition: Instructions that load or store multiple data elements from or to memory
    in a single operation, utilizing vector registers.
- term: Gathers and scatters
  definition: Specialized vector memory operations where the addresses of the elements
    to be accessed are specified in a separate vector register (gather) or written
    to memory (scatter). These are often implemented using scalar load/store mechanisms
    at a lower level.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cfa4979a2c2f91c5077bf5d1c1500518581b2627
date: '2026-09-29'
is_stub: false
stub_reason: ''
---

The cost model for RISC-V vector operations has been updated to include scalar loads and stores in the LMUL ratio calculation. Previously, gathers and scatters were costed as scalar operations but not factored into the LMUL ratio, leading to potential mismatches when comparing different loops.

This change ensures that the vector cost model accurately reflects the performance implications of scalar operations within vector contexts, improving loop optimization decisions.
