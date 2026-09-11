---
project: binutils
subsystem: elf
patch_id: null
tags:
- ELF
- linker
- function size
- shared libraries
- MIPS
discussion_id: CAMe9rOo0M1A28Kty+TgzdLB4pRG1xnmdYM=RaDWHw3REMCVzvA@mail.gmail.com
source_type: public_inbox
title: '[PATCH v2] elf: Only use function size from regular object'
headline: 'elf: Only use function size from regular object'
tldr: Ensures linker uses function size from regular objects, not shared libraries,
  for relevance.
proposer: H.J. Lu
consensus: Under Review
outcome: under_review
impact_score: 5
sentiment_score: 4
technical_tradeoffs:
- Simplifies linker logic by removing consideration of shared library function sizes,
  potentially improving performance.
- Risk of breaking compilation or runtime behavior on architectures where shared library
  function sizes are relevant for linking.
exchanges:
- author: H.J. Lu
  role: proposer
  position: Submits a patch to ensure function sizes are taken only from regular objects,
    deeming shared library sizes irrelevant at link-time.
  quote: Only use function size defined in regular object since function size defined
    in shared library at link-time is irrelevant.
- author: Alan Modra
  role: reviewer
  position: Expresses doubt about the patch's premise, citing test suite failures
    on MIPS targets as evidence that the assumption might be incorrect.
  quote: 'I''m not completely convinced this is true. If you had run the testsuite
    over a good set of targets, you would have discovered: mipsisa32r2el-elf +FAIL:
    Build pr34585b.so'
- author: H.J. Lu
  role: proposer
  position: Acknowledges the test failures but reiterates the point about irrelevant
    function sizes from shared libraries.
  quote: null
- author: Jan Beulich
  role: reviewer
  position: Agrees with Alan Modra's concern about the patch's assertion and the observed
    test failures.
  quote: null
primer_expert: This patch targets the ELF linker's handling of function sizes, particularly
  when linking objects that might involve shared libraries. The core issue is whether
  the size of a function defined in a shared library (which is determined at runtime
  or during its own build) should influence how the linker calculates or represents
  that function's size when linking against it from another object file. The proposer
  believes it's irrelevant and potentially problematic, while reviewers point to test
  failures on specific architectures like MIPS, suggesting the assumption may not
  hold universally.
primer_glossary:
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for object
    files, executables, and shared libraries on Unix-like systems.
- term: linker
  definition: A program that combines object files and libraries into an executable
    program, resolving external references between them.
- term: shared library
  definition: A library whose code can be shared by multiple programs at runtime,
    loaded dynamically by the operating system.
- term: object file
  definition: A file produced by a compiler or assembler containing machine code and
    data, typically intended to be linked with other object files to form an executable
    or library.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOo0M1A28Kty+TgzdLB4pRG1xnmdYM=RaDWHw3REMCVzvA@mail.gmail.com
bugzilla_url: null
date: '2026-09-10'
is_stub: false
stub_reason: ''
---

This patch modifies the ELF linker to exclusively use function sizes defined in regular object files. It argues that function sizes specified in shared libraries at link-time are irrelevant for the linking process. The change is intended to fix PR ld/34585 and includes updates to test cases for various ELF targets.
