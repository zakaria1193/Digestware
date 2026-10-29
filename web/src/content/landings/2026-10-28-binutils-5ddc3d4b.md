---
project: binutils
subsystem: binutils
patch_id: null
tags:
- disassembler
- tilepro
- tilegx
- bugfix
- undefined behavior
commit_hash: 5ddc3d4b1ad5029fad8eb10b040da099a4f9936f
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Undefined shift in print_insn_tilepro
tldr: Change integer types to unsigned for TilePro and TileGX instruction decoding
  to avoid undefined behavior with shifted values.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit sanitizes the handling of operand values in the TilePro
  and TileGX disassemblers. The ``operand_values`` field in ``struct tilepro_decoded_instruction``
  and related fields in ``struct tilegx_decoded_instruction`` were previously signed
  ``int`` or ``long long``. If the most significant bit was set, left-shifting this
  value invoked undefined behavior, potentially triggering UBSan errors. Changing
  these fields to ``unsigned int`` resolves this by ensuring that shifts on values
  with the MSB set are well-defined.
primer_glossary:
- term: TilePro
  definition: A family of microprocessors from TileData, Inc., known for their multi-core
    architecture. Binutils includes disassemblers for these processors.
- term: TileGX
  definition: A variant of the TilePro architecture, also with multi-core capabilities.
    Binutils supports its instruction set decoding.
- term: UBSan
  definition: Undefined Behavior Sanitizer. A runtime instrumentation tool that detects
    undefined behavior in C/C++ code, often signalling potential bugs or security
    vulnerabilities.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261028223609.2CF6C4BA2E26@sourceware.org
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

The TilePro and TileGX instruction decoders used signed integers for operand values, which could lead to undefined behavior if the top bit was set. This change modifies the relevant fields to use unsigned integers, preventing potential crashes or incorrect behavior when shifting these values. This aligns with how the values are stored and is generally safer for bitwise operations.
