---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- binutils
- aarch64
- cygwin
- cross-compilation
- target support
discussion_id: 20261105114343.31926-1-evgeny.karpov@arm.com
source_type: public_inbox
title: '[PATCH v2 0/1] aarch64: Introduce aarch64-pc-cygwin target'
headline: 'aarch64: Introduce aarch64-pc-cygwin target'
tldr: Evgeny Karpov proposes adding 'aarch64-pc-cygwin' as a supported target in Binutils,
  with minor updates to formatting and GDB configuration in v2.
proposer: Evgeny Karpov <evgeny.karpov@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 7
technical_tradeoffs:
- Adding new target support (`aarch64-pc-cygwin`) vs. the complexity of maintaining
  configuration scripts across multiple tools (BFD, GAS, LD, GDB).
- Ensuring proper integration with the PE executable format used by Cygwin vs. potential
  conflicts or nuances.
- Cross-compilation support for AArch64 on Cygwin vs. the existing support for other
  targets and architectures.
exchanges:
- author: Evgeny Karpov
  role: proposer
  position: Submitted v2 of a patch to introduce the `aarch64-pc-cygwin` target, incorporating
    feedback on formatting, `pe.em`, and GDB configuration.
  quote: 'Hello,


    Thanks for reviewing v1.

    v2 contains minor changes and an update to the GDB configuration.


    Changes in v2:

    - Update formatting.

    - Exclude changes in pe.em.

    - Update GDB configuration.


    v1 2026-10-29:

    The patch adds support for aarch64-pc-cygwin target.

    https://sourceware.org/pipermail/binutils/2026-October/152276.html


    Regards,

    Evgeny'
- author: Evgeny Karpov
  role: proposer
  position: 'Provides a concise summary of the patch''s purpose: adding `aarch64-pc-cygwin`
    support.'
  quote: 'The patch adds support for aarch64-pc-cygwin target.


    Co-authored-by: Radek Barton <radek.barton@microsoft.com>

    ---'
- author: Jan Beulich
  role: reviewer
  position: Notes that the modification to `ld/emultempl/pep.em` should be handled
    by the 'config' project, suggesting a potential routing issue for that specific
    change.
  quote: "On 05.11.2026 12:43, Evgeny Karpov wrote:\nThe patch adds support for aarch64-pc-cygwin\
    \ target.\n\nCo-authored-by: Radek Barton <radek.barton@microsoft.com>\n---\n\
    \ bfd/config.bfd          | 2 +-\n binutils/configure      | 2 +-\n binutils/configure.ac\
    \   | 2 +-\n config.guess            | 3 +++\n gas/configure.tgt       | 2 +-\n\
    \ gdb/configure.host      | 1 +\n gdbserver/configure.srv | 6 ++++++\n ld/configure…"
primer_expert: This patch series introduces support for the `aarch64-pc-cygwin` target
  triplet in Binutils. This enables cross-compilation for the AArch64 architecture
  when using the Cygwin environment on a host system. The changes involve updating
  configuration scripts (`configure`, `config.guess`, `configure.tgt`) across BFD,
  GAS, and LD, as well as modifications to GDB and GDB server configurations. The
  inclusion of `pe.em` changes is noted as needing review by the 'config' project
  maintainers.
primer_glossary:
- term: aarch64
  definition: The 64-bit ARM architecture. It is a widely used instruction set architecture
    for servers, desktops, and mobile devices.
- term: Cygwin
  definition: A POSIX-compatible environment that runs on Microsoft Windows. It provides
    a Unix-like command-line interface and compatibility layer, allowing many Unix
    programs to be compiled and run on Windows.
- term: target triplet
  definition: A string that uniquely identifies a target platform for a compiler or
    toolchain. It typically consists of the architecture, vendor, and operating system
    (e.g., `x86_64-linux-gnu`).
- term: cross-compilation
  definition: The process of developing software on one platform (the host) for a
    different platform (the target). This requires a cross-compiler and associated
    tools that run on the host but generate code for the target.
- term: BFD
  definition: Binary File Descriptor library. A library used by GNU Binutils to provide
    a common interface for reading and writing various executable file formats (like
    ELF, COFF, a.out).
- term: GAS
  definition: GNU Assembler. The assembler component of the GNU toolchain.
- term: LD
  definition: GNU Linker. The linker component of the GNU toolchain.
- term: PE
  definition: Portable Executable. The file format used for executables, object code,
    and DLLs used in 32-bit and 64-bit versions of Windows operating systems.
series_id: 'binutils:aarch64: introduce aarch64-pc-cygwin target'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261105114343.31926-1-evgeny.karpov@arm.com
bugzilla_url: null
date: '2026-11-05'
is_stub: false
stub_reason: ''
---

Evgeny Karpov has submitted version 2 of a patch series to introduce official support for the `aarch64-pc-cygwin` target in Binutils. This target allows cross-compilation for AArch64 systems running the Cygwin environment. Version 2 includes minor formatting adjustments, excludes changes to `pe.em`, and updates the GDB configuration. The initial version of the patch, submitted earlier, focused on adding the target to various Binutils components like BFD, `configure` scripts, GAS, and LD, along with GDB and GDB server configurations. The primary goal is to enable a complete toolchain for AArch64 on Cygwin.
