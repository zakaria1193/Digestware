---
project: binutils
subsystem: sim/erc32
patch_id: null
tags:
- binutils
- gdb
- simulator
- erc32
- compiler warnings
discussion_id: 6ec2bf41-7c39-43d5-a63a-87025ae5a5be@efficios.com
source_type: public_inbox
title: 'Re: [PATCH 10/18] sim/erc32: fix -Wunused-but-set-global errors'
headline: 'sim/erc32: fix -Wunused-but-set-global errors'
tldr: Removes unused variables and marks others as unused in the erc32 simulator to
  fix compiler warnings.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs:
- Removes unused code and resolves compiler warnings.
- Improves code clarity by marking variables as unused where appropriate.
- No impact on simulator functionality.
exchanges:
- author: Simon Marchi <simon.marchi@efficios.com>
  role: proposer
  position: Submits a patch to fix unused variable warnings in the erc32 simulator
    by removing unused variables and marking others as unused.
  quote: "Building the erc32 simulator with a recent clang fails with:\n\n    /home/smarchi/src/binutils-gdb/sim/erc32/erc32.c:159:19:\
    \ error: variable 'mec_icr' set but not used [-Werror,-Wunused-but-set-global]\n\
    \    /home/smarchi/src/binutils-gdb/sim/erc32/erc32.c:165:19: error: variable\
    \ 'posted_irq' set but not used [-Werror,-Wunused-but-set-global]\n    /home/smarchi/src/binutils-gdb/sim/erc32/erc32.c:247:1…"
primer_expert: This patch modifies the ERC32 simulator code (`sim/erc32/erc32.c`)
  to resolve compiler warnings related to unused variables. The variables `mec_icr`
  and `posted_irq` were found to be always initialized to zero in `mec_reset` and
  never subsequently used, so they are removed. The UART data variables (`uarta_data`,
  `uartb_data`) are only accessed when the `FAST_UART` macro is not defined. Since
  the simulator is usually built with `FAST_UART` enabled, these variables are effectively
  unused in the common build configuration. They are therefore marked with `ATTRIBUTE_UNUSED`
  to suppress compiler wa…
primer_glossary:
- term: simulator
  definition: A program that mimics the behavior of a hardware device or system. In
    this context, it simulates the execution of instructions for a specific processor.
- term: ERC32
  definition: A SPARC-based System-on-Chip (SoC) processor often used in space applications.
    Binutils includes a simulator for it.
- term: FAST_UART
  definition: A preprocessor macro that likely enables a faster, possibly simplified,
    implementation of UART (Universal Asynchronous Receiver/Transmitter) simulation
    in the ERC32 simulator.
- term: ATTRIBUTE_UNUSED
  definition: A compiler attribute used to indicate that a function or variable may
    be intentionally unused. This suppresses compiler warnings about such symbols.
- term: UART
  definition: Universal Asynchronous Receiver/Transmitter, a hardware component that
    handles serial communication between devices.
series_id: 'binutils:sim/erc32: fix -wunused-but-set-global errors'
series_role: reply
series_parts:
- title: 'sim/erc32: fix -Wunused-but-set-global errors'
  url: https://inbox.sourceware.org/binutils/20261019193231.1708375-11-simon.marchi@efficios.com
  n: 10
  total: 18
url: https://inbox.sourceware.org/binutils/6ec2bf41-7c39-43d5-a63a-87025ae5a5be@efficios.com
bugzilla_url: null
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

This patch addresses compiler warnings (`-Wunused-but-set-global`) in the ERC32 simulator. It removes two variables, `mec_icr` and `posted_irq`, as they are always initialized to zero and never used. Additionally, `uarta_data` and `uartb_data` are only read when `FAST_UART` is not defined, but the simulator is typically built with `FAST_UART` enabled. These variables are marked with `ATTRIBUTE_UNUSED` to suppress warnings, similar to other unused functions in the same situation. This cleans up the codebase and resolves compiler warnings.
