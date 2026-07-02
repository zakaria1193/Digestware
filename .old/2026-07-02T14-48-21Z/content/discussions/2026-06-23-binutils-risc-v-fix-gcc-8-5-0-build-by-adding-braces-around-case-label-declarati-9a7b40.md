---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- gcc
- build-fix
- compatibility
discussion_id: 20260623133508.2896582-1-zhuangqiubin@linux.spacemit.com
source_type: public_inbox
title: '[PATCH v3] RISC-V: Fix build with GCC-8'
headline: 'Binutils RISC-V: Fix GCC 8.5.0 build by adding braces around case label
  declarations'
tldr: Binutils fixes GCC 8.5.0 build errors for RISC-V by adding braces around declarations
  immediately following `case` labels.
proposer: Mark Zhuang <zhuangqiubin@linux.spacemit.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Adding braces introduces additional scopes but is a standard C/C++ practice to resolve
  such compilation errors and should not impact performance or correctness.
exchanges:
- author: Mark Zhuang <zhuangqiubin@linux.spacemit.com>
  role: proposer
  position: Proposes to fix Binutils build failures with GCC 8.5.0 on RISC-V by adding
    braces around declarations that immediately follow `case` labels, conforming to
    GCC's parsing requirements.
  quote: GCC 8.5.0 rejects a declaration right after a case label. Add braces to fix
    it.
primer_expert: This patch addresses a C/C++ language compatibility issue when compiling
  Binutils for RISC-V targeting environments with GCC 8.5.0. Specifically, GCC 8.5.0
  enforces a stricter C language rule (or interpretation thereof) than previous versions
  concerning variable declarations within `switch` statements. A declaration directly
  following a `case` label without being enclosed in curly braces `{}` creates a jump
  into the middle of a scope, which is undefined behavior and rejected by GCC 8.5.0.
  The fix involves explicitly scoping these declarations with braces, thereby moving
  the declaration into a…
primer_general: Compilers translate human-readable code into machine instructions.
  Different versions of compilers can sometimes interpret programming language rules
  slightly differently. This patch fixes a problem that occurs when trying to build
  the Binutils (a set of essential programming tools, including an assembler and disassembler)
  for RISC-V processors using a specific version of the GCC compiler (version 8.5.0).
  The issue is that GCC 8.5.0 is very strict about where you can declare new variables
  inside certain types of code blocks called `switch` statements. If a variable is
  declared immediately after a `case` label (a specific entry point in a `switch`
  statement) without being enclosed in curly braces (`{}`), GCC 8.5.0 considers it
  an error. The fix is simply to add these curly braces, which creates a small, self-contained
  section of code for the variable, making it compliant with GCC 8.5.0's rules and
  allowing the Binutils to compile successfully.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260623133508.2896582-1-zhuangqiubin@linux.spacemit.com
bugzilla_url: null
date: '2026-06-23'
is_stub: false
---

This patch (v3) addresses a build issue with GCC 8.5.0 when compiling Binutils for RISC-V. GCC 8.5.0 rejects declarations that immediately follow a `case` label in `switch` statements. The fix involves adding braces (`{}`) around such declarations, implicitly creating a new scope and satisfying GCC's stricter parsing rules.
