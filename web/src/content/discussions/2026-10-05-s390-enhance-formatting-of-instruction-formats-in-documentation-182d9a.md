---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- gas
- documentation
- formatting
discussion_id: 20261005153947.363053-52-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 04/46] s390: Enhance formatting of instruction formats in documentation'
headline: 's390: Enhance formatting of instruction formats in documentation'
tldr: Improves the ASCII-art formatting of s390 instruction formats in the documentation
  for better visual consistency and readability.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- The change increases the verbosity of the documentation's ASCII art.
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Enhances the formatting of instruction format diagrams in gas/doc/c-s390.texi
    by using a fixed width per nibble and adding a template.
  quote: null
primer_expert: This patch modifies `gas/doc/c-s390.texi` to improve the visual presentation
  of s390 instruction formats. It standardizes the ASCII-art diagrams by allocating
  4 characters per nibble (4 bits) and adding separators, ensuring that instructions
  of the same byte length have uniform widths and that bit fields are proportionally
  represented. A new template is also included to facilitate the creation and verification
  of these diagrams.
primer_glossary:
- term: nibble
  definition: A unit of 4 bits, equivalent to a hexadecimal digit.
- term: ASCII art
  definition: A graphic design technique that uses computers for presentation and
    consists of pictures pieced together from the 96 printable characters defined
    by the ASCII standard.
- term: instruction format
  definition: The binary structure of a machine instruction, defining the fields for
    opcode, operands, and addressing modes.
series_id: 'binutils:s390: enhance formatting of instruction formats in documentation'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-52-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch refines the formatting of s390 instruction formats within the GNU Assembler's documentation. It standardizes the width of fields in ASCII-art diagrams to use 4 characters per nibble plus a separator, ensuring consistent presentation for instructions of the same byte size. A template is also introduced to aid in drawing and verifying these diagrams.
