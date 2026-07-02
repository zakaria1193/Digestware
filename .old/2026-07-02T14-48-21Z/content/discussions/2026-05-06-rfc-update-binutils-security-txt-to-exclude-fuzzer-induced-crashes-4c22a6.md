---
project: binutils
subsystem: rfc
patch_id: null
tags:
- binutils
- security
- fuzzing
- CVE
discussion_id: 87qzno3ip4.fsf@redhat.com
source_type: public_inbox
title: 'RFC: Updating the Binutils SECURITY.txt document'
headline: 'RFC: Update Binutils SECURITY.txt to Exclude Fuzzer-Induced Crashes'
tldr: Binutils SECURITY.txt will clarify that crashes from fuzzed binaries, without
  a breach of trust boundary, are not security bugs.
proposer: Nick Clifton <nickc@redhat.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Reduces noise from automated fuzzing, but may miss subtle vulnerabilities.
- Requires a clear definition of 'trust boundary' to avoid ambiguity.
exchanges:
- author: Nick Clifton
  role: proposer
  position: Proposes updating the SECURITY.txt document to exclude fuzzer-induced
    crashes, without a breach of trust boundary, from being considered security bugs,
    and to clarify that binutils tools are not intended for network services.
  quote: I want to update the SECURITY.txt document so that it makes clear that bugs
    that rely upon using a fuzzed binary to trigger an illegal memory access should
    not be considered as security bugs.
- author: Jan Beulich
  role: other
  position: Acknowledges the email.
  quote: null
- author: Sam James
  role: other
  position: Acknowledges the email.
  quote: null
primer_expert: This concerns the SECURITY.txt file in binutils, which defines the
  project's security policy. Fuzzing tools like AFL and libFuzzer generate potentially
  malicious inputs to find crashes. By clarifying what constitutes a security bug,
  the project aims to reduce noise from purely fuzzer-induced crashes that don't represent
  real-world exploits.
primer_general: The binutils project provides essential tools for working with binary
  files, such as linkers and assemblers.  SECURITY.txt files are used to communicate
  a project's security policies. Fuzzing is a testing technique that involves feeding
  a program with random or malformed inputs to find bugs. This proposal clarifies
  that crashes caused by fuzzing are not security bugs unless they can be exploited
  to compromise the system.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/87qzno3ip4.fsf@redhat.com
bugzilla_url: null
date: '2026-05-06'
---

Nick Clifton proposes updating the binutils SECURITY.txt document to clarify that crashes caused by fuzzed input, without demonstrating a breach of a trust boundary (e.g., code execution as another user), will not be considered security bugs. They also want to clarify that binutils tools are not intended for network services, so denial-of-service attacks are not relevant. This aims to reduce the number of reported CVEs for fuzzer-induced crashes.
