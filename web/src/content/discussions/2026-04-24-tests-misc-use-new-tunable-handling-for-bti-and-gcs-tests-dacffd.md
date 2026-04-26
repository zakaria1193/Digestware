---
project: glibc
subsystem: tests
patch_id: null
tags:
- glibc
- tests
- tunables
- BTI
- GCS
discussion_id: c6dcdf0d-9f9a-419d-970f-ed67640d9e37@linaro.org
source_type: public_inbox
title: 'Re: [PATCH v4 8/8] tests: misc: Use new tunable handling for BTI and GCS tests'
headline: 'tests: misc: Use new tunable handling for BTI and GCS tests'
tldr: Updates BTI and GCS tests to use the new tunable handling mechanism, addressing
  failures caused by ambient GLIBC_TUNABLES.
proposer: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
consensus: Under Review
outcome: ready
sentiment_score: null
technical_tradeoffs:
- Improved test reliability at the cost of increased Makefile complexity.
- Potential for subtle differences in test behavior due to the new tunable handling.
exchanges:
- author: Yury Khrustalev
  role: proposer
  position: Proposes using the new test tunable handling for BTI and GCS tests to
    address failures with ambient `GLIBC_TUNABLES`.
  quote: 'Use new way of handling test tunables for BTI and GCS tests.


    Fix tests that would fail when ambient GLIBC_TUNABLES variable

    is used with the aarch64_gcs tunable.'
- author: Adhemerval Zanella Netto
  role: reviewer
  position: Reviewed and approved the patch.
  quote: 'LGTM, thanks.


    Reviewed-by: Adhemerval Zanella  <adhemerval.zanella@linaro.org>'
primer_expert: This patch modifies the Makefiles for BTI and GCS tests under `sysdeps/unix/sysv/linux/aarch64/`
  to utilize the new `tst-foo-TUNABLES` mechanism.  Glibc tunables control internal
  glibc behavior at runtime.  The `GLIBC_TUNABLES` environment variable can be used
  to set these tunables.  This change ensures that test-specific tunable settings
  are correctly applied, even in the presence of a global `GLIBC_TUNABLES` variable.
  BTI relates to security hardening, while GCS affects memory management.
primer_general: Glibc's behavior can be adjusted at runtime using tunables, which
  are controlled via the `GLIBC_TUNABLES` environment variable. This patch modifies
  how glibc's test suite handles these tunables, specifically for Branch Target Identification
  (BTI) and Global Construction Set (GCS) features. BTI is a security feature that
  prevents code from jumping to unexpected locations, while GCS relates to memory
  allocation strategies. The patch ensures that tests for these features work correctly
  even if system-wide tunables are set, making the test suite more robust.
series_id: 'glibc:tests: misc: use new tunable handling for bti and gcs tests'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/c6dcdf0d-9f9a-419d-970f-ed67640d9e37@linaro.org
bugzilla_url: null
date: '2026-04-24'
---

This patch updates the BTI (Branch Target Identification) and GCS (Global Construction Set) tests to use the newly introduced tunable handling mechanism in glibc. This resolves test failures that occurred when the `GLIBC_TUNABLES` environment variable was set globally. The change ensures that test-specific tunable values override ambient settings, leading to more reliable test execution.
