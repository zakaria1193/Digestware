---
project: binutils
subsystem: binutils
patch_id: null
tags:
- macho
- gas
- assembler
- binutils
- relocation
discussion_id: F41F5DF9-8AA5-4E95-B545-5028A0715060@sandoe.co.uk
source_type: public_inbox
title: 'Re: macho gas support'
headline: macho gas support
tldr: A developer reports progress on Mach-O assembler support, noting some test failures
  and relocation issues on darwin17.
proposer: Iain Sandoe <iain@sandoe.co.uk>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adding Mach-O support to gas increases its complexity and maintenance burden.
- The remaining test failures and relocation issues need to be resolved before the
  support can be considered complete.
exchanges:
- author: Iain Sandoe
  role: other
  position: Reports progress on Mach-O assembler support, noting some test failures
    and relocation issues on darwin17.
  quote: 'OK ..  so I worked on darwin17 which is the last OS version to support native
    32b officially (albeit deprecated).


    I built bfd, binutils and gas as 32b exes, using GCC-10.5 (unfortunately, the
    system clang does not build binutils on that platform).


    $ ./gas/as-new --version

    GNU assembler (GNU Binutils) 2.46.50.20260526

    …'
primer_expert: The discussion concerns the effort to add Mach-O object file format
  support to the GNU assembler (gas). Mach-O is the object file format used by macOS
  and other Apple operating systems. The report highlights progress made in building
  gas for a 32-bit macOS target (darwin17) and identifies remaining test failures
  and relocation issues. The focus is on `as-new`, the new implementation of the assembler,
  and its ability to generate correct relocations for section differences in Mach-O
  binaries.
primer_general: The GNU assembler (gas) is a crucial part of the toolchain that translates
  assembly code into machine code.  This discussion involves adding support for the
  Mach-O object file format, which is used by macOS.  The goal is to enable gas to
  assemble code that can be linked into applications and libraries on macOS.  The
  developer is working on getting the assembler to generate the correct output and
  relocation information so that the resulting code can be linked correctly. Relocations
  are adjustments that the linker makes to the code to account for the final memory
  addresses of different parts of the program.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/F41F5DF9-8AA5-4E95-B545-5028A0715060@sandoe.co.uk
bugzilla_url: null
date: '2026-05-28'
is_stub: false
---

A developer provides an update on their work to support the Mach-O object file format in the GNU assembler (gas). They report that they were able to build gas for the i686-apple-darwin17 target (32-bit macOS), and that some tests now pass. They also note that some tests are still failing, and that there are issues with generating correct relocations for section differences. This work aims to allow gas to assemble code that can be linked into Mach-O binaries, which is useful for building software on macOS and other Apple platforms.
