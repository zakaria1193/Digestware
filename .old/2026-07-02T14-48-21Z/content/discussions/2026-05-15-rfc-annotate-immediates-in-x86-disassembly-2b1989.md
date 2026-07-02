---
project: binutils
subsystem: rfc
patch_id: null
tags:
- binutils
- testsuite
- x86-64
- Tcl
- build fix
discussion_id: 25dd2e82-33ca-465a-aa7c-052c77b7114e@suse.com
source_type: public_inbox
title: 'Re: RFC: Annotate immediates in x86 disassembly'
headline: 'RFC: Annotate immediates in x86 disassembly'
tldr: Fixes a testsuite error in x86-64 mode by defining the `exe` variable.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Adds a variable definition to a test script to resolve an error.
exchanges:
- author: Nick Clifton
  role: other
  position: Reports an error in the testsuite due to an undefined `exe` variable.
  quote: 'For me the use of the global "exe" in test_objdump_M_annotate is a problem
    when running the testsuite with RUNTESTFLAGS=x86-64.exp:

    ERROR: can''t read "exe": no such variable'
- author: Maciej W. Rozycki
  role: contributor
  position: Suggests setting the `exe` variable using `[exeext]`.
  quote: 'You just need:

    set exe [exeext]'
- author: Nick Clifton
  role: other
  position: Confirms the suggested solution works.
  quote: 'Thanks Maciej.


    I am happy with either solution.  Jan - can you confirm that one or

    both work, and do you have a preference ?'
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Confirms the solution and indicates the patch will be committed.
  quote: 'Maciej''s works and is in line with what some parent dir *.exp also do.

    I guess I''ll commit the patch below right away.'
primer_expert: The binutils testsuite uses `.exp` files to define tests.  These files
  use Tcl scripting.  The `x86-64/x86-64.exp` script runs tests specific to the x86-64
  architecture.  The `exeext` variable provides the executable extension for the host
  system.  This patch ensures that the `exe` variable is defined correctly in the
  test script.
primer_general: Binutils is a collection of tools for working with binary files, including
  assemblers, linkers, and debuggers. Its functionality is validated by a testsuite.
  The testsuite uses scripts to automate the execution of tests and compare the results
  against expected outputs.  This patch addresses a specific error related to the
  executable extension within the x86-64 test environment, ensuring the testsuite
  runs correctly.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/25dd2e82-33ca-465a-aa7c-052c77b7114e@suse.com
bugzilla_url: null
date: '2026-05-15'
is_stub: false
---

This patch addresses an error encountered when running the binutils testsuite in x86-64 mode. The error arises because the `exe` variable, representing the executable extension, is not defined in the `x86-64.exp` test script. The patch resolves this by explicitly setting `exe` using `[exeext]`, ensuring the testsuite functions correctly in x86-64 environments. The change restores the functionality of the testsuite.
