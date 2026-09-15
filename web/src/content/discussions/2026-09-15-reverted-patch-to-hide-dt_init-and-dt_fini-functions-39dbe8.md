---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- elf
- linker
- abi
- reverted
discussion_id: aqim7jougG6iio7x@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: [PATCH] elf: Hide DT_INIT and DT_FINI functions'
headline: Reverted patch to hide DT_INIT and DT_FINI functions
tldr: Patch to hide DT_INIT/DT_FINI functions in ELF reverted due to negative community
  feedback.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: needs_revision
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Hiding linker-internal symbols vs. providing source-level control for initialization/termination
  functions.
- Potential impact on dynamic linking behavior and runtime initialization/cleanup
  compared to the complexity of linker-level hiding.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: maintainer
  position: Reverted a patch that hid DT_INIT and DT_FINI functions in ELF, citing
    community consensus and the availability of source-level hiding.
  quote: 'I have reverted the patch since majority opinion seems to be that ld

    hiding _init and _fini is surprising, it can be accomplished in

    source, and impact of non-hidden _init and _fini is small.  There may

    even be reasons to export them.


    On top of that, the patch introduced regressions needing the following

    to fix.'
primer_expert: This discussion concerns a patch for the `binutils` ELF object file
  handler that proposed hiding the `DT_INIT` and `DT_FINI` symbols. These symbols
  typically point to functions executed during dynamic linking initialization and
  termination. The maintainer reverted the patch after receiving feedback that hiding
  them via the linker is unexpected and that source-level control is sufficient. The
  decision also acknowledges potential benefits of exporting these symbols and addresses
  regressions introduced by the patch.
primer_glossary:
- term: DT_INIT
  definition: A dynamic section tag in an ELF file that indicates the address of the
    initialization function called when a shared library is loaded.
- term: DT_FINI
  definition: A dynamic section tag in an ELF file that indicates the address of the
    termination function called when a shared library is unloaded.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like systems.
- term: ld
  definition: The GNU linker, part of the binutils package, responsible for combining
    object files and libraries into an executable or shared library.
- term: dynamic linking
  definition: A process where an executable or library links against shared libraries
    at runtime, rather than having all code statically included at build time.
- term: ABI
  definition: Application Binary Interface. Defines how compiled code interacts at
    the binary level, including function calling conventions, data type representation,
    and system call interfaces.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aqim7jougG6iio7x@squeak.grove.modra.org
bugzilla_url: null
date: '2026-09-15'
is_stub: false
stub_reason: ''
---

Alan Modra has reverted a patch that aimed to hide DT_INIT and DT_FINI functions in ELF objects. The decision was made because the majority opinion was that `ld` hiding these functions is surprising, they can be hidden at the source level, and the impact of them not being hidden is small. There might even be reasons to keep them exported. The patch also introduced regressions that required further fixes.
