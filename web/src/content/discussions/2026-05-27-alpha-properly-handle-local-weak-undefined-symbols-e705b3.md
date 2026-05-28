---
project: binutils
subsystem: alpha
patch_id: null
tags:
- alpha
- linker
- relocation
- asan
- undefined symbol
discussion_id: ahbpFYH6noihSaKO@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: alpha: Properly handle local weak undefined symbols'
headline: 'alpha: Properly handle local weak undefined symbols'
tldr: Fixes a null pointer dereference in the alpha backend that caused ASan failures
  when handling local weak undefined symbols.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Adds a null check, which has a minimal performance impact.
- Prevents a crash and improves robustness.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Proposes a patch to fix a null pointer dereference in `elf64_alpha_relocate_section`
    when handling local weak undefined symbols, resolving ASan failures.
  quote: 'asan complains "runtime error: member access within null pointer"

    for &h->root with NULL h, which is annoying since &h->root is the

    same address as h, causing

    alpha-linux-gnu  +FAIL: TLS -fpic -shared'
primer_expert: The `elf64_alpha_relocate_section` function in binutils handles relocations
  for Alpha architecture ELF files.  Local weak undefined symbols require special
  handling during linking.  The patch guards against a null `h` pointer, which can
  occur in specific scenarios involving these symbols, preventing a crash detected
  by ASan.
primer_general: When linking programs, the linker needs to resolve references between
  different parts of the code. Sometimes, a symbol (like a variable or function name)
  might be declared but not defined in the same file.  These are called undefined
  symbols.  Weak symbols are a special type of symbol that can be overridden by a
  definition in another file. This patch fixes a bug in how the binutils linker handles
  these undefined weak symbols on Alpha architecture, preventing a crash reported
  by a memory error detector (ASan).
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/ahbpFYH6noihSaKO@squeak.grove.modra.org
bugzilla_url: null
date: '2026-05-27'
is_stub: false
---

A patch addresses a null pointer dereference in the alpha backend of binutils when processing local weak undefined symbols. The issue triggered AddressSanitizer (ASan) errors, leading to test failures related to TLS with various configurations (e.g., `-fpic -shared`).  The fix involves checking for a null `h` pointer before accessing its members, preventing the dereference and resolving the ASan complaint.
