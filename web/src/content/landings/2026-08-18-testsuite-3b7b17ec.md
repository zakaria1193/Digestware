---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- alpha
- inline assembly
commit_hash: 3b7b17ecc0a5e86e9215161fb302653690549bc7
source_type: github
author: Matt Turner
headline: Require asm goto with outputs for test pr125545.c
tldr: A test case now requires support for 'asm goto' with output operands, fixing
  failures on targets like Alpha.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The test `pr125545.c` employs `asm goto` with an output operand. Targets
  lacking support for this specific feature (e.g., Alpha) would fail with an error
  message. This patch modifies the test to include `require asm_goto_with_outputs`,
  ensuring that DejaGnu only executes this test on toolchains that explicitly support
  `asm goto` with output operands.
primer_glossary:
- term: asm goto
  definition: A GCC extension that allows `goto` statements within inline assembly
    code, enabling conditional branching directly from assembly.
- term: output operand
  definition: In GCC's inline assembly, an operand specified to receive the result
    of the assembly instruction.
- term: asm_goto_with_outputs
  definition: A GCC testsuite macro or condition that checks if the target architecture
    and compiler support the 'asm goto' construct when it has output operands.
discussion_id_link: null
bugzilla_pr: null
series_id: 'gcc:testsuite: require asm goto with outputs in pr125545.c'
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3b7b17ecc0a5e86e9215161fb302653690549bc7
date: '2026-08-18'
is_stub: true
stub_reason: low_score
---

The test `pr125545.c` uses an inline assembly statement with the `asm goto` construct and an output operand. Previously, it did not explicitly require support for this feature, causing it to fail on targets like Alpha that do not support 'asm goto' with outputs. This commit adds a requirement for `asm_goto_with_outputs`, ensuring the test only runs on compatible targets.
