---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- static analysis
- benchmarking
- testing
discussion_id: 0824b5fef61bc82d67908e5563a77c1288d09dad.camel@redhat.com
source_type: public_inbox
title: 'New support repository: gcc-analyzer-benchmarks'
headline: 'New support repository: gcc-analyzer-benchmarks'
tldr: A new repository 'gcc-analyzer-benchmarks' is created to provide a harness for
  testing GCC's static analyzer (-fanalyzer) with various third-party benchmarking…
proposer: David Malcolm <dmalcolm@redhat.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Separates benchmarking infrastructure from the main GCC repository, potentially
  allowing for faster iteration on the harness itself but requiring users to clone
  an additional repository.
exchanges:
- author: David Malcolm <dmalcolm@redhat.com>
  role: proposer
  position: Introduces a new repository containing a benchmarking harness ('gab')
    for GCC's static analyzer (-fanalyzer).
  quote: "So I've created a new harness for using them for testing GCC's -fanalyzer\
    \ option:\n  https://github.com/davidmalcolm/gcc-analyzer-benchmarks\nrunning\
    \ them, generating scores, diffing two runs, etc.  The tool is\ncalled \"gab\"\
    :"
primer_expert: This is about a new external repository, 'gcc-analyzer-benchmarks',
  which provides a standardized harness ('gab') for evaluating GCC's static analysis
  pass (-fanalyzer). It aggregates and runs various third-party benchmark suites,
  aiming to simplify the process of testing the analyzer's effectiveness across different
  codebases and configurations.
primer_glossary:
- term: -fanalyzer
  definition: A GCC compiler flag that enables the built-in static analyzer, which
    attempts to find bugs in code without executing it.
- term: static analysis
  definition: The analysis of computer software that is performed non-dynamically,
    i.e., without actually executing the program. Static analyzers analyze code to
    find potential bugs, security vulnerabilities, and style violations.
- term: benchmarking suite
  definition: A collection of programs or test cases designed to evaluate the performance
    or correctness of a system or tool, in this case, a static analyzer.
- term: harness
  definition: A framework or set of tools used to automate the testing and evaluation
    of software components.
- term: CWE
  definition: Common Weakness Enumeration; a list of software security weakness types
    that can be used as a common language for describing security weaknesses in software.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/0824b5fef61bc82d67908e5563a77c1288d09dad.camel@redhat.com
bugzilla_url: null
date: '2026-11-23'
is_stub: false
stub_reason: ''
---

David Malcolm has created a new, standalone repository named 'gcc-analyzer-benchmarks' to serve as a harness for testing GCC's static analyzer, '-fanalyzer'. This tool, 'gab', aims to standardize the process of running third-party benchmarking suites, generating scores, and comparing results. It addresses the current inconsistencies in how these suites express ground truth, build flags, and dependencies.
