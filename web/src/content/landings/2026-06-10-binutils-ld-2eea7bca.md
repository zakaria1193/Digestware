---
project: binutils
subsystem: binutils/ld
patch_id: null
tags:
- documentation
- linker
- windows
- portability
commit_hash: 2eea7bca0ced1a25eb47ae586363fe32008b8566
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: The linker documentation consistently describes PE target-only options
tldr: Binutils `ld` documentation now uses consistent phrasing for options specific
  to PE (Windows) targets, clarifying their applicability across architectures.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses documentation consistency within the `ld.texi`
  file for the Binutils `ld` linker. It clarifies the scope of several command-line
  options that are specific to PE (Portable Executable) file format targets. Previously,
  the text might have misleadingly implied i386-only applicability, but with the advent
  of x86_64 and AArch64 PE support, this language has been updated to reflect broader
  applicability within PE-based environments. This is a common task in maintaining
  documentation completeness and accuracy as system support evolves.
primer_general: When you compile a program, a 'linker' (like `ld` in Binutils) combines
  all the compiled pieces into a single executable file. Different operating systems
  and architectures use different executable file formats; Windows, for example, uses
  the PE (Portable Executable) format. This commit updates the documentation for the
  `ld` linker to make it clearer which command-line options are specifically for programs
  targeting Windows. Before this change, some descriptions might have implied that
  these options only worked for older Intel 32-bit systems (i386), which is no longer
  accurate as Windows also runs on 64-bit Intel (x86-64) and ARM (AArch64) processors.
  This update helps developers quickly understand which options apply to their Windows-targeted
  projects, regardless of the specific CPU architecture.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260610233750.187E84BA5435@sourceware.org
date: '2026-06-10'
is_stub: false
---

This commit harmonizes the Binutils `ld` linker documentation by standardizing the language used to describe options exclusive to PE (Portable Executable) targets. Previously, the documentation used inconsistent or outdated phrases like 'i386 PE targeted', which no longer reflected the modern support for PE on architectures like x86_64 and AArch64. The documentation now consistently states that these options are 'specific to PE targeted ports of the linker,' improving clarity for developers working with Windows binaries across different CPU architectures.
