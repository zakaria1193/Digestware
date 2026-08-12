---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- elf
- relocation
- plt
discussion_id: 1135d74b-52b8-460e-87ae-3acb57f3fbe9@iscas.ac.cn
source_type: public_inbox
title: 'Re: Re: [PATCH] RISC-V: define elf_backend_dtrel_excludes_plt'
headline: 'RISC-V: define elf_backend_dtrel_excludes_plt'
tldr: Patch to define elf_backend_dtrel_excludes_plt for RISC-V has been committed.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Committed
outcome: committed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jiawei
  role: proposer
  position: Requested a maintainer to commit a previously approved patch for RISC-V,
    as they lack write access.
  quote: 'This patch has not been committed yet, and I do not have write access to

    the binutils repository. Could you or another maintainer please commit

    it for me?'
- author: Jiawei
  role: contributor
  position: Confirmed that the patch has been committed.
  quote: "Since this has already been approved by Nelson, pushed as \n|4e8ba93fdb24f9bcf31f706e62e67c57ae91168f|."
primer_expert: This is a commit confirmation for a RISC-V specific patch in Binutils.
  The patch defines `elf_backend_dtrel_excludes_plt`, likely related to how dynamic
  relocations (DT_REL) interact with the Procedure Linkage Table (PLT) for RISC-V
  ELF binaries. The confirmation indicates successful integration into the codebase.
primer_glossary:
- term: elf_backend_dtrel_excludes_plt
  definition: A flag or setting within the Binutils ELF backend for RISC-V that likely
    controls whether dynamic relocations exclude entries related to the Procedure
    Linkage Table (PLT). This can affect how dynamically linked executables are resolved.
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on reduced
    instruction set computing principles. It is designed to be simple, modular, and
    extensible.
- term: ELF
  definition: Executable and Linkable Format. A common file format for object files,
    executables, shared libraries, and core dumps on Unix-like systems.
- term: DT_REL
  definition: A dynamic section tag in an ELF file indicating the presence of relocation
    entries used for dynamic linking. These entries specify how to modify symbols
    in a shared object or executable at load time.
- term: PLT
  definition: Procedure Linkage Table. A table used in dynamically linked executables
    and shared libraries to resolve external function calls at runtime.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/1135d74b-52b8-460e-87ae-3acb57f3fbe9@iscas.ac.cn
bugzilla_url: null
date: '2026-08-12'
is_stub: false
stub_reason: ''
---

A patch to define `elf_backend_dtrel_excludes_plt` for the RISC-V architecture, previously approved by Nelson, has been committed. Jiawei, who does not have write access to the repository, requested a maintainer to commit it.
