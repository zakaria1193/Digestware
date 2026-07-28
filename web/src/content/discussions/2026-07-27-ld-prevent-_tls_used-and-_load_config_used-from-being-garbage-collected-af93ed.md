---
project: binutils
subsystem: ld
patch_id: null
tags:
- ld
- linker
- windows
- mingw
- gc-sections
discussion_id: 8eb0155d-cbb3-4780-a81f-c360aa27bdde@126.com
source_type: public_inbox
title: 'ld: Prevent `_tls_used` and `_load_config_used` from being garbage-collected'
headline: 'ld: Prevent `_tls_used` and `_load_config_used` from being garbage-collected'
tldr: Prevents linker garbage collection of `_tls_used` and `_load_config_used` symbols
  on Windows, fixing broken executables.
proposer: LIU Hao <lh_mouse@126.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: 8
technical_tradeoffs:
- Prevents executable corruption on Windows by retaining essential symbols.
- Slightly increases executable size by ensuring `_tls_used` and `_load_config_used`
  are not garbage collected.
exchanges:
- author: LIU Hao <lh_mouse@126.com>
  role: proposer
  position: Submits a patch to prevent garbage collection of `_tls_used` and `_load_config_used`
    symbols in `ld`, which is necessary for `--gc-sections` with recent mingw-w64
    changes that caused broken executables.
  quote: 'Earlier today I pushed some patches to mingw-w64 to make `_tls_used` only

    linked on demand, by referencing it indirectly through tentative definitions.

    However, since the startup code no longer has strong references to `_tls_used`,

    if LD is passed `--gc-sections`, it garbage-collects `_tls_used`, resulting in

    a broken executable:'
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Acknowledges the issue and the proposed solution, asking for confirmation
    on whether the fix should include all PE targets or only specific ones like i386pe.
  quote: "On 27.07.2026 17:38, LIU Hao wrote:\n> From: LIU Hao <lh_mouse@126.com>\n\
    > \n> Earlier today I pushed some patches to mingw-w64 to make `_tls_used` only\n\
    > linked on demand, by referencing it indirectly through tentative definitions.\n\
    > However, since the startup code no longer has strong references to `_tls_used`,\n\
    > if LD is passed `--gc-sections`, it garbage-collects `_tls_used`, resulting\
    \ in\n> a br…"
- author: LIU Hao <lh_mouse@126.com>
  role: contributor
  position: Responds to Jan Beulich's query, providing the corrected patch that includes
    conditional compilation for `TARGET_IS_i386pe` to handle different symbol naming
    conventions.
  quote: "--- a/ld/emultempl/pe.em\n+++ b/ld/emultempl/pe.em\n@@ -1573,6 +1573,16\
    \ @@ gld${EMULATION_NAME}_after_open (void)\n\n     pe_output_file_set_long_section_names\
    \ (link_info.output_bfd);\n\n+  /* The RVAs of these symbols will be written into\
    \ the PE header, so they\n+     must not be collected.  */\n+#if defined (TARGET_IS_i386pe)\n\
    +  lang_add_gc_name (\"__tls_used\");\n+  lang_add_gc_name (\"__load_config_used\"\
    …"
primer_expert: This patch modifies the PE (Portable Executable) emulation file for
  `ld` to prevent the garbage collection of `__tls_used` and `__load_config_used`
  symbols. These symbols are essential for the TLS (Thread-Local Storage) and Load
  Configuration Directory structures in Windows executables. Recent changes in the
  mingw-w64 startup code led to these symbols being defined only tentatively, making
  them subject to `--gc-sections`. This change ensures they are retained, preserving
  the integrity of the PE header which relies on their presence and RVAs.
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or shared library.
- term: PE
  definition: Portable Executable, the file format for executables, object code, and
    DLLs used in 32-bit and 64-bit versions of Windows operating systems.
- term: --gc-sections
  definition: A linker option that enables garbage collection of unused sections in
    the output file. This helps reduce the final executable size.
- term: mingw-w64
  definition: A widely used fork of the MinGW project that provides a C compiler (GCC)
    and development tools for creating Windows applications, supporting both 32-bit
    and 64-bit targets.
- term: RVA
  definition: Relative Virtual Address. An address relative to the base address of
    the image, used in PE executables.
- term: TLS
  definition: Thread-Local Storage. A mechanism that allows threads to have their
    own private copy of a variable.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/8eb0155d-cbb3-4780-a81f-c360aa27bdde@126.com
bugzilla_url: null
date: '2026-07-27'
is_stub: false
stub_reason: ''
---

This patch prevents the `ld` linker from garbage-collecting the `_tls_used` and `_load_config_used` symbols when the `--gc-sections` option is used. These symbols are crucial for the PE executable format on Windows, as their Relative Virtual Addresses (RVAs) are written into the PE header. Recent changes in mingw-w64 made these symbols only linked on demand, leading to their removal by garbage collection and resulting in broken executables. The patch adds these symbols to a list that `ld` will not garbage-collect, ensuring correct executable generation.
