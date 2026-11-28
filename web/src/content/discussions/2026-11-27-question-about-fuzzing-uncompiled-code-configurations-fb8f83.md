---
project: binutils
subsystem: binutils
patch_id: null
tags:
- fuzzing
- binutils
- testing
- configuration
discussion_id: SJ2PR01MB8258EA2C5A9586C2EC022D56FC412@SJ2PR01MB8258.prod.exchangelabs.com
source_type: public_inbox
title: Should code that the fuzz build does not compile be fuzzed?
headline: Question about fuzzing uncompiled code configurations
tldr: A researcher asks whether binutils code compiled under different configurations
  should be fuzzed, even if not part of the default OSS-Fuzz build.
proposer: '"Ahmed, Meah Tahmeed" <Meah.Ahmed@UTDallas.edu>'
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Meah.Ahmed@UTDallas.edu
  role: proposer
  position: Asks if code compiled under configurations not used by OSS-Fuzz should
    be fuzzed.
  quote: '1. Do you think this code should be fuzzed, or is fuzzing the current configuration
    enough?

    2. Is this code tested in other ways that you consider sufficient?'
primer_expert: This inquiry delves into the scope of fuzzing for the binutils project,
  specifically concerning code paths that are not exercised by the default OSS-Fuzz
  configuration (Linux x86-64, --enable-targets=all). The question is whether code
  unique to other build targets (e.g., Windows, AIX, HP-UX, 32-bit) should also be
  subjected to fuzzing, and if current testing methodologies for these configurations
  are sufficient.
primer_glossary:
- term: fuzzing
  definition: An automated software testing technique that involves providing invalid,
    unexpected, or random data as input to a program to find bugs and vulnerabilities.
- term: OSS-Fuzz
  definition: A free fuzzing-as-a-service for open-source projects, provided by Google,
    that helps developers find bugs.
- term: BFD
  definition: The Binary File Descriptor library, used by binutils to support various
    object file formats.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/SJ2PR01MB8258EA2C5A9586C2EC022D56FC412@SJ2PR01MB8258.prod.exchangelabs.com
bugzilla_url: null
date: '2026-11-27'
is_stub: false
stub_reason: ''
---

A PhD student is investigating how build configurations impact fuzzing effectiveness for binutils. They observe that OSS-Fuzz only targets a specific configuration, leaving code compiled under other settings (e.g., Windows-host, 32-bit BFD) unfuzzed. The student seeks community input on whether these unfuzzed configurations warrant fuzzing and if they are adequately tested by other means.
