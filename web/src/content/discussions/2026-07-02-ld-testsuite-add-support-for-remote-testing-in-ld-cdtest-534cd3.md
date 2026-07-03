---
project: binutils
subsystem: ld/testsuite
patch_id: null
tags:
- binutils
- linker
- testsuite
- remote testing
- cross-compilation
discussion_id: CAJ307EhRepQURcsfUB_xUQ=_D68oVDXwTtQG82SxjY7Q1wTGXw@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH v2] ld/testsuite: add support for remote testing in ld-cdtest'
headline: 'ld/testsuite: add support for remote testing in ld-cdtest'
tldr: Patch adds remote execution capabilities to ld-cdtest, enabling tests on both
  native and cross-compiled targets.
proposer: Clément Chigot <chigot@adacore.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Enables broader test coverage by supporting remote execution.
- Introduces a dependency on the `remote_load` functionality, which might require
  specific test environment setup.
exchanges:
- author: Clément Chigot <chigot@adacore.com>
  role: proposer
  position: Submits a patched version of the `ld-cdtest` testsuite that uses `remote_load`
    to enable remote test execution.
  quote: Gentle ping to Maciej.
- author: Maciej W. Rozycki <macro@orcam.me.uk>
  role: reviewer
  position: Confirms the patch works correctly on native and remote targets but notes
    a minor issue with `remote_load` usage and output handling.
  quote: I can see this works correctly here with native `powerpc64le-linux-gnu' system
    as well as remote `mips-linux-gnu' cross target, enabling the tests in the latter
    case.  I have looked through the change and it seems good to me except for one
    nit across two places; see below.
primer_expert: The `ld-cdtest` is a Tcl-based test harness within the binutils ld/testsuite
  designed to verify the linker's behavior. This patch refactors the test execution
  logic to use `remote_load`, a Tcl command likely provided by the test infrastructure,
  to run the `cdtest` program on the target system (either native or remote). This
  enables testing cross-linker configurations more effectively and reliably, moving
  away from direct `exec` calls which could be fragile.
primer_glossary:
- term: ld-cdtest
  definition: A test within the binutils linker testsuite (`ld/testsuite`) that likely
    tests specific linker features or command-line options related to code distribution
    or compilation drivers.
- term: remote_load
  definition: A Tcl command, presumably part of the binutils testing framework, used
    to load and execute a program on a remote target system.
- term: cross-compiled target
  definition: A target system for which code is compiled on a different host system
    and architecture. For example, compiling code for an ARM processor on an x86-based
    Linux machine.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAJ307EhRepQURcsfUB_xUQ=_D68oVDXwTtQG82SxjY7Q1wTGXw@mail.gmail.com
bugzilla_url: null
date: '2026-07-02'
is_stub: false
stub_reason: ''
---

This patch revises the `ld-cdtest` testsuite to support remote execution, allowing tests to run on both native and cross-compiled targets. Maciej Rozycki has reviewed the changes, confirming their correctness on `powerpc64le-linux-gnu` (native) and `mips-linux-gnu` (remote) cross targets. He identifies a minor nitpick regarding the use of 'remote_load' and output handling that needs to be addressed.
