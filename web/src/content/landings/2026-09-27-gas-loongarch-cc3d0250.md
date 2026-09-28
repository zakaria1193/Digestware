---
project: binutils
subsystem: gas/loongarch
patch_id: null
tags:
- loongarch
- gas
- deprecation
commit_hash: cc3d02502e1d6dc311dc5c4883d55805d39ffba7
source_type: public_inbox
author: liu zhensong <liuzhensong@sourceware.org>
headline: 'LoongArch: Deprecate -mignore-start-align option'
tldr: LoongArch GAS deprecates the -mignore-start-align option as it's now handled
  by default optimizations.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit deprecates the `-mignore-start-align` option in LoongArch
  GAS. This option was previously used to disable alignment optimizations before the
  first linker-relaxable relocation. Since the new optimization in commit 90a7bfab3c335c208392dfee449cca48d25e0d50
  handles this case automatically, the option is no longer necessary. It is retained
  as a deprecated compatibility flag that issues a warning, and the associated internal
  `LARCH_opts.ignore_start_align` field is removed.
primer_glossary:
- term: -mignore-start-align
  definition: A compiler or assembler option for LoongArch that historically disabled
    specific alignment optimizations for fragments preceding the first linker-relaxable
    relocation.
- term: linker-relaxable relocation
  definition: A relocation that the linker can adjust or 'relax' after an initial
    linking pass, typically to optimize instruction encoding or code density. Fragments
    preceding such relocations may have special alignment requirements.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260927090851.36B404BA7995@sourceware.org
date: '2026-09-27'
is_stub: false
stub_reason: ''
---

The LoongArch assembler's -mignore-start-align option is deprecated because the assembler now automatically optimizes alignment before the first relax relocation. The option is kept for compatibility but will only issue a warning. The internal LARCH_opts.ignore_start_align flag has been removed.
