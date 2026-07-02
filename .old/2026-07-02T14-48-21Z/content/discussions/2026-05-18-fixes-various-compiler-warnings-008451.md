---
project: gcc
subsystem: gcc
patch_id: null
tags:
- compiler warnings
- diagnostics
- code quality
discussion_id: '127'
source_type: github_pr
title: Fix various compiler warnings (-Wformat-diag, -Wmaybe-uninitialized, -Wdelete-non-virtual-dtor)
headline: Fixes various compiler warnings
tldr: This PR resolves compiler warnings related to formatting, uninitialized variables,
  non-virtual destructors, and unused variables in GCC.
proposer: Zeinab-Ayman
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Adding a virtual destructor might introduce a slight runtime overhead, but prevents
  memory leaks when deleting objects of derived classes through base class pointers.
- Initializing variables upfront can improve code clarity but might add unnecessary
  assignments in some cases.
exchanges: []
primer_expert: This PR targets warning cleanup across multiple GCC modules, including
  diagnostics, text-art, and the analyzer. These warnings, such as `-Wformat-diag`,
  `-Wmaybe-uninitialized`, and `-Wdelete-non-virtual-dtor`, are detected during the
  compilation of GCC itself.  Resolving these warnings improves the overall quality
  and maintainability of the GCC codebase.
primer_general: When building software, compilers often produce warnings about potential
  issues in the code.  These warnings can range from formatting inconsistencies to
  more serious problems like uninitialized variables or improper memory management.  This
  PR addresses a collection of such warnings that arise when compiling GCC itself,
  improving the compiler's code quality and reducing potential risks.
series_id: null
series_role: standalone
series_parts: []
url: https://github.com/gcc-mirror/gcc/pull/127
bugzilla_url: null
date: '2026-05-18'
is_stub: false
---

This PR fixes a set of compiler warnings across the diagnostics, text-art, and analyzer modules in GCC.  The warnings addressed include `-Wformat-diag` issues, `-Wmaybe-uninitialized` warnings, `-Wdelete-non-virtual-dtor` warnings, and `-Wunused-variable` warnings.  Fixing these warnings improves code quality and reduces the risk of potential bugs, contributing to a more robust compiler.
