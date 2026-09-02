---
project: gcc
subsystem: tree-ssa-structalias.cc
patch_id: null
tags:
- gcc
- compiler
- analysis
- ipa
- pta
discussion_id: apaWVIe17Ac-Fk7c@localhost.localdomain
source_type: public_inbox
title: 'tree-ssa-structalias.cc: Why do we iterate over fields of a global varinfo'
headline: 'tree-ssa-structalias.cc: Why do we iterate over fields of a global varinfo'
tldr: Investigating IPA PTA code regarding shadow vars and global aggregate fields.
proposer: Filip Kastl <fkastl@suse.cz>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: 7
technical_tradeoffs:
- Potential redundancy in analysis loops.
- Correctness of handling global aggregate field information.
exchanges:
- author: Filip Kastl <fkastl@suse.cz>
  role: proposer
  position: Asks why the IPA PTA code iterates over fields of a global aggregate variable,
    questioning if those fields are not marked as global and if the second loop is
    redundant.
  quote: Are the varinfos that represent fields of a global aggregate variable not
    is_global_var = true? If they were is_global_var = true, then the for loop would
    be redundant, right?
- author: Filip Kastl <fkastl@suse.cz>
  role: contributor
  position: Found a comment in gimple-ssa-pta-constraints.cc that explains why separate
    varinfos for fields might not be created for globals in IPA mode.
  quote: So that would explain why I couldn't see separate varinfos for fields. Indeed,
    if compile the testcase from my previous mail and d
- author: Richard Biener <rguenther@suse.de>
  role: reviewer
  position: Acknowledges Filip's initial question about the IPA PTA code and global
    aggregate fields.
  quote: null
primer_expert: This discussion concerns the Interprocedural Analysis (IPA) Pointer
  Analysis (PTA) component in GCC, specifically within `tree-ssa-structalias.cc`.
  The question revolves around the handling of `varinfo_t` structures representing
  fields of global aggregate variables. The proposer is investigating why the code
  appears to iterate over fields when it might not be necessary if those fields are
  already treated as global.
primer_glossary:
- term: IPA PTA
  definition: Interprocedural Analysis Pointer Analysis. A static analysis technique
    used by compilers to determine which memory locations a pointer can possibly point
    to, considering function calls across the entire program.
- term: varinfo_t
  definition: A data structure likely representing variable information within GCC's
    internal compiler representation, used for tracking variables and their properties
    during analysis.
- term: shadow vars
  definition: In the context of GCC's analysis, shadow variables are auxiliary variables
    used to track information about other variables, often for specific analysis purposes
    like aliasing or point-to analysis.
- term: aggregate variable
  definition: A variable composed of multiple data elements, such as C structs, arrays,
    or unions.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/apaWVIe17Ac-Fk7c@localhost.localdomain
bugzilla_url: null
date: '2026-09-01'
is_stub: false
stub_reason: ''
---

Filip Kastl questions why IPA PTA code in tree-ssa-structalias.cc iterates over fields of a global aggregate variable. He wonders if varinfos representing fields of global aggregates are not marked as global, making the second loop redundant. A subsequent comment from Filip suggests he found an explanation in gimple-ssa-pta-constraints.cc, indicating that subfields for globals are not used in IPA mode.
