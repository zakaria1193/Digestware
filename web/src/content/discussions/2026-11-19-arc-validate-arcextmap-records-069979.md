---
project: binutils
subsystem: arc
patch_id: null
tags:
- arc
- security
- vulnerability
- parsing
- objdump
discussion_id: CAO9RCZXedX9Q51GVYf0X+JOtSOegkuPZdC3HLuZDo9qOxF29sQ@mail.gmail.com
source_type: public_inbox
title: '[PATCH] arc: validate .arcextmap records'
headline: 'ARC: Validate .arcextmap records'
tldr: Adds validation for .arcextmap records in the ARC toolchain to prevent out-of-bounds
  memory access vulnerabilities.
proposer: mustafa <mustafa@medios.digiscrypt.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Improves security and stability by adding necessary validation checks.
- Slight performance overhead due to additional checks during section parsing.
exchanges:
- author: mustafa
  role: proposer
  position: Proposes validating records in the `.arcextmap` section of ARC object
    files to prevent out-of-bounds memory access.
  quote: 'create_map in arc-ext.c parses the .arcextmap section of an object.

    Each record starts with its length and a type byte, but neither is

    used for anything: the register number and the condition code are

    used as array indexes without a range check, and the names are

    copied with xstrdup, which does not stop at the end of the record or

    of the section.


    For a crafted section this writes outside coreReg…'
primer_expert: This patch targets `opcodes/arc-ext.c` and specifically the `create_map`
  function, which parses the `.arcextmap` section in ARC object files. The vulnerability
  lies in the unchecked use of `length` and `type` bytes within each record, leading
  to out-of-bounds access on `coreRegisters` and `condCodes` arrays, and unbounded
  string copies with `xstrdup`. The proposed fix adds boundary checks for record length,
  register/condition code indices, and uses `xstrndup` to safely copy names within
  the record's bounds, mitigating a UBSan-detected vulnerability.
primer_glossary:
- term: .arcextmap
  definition: A custom section in ARC object files that stores extended instruction
    mapping information.
- term: out-of-bounds access
  definition: An error condition where a program attempts to read or write memory
    outside the allocated buffer or array boundaries.
- term: UBSan
  definition: Undefined Behavior Sanitizer, a runtime instrumentation tool that detects
    various kinds of undefined behavior in C/C++ code.
- term: xstrdup
  definition: A string duplication function that allocates memory and copies a string.
    It is potentially unsafe if the source string is not properly null-terminated
    or if the destination buffer is not checked.
- term: xstrndup
  definition: A safer version of `strdup` that duplicates at most a specified number
    of characters from the source string.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAO9RCZXedX9Q51GVYf0X+JOtSOegkuPZdC3HLuZDo9qOxF29sQ@mail.gmail.com
bugzilla_url: null
date: '2026-11-19'
is_stub: false
stub_reason: ''
---

This patch addresses a security vulnerability in the ARC toolchain's parsing of the `.arcextmap` section. The current implementation in `arc-ext.c` does not validate record lengths or indices, allowing crafted input to cause out-of-bounds reads and writes. The fix introduces checks for record validity, register numbers, condition codes, and safely copies string data, preventing potential crashes and security exploits.
