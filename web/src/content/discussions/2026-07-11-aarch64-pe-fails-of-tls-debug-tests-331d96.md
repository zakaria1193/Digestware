---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- gas
- testing
- aarch64
- TLS
discussion_id: alIDucLjp-_De53W@squeak.grove.modra.org
source_type: public_inbox
title: aarch64-pe fails of tls-debug tests
headline: aarch64-pe fails of tls-debug tests
tldr: Test suite adjustments to fix failing aarch64-pe TLS debug tests by using a
  generic ELF format check.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Replaces a potentially fragile target-specific test condition with a more general
  format check.
- Ensures tests relevant to ELF are only run on ELF targets, improving test reliability.
exchanges: []
primer_expert: The gas testsuite for aarch64 currently includes tests for TLS debug
  information that incorrectly rely on ELF-specific section directives. These directives
  are not universally applicable to all aarch64 configurations, particularly for targets
  like aarch64-pe (Portable Executable). The change modifies the test directives to
  use a more generic `is_elf_format` check, ensuring the tests only run when the target
  is indeed ELF, thus resolving spurious failures.
primer_glossary:
- term: aarch64
  definition: The 64-bit ARM architecture.
- term: PE
  definition: Portable Executable. A file format used for executables, DLLs, and object
    code in 32-bit and 64-bit versions of Windows operating systems. Binutils supports
    generating PE files for ARM targets.
- term: TLS
  definition: Thread-Local Storage. A storage mechanism that allows a variable to
    have unique instances for each thread of execution.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package. It translates assembly
    language code into machine code.
- term: testsuite
  definition: A collection of tests designed to verify the correct functionality of
    a software program. In this case, it's for the GNU Assembler.
- term: ELF section directives
  definition: Directives used in assembly code to define or manipulate sections within
    an ELF object file. Examples include specifying section names and attributes.
- term: is_elf_format
  definition: A condition or variable used within the gas testsuite to determine if
    the current target uses the ELF file format.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alIDucLjp-_De53W@squeak.grove.modra.org
bugzilla_url: null
date: '2026-07-11'
is_stub: false
stub_reason: ''
---

Alan Modra proposes changes to the gas testsuite to fix failing TLS debug tests for the aarch64-pe target. The tests currently use ELF section directives which are not specific to aarch64, leading to failures. The fix replaces the target-specific check with a generic `is_elf_format` check.
