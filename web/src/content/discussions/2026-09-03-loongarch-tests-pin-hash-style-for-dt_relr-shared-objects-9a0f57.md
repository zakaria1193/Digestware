---
project: binutils
subsystem: ld
patch_id: null
tags:
- ld
- loongarch
- testing
- relocations
- hash style
discussion_id: QXxie6f1nYx2v6HGPjRGaIyTIxseNQZ7Lwb39fSMi6XgE-ftXUTyJSSbeevySD3jmM1pN2CWCiQgsdw3XUB73yGfyfiLNI1tIgr_kQ-0FtA=@protonmail.com
source_type: public_inbox
title: '[PATCH 2/3] ld: Pin the hash style in the LoongArch DT_RELR shared tests'
headline: 'LoongArch tests: Pin hash style for DT_RELR shared objects'
tldr: Pins the hash style to 'both' for LoongArch DT_RELR shared library tests.
proposer: mintsuki <mintsuki@protonmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Ensures test stability by fixing expectations related to hash style.
- Makes the tests less flexible regarding the default linker behavior but more reliable.
exchanges:
- author: mintsuki <mintsuki@protonmail.com>
  role: proposer
  position: Pins the hash style to `--hash-style=both` for LoongArch DT_RELR shared
    tests to ensure consistent symbol indexing.
  quote: 'These three tests match .rela.dyn entries with the symbol index of

    r_info written out in full, and that index depends on the default hash

    style.  A GNU hash table requires the undefined symbols to precede the

    defined ones in .dynsym, so an undefined weak in these tests sorts to

    index 2 with --hash-style=both or gnu, and to the end of the table with

    sysv.  The expectations were written against the…'
primer_expert: This patch modifies the testsuite for LoongArch bare-metal targets.
  Specifically, it pins the hash style used by the linker to `--hash-style=both` for
  three tests involving `DT_RELR` relocations in shared objects. This ensures that
  the symbol indices within the relocation entries are consistent, as the default
  hash style for bare-metal targets (`sysv`) differs from the style expected by these
  tests (`gnu`/`both`). This is a preparatory step for enabling PIE and shared library
  support.
primer_glossary:
- term: DT_RELR
  definition: A dynamic tag in an ELF file that indicates the presence and location
    of RELR relocations, a more compact form of relocation used in some systems.
- term: hash style
  definition: Refers to the algorithm used by the linker to construct symbol hash
    tables, which are used for efficient symbol lookup in shared libraries. Common
    styles include 'sysv', 'gnu', and 'both'.
- term: symbol index
  definition: An integer identifier for a symbol within an object file's symbol table.
- term: relocation
  definition: Information in an object file that describes how to modify addresses
    and other references when the code is linked or loaded into memory.
- term: bare-metal target
  definition: A system where the software runs directly on the hardware without an
    underlying operating system.
series_id: 'binutils:ld: pin the hash style in the loongarch dt_relr shared tests'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/QXxie6f1nYx2v6HGPjRGaIyTIxseNQZ7Lwb39fSMi6XgE-ftXUTyJSSbeevySD3jmM1pN2CWCiQgsdw3XUB73yGfyfiLNI1tIgr_kQ-0FtA=@protonmail.com
bugzilla_url: null
date: '2026-09-03'
is_stub: false
stub_reason: ''
---

This patch pins the hash style to `--hash-style=both` for three LoongArch DT_RELR shared library tests. This is necessary because the tests rely on specific symbol indices in the `.rela.dyn` section, which are dependent on the linker's hash style (GNU vs. SYSV). The bare-metal default is SYSV, but the tests were written against the GNU hash style. Pinning the style ensures consistent test results and is a prerequisite for the following patch that enables shared library and PIE support for LoongArch.
