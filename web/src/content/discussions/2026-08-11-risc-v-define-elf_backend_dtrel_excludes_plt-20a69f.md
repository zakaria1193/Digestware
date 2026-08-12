---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- elf
- relocations
- commit
discussion_id: e203f8a1-21e5-4df6-8a85-5c5bbcc7bb77.juewang@linux.alibaba.com
source_type: public_inbox
title: 'Re: [PATCH] RISC-V: define elf_backend_dtrel_excludes_plt'
headline: 'RISC-V: define elf_backend_dtrel_excludes_plt'
tldr: Wang Jue requests a binutils maintainer to commit a patch for RISC-V ELF backend.
proposer: wangjue <juewang@linux.alibaba.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Requires maintainer intervention for commit due to access control.
exchanges:
- author: wangjue <juewang@linux.alibaba.com>
  role: proposer
  position: Requests a binutils maintainer to commit a previously approved patch,
    as they do not have direct write access to the repository.
  quote: 'This patch has not been committed yet, and I do not have write access to

    the binutils repository.  Could you or another maintainer please commit

    it for me?'
primer_expert: This patch modifies binutils' RISC-V backend to define `elf_backend_dtrel_excludes_plt`.
  This flag likely controls which dynamic relocation entries are excluded from the
  Procedure Linkage Table (PLT) for Position Independent Executables (PIE) or Position
  Independent Code (PIC) on RISC-V. Correctly setting this is crucial for generating
  optimal and functional shared objects and executables.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/e203f8a1-21e5-4df6-8a85-5c5bbcc7bb77.juewang@linux.alibaba.com
bugzilla_url: null
date: '2026-08-11'
is_stub: false
stub_reason: ''
---

Wang Jue's patch, which defines `elf_backend_dtrel_excludes_plt` for RISC-V, has received approval but requires a maintainer to commit it due to the proposer lacking write access to the binutils repository. The change aims to correctly handle dynamic relocation excludes for the RISC-V architecture.
