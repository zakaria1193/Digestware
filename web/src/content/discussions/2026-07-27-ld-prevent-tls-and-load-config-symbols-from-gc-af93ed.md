---
project: binutils
subsystem: ld
patch_id: null
tags:
- linker
- mingw
- pe
- tls
- gc-sections
discussion_id: 8eb0155d-cbb3-4780-a81f-c360aa27bdde@126.com
source_type: public_inbox
title: 'ld: Prevent `_tls_used` and `_load_config_used` from being garbage-collected'
headline: 'ld: Prevent TLS and load config symbols from GC'
tldr: Patch prevents linker garbage collection of `_tls_used` and `_load_config_used`
  symbols for mingw-w64 PE targets.
proposer: LIU Hao <lh_mouse@126.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: 8
technical_tradeoffs:
- Preventing garbage collection of these symbols ensures correctness for PE executables
  but may slightly increase the size of executables that do not use TLS or specific
  load configurations.
- Correctly handling symbol garbage collection in conjunction with indirect references
  and specific file formats is complex.
exchanges:
- author: LIU Hao <lh_mouse@126.com>
  role: proposer
  position: Submits a patch to prevent `_tls_used` and `_load_config_used` symbols
    from being garbage-collected by the linker on mingw-w64 PE targets, as they are
    referenced indirectly and would otherwise be removed.
  quote: "Earlier today I pushed some patches to mingw-w64 to make `_tls_used` only\n\
    linked on demand, by referencing it indirectly through tentative definitions.\n\
    However, since the startup code no longer has strong references to `_tls_used`,\n\
    if LD is passed `--gc-sections`, it garbage-collects `_tls_used`, resulting in\n\
    a broken executable:\n\n    $ objdump -p bin/test_thread_id_cpp.exe | grep -F\
    \ .tls\n    Ent…"
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Acknowledged the patch and its description of how `_tls_used` could be
    removed due to `--gc-sections`.
  quote: 'On 27.07.2026 17:38, LIU Hao wrote:

    > From: LIU Hao <lh_mouse@126.com>

    >

    > Earlier today I pushed some patches to mingw-w64 to make `_tls_used` only

    > linked on demand, by referencing it indirectly through tentative definitions.

    > However, since the startup code no longer has strong references to `_tls_used`,

    > if LD is passed `--gc-sections`, it garbage-collects `_tls_used`, resulting
    in

    > a bro…'
- author: LIU Hao <lh_mouse@126.com>
  role: proposer
  position: Responded to Jan Beulich's comment with a truncated diff.
  quote: "在 2026-7-27 23:55, Jan Beulich 写道:\n>> --- a/ld/emultempl/pe.em\n>> +++\
    \ b/ld/emultempl/pe.em\n>> @@ -1573,6 +1573,16 @@ gld${EMULATION_NAME}_after_open\
    \ (void) \n>> \n>>      pe_output_file_set_long_section_names (link_info.output_bfd);\n\
    >> \n>> +  /* The RVAs of these symbols will be written into the PE header, so\
    \ they\n>> +     must not be collected.  */\n>> +#if defined (TARGET_IS_i386pe)\n\
    >> +  lang_add…"
primer_expert: Recent changes in mingw-w64 startup code have made `_tls_used` and
  `_load_config_used` symbols implicitly referenced via tentative definitions. When
  the binutils linker (`ld`) is invoked with `--gc-sections`, it performs garbage
  collection of unreferenced sections. Since these symbols are no longer strongly
  referenced by the startup code, `ld` incorrectly removes them, breaking the PE executable's
  Thread Local Storage (TLS) and load configuration structures. This patch prevents
  their garbage collection by explicitly registering them using `lang_add_gc_name`.
primer_glossary:
- term: ld
  definition: The GNU linker, part of the GNU Binutils package, responsible for combining
    object files into executables.
- term: --gc-sections
  definition: A linker option that enables garbage collection of unused sections in
    the output file, reducing executable size.
- term: mingw-w64
  definition: A widely used fork of MinGW which provides a build environment for native
    MS Windows applications using GCC.
- term: PE
  definition: Portable Executable format, the file format used for executables, DLLs,
    and object files on Windows operating systems.
- term: _tls_used
  definition: A symbol often used in C/C++ runtimes to indicate that Thread Local
    Storage (TLS) is in use by the program.
- term: _load_config_used
  definition: A symbol related to the PE loader configuration directory, indicating
    that specific loader features are required.
- term: tentative definition
  definition: In C/C++, a declaration of a variable without an initializer. If no
    definition with an initializer is seen, it is assumed to have a default initializer
    (e.g., zero).
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/8eb0155d-cbb3-4780-a81f-c360aa27bdde@126.com
bugzilla_url: null
date: '2026-07-27'
is_stub: false
stub_reason: ''
---

This patch addresses an issue where the linker (`ld`) with `--gc-sections` would garbage-collect symbols like `_tls_used` and `_load_config_used` on mingw-w64 PE targets. These symbols are necessary for the PE header at runtime and must not be collected. The change adds these symbols to the list of names that should not be garbage-collected, ensuring executables remain functional.
