---
project: binutils
subsystem: binutils/gas
patch_id: null
tags:
- testsuite
- gas
- i386
- relocation
commit_hash: 7a40b4d6306587e19850afc65170634375c37c2c
source_type: public_inbox
author: '"H.J. Lu" <hjl@sourceware.org>'
headline: 'binutils/gas: Make PLT test more robust to offset changes'
tldr: Gas test for PLT relocations no longer hard-codes the offset, making it resilient
  to future changes.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies `testsuite/gas/i386/plt.d` to replace the hardcoded
  offset `0xd4` in the expected output for relocation sections with a regex `0x[0-9a-f]+`.
  This change addresses PR gas/34423 by making the test less brittle to variations
  in the offset calculation within the PLT.
primer_glossary:
- term: PLT
  definition: Procedure Linkage Table. A table used by dynamically linked executables
    to resolve external function calls indirectly, especially when dealing with Position
    Independent Code (PIC).
- term: relocation
  definition: Information in an object file that describes how to modify code or data
    after linking. For example, it might specify that a certain constant needs to
    be replaced by the actual address of a symbol.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260729225231.AD8784BB3BE8@sourceware.org
date: '2026-07-29'
is_stub: true
stub_reason: low_score
---

The gas testsuite for i386 PLT (Procedure Linkage Table) relocations has been updated to improve robustness. Instead of hard-coding the exact offset of the relocation section in the `.rodata` section, the test now uses a regular expression to match any hexadecimal offset. This prevents the test from failing due to minor, non-functional changes in the linker's output.
