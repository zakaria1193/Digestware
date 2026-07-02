---
project: binutils
subsystem: binutils
patch_id: null
tags:
- x86
- avx10
- binutils
- instruction set
- documentation
discussion_id: IA4PR11MB900937DF7F4B109033884985ECE82@IA4PR11MB9009.namprd11.prod.outlook.com
source_type: public_inbox
title: 'RE: [PATCH v1 1/2] Support AVX10_V2_AUX instructions'
headline: Support AVX10_V2_AUX instructions
tldr: Confirms that a dedicated revision of the AVX10 spec for AVX10_V2_AUX is not
  currently planned, but may happen in the future.
proposer: Jiang, Haochen <haochen.jiang@intel.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Decision not to create a dedicated AVX10 spec revision at this time, relying on
  existing joint documentation.
- Potential future effort to create a dedicated spec if needed.
exchanges:
- author: Jiang, Haochen <haochen.jiang@intel.com>
  role: other
  position: Responds to an inquiry about a dedicated AVX10 spec revision, stating
    it's not currently planned but possible in the future.
  quote: null
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Asks whether a more dedicated revision of the AVX10 specification, specifically
    covering 10.2-aux, is planned.
  quote: null
- author: Ganesh Gopalasubramanian
  role: contributor
  position: Provides clarification on AVX10 instructions, noting that AVX10_V1_AUX
    are part of AVX10.2 (under a new CPUID bit) and AVX10_V2_AUX are new x86 instructions,
    referencing the ACE Specification v1.15.
  quote: null
primer_expert: This thread discusses the binutils support for x86 AVX10 extensions,
  specifically AVX10_V2_AUX. A reviewer inquired about the availability of a dedicated
  specification revision for these instructions. The proposer clarifies that while
  not currently planned due to existing joint documentation, a future revision is
  possible, aligning with the inclusion of AVX10_V1_AUX in the broader AVX10 spec.
primer_general: This conversation is about the documentation for new x86 processor
  instructions, specifically the AVX10_V2_AUX extensions. A question was raised about
  whether Intel plans to release a dedicated manual or update for these new instructions.
  The response indicates that while a specific manual is not currently planned, it
  might be developed in the future. This is relevant for developers who need to understand
  and utilize these advanced instructions for high-performance computing.
series_id: binutils:support avx10_v2_aux instructions
series_role: reply
series_parts:
- title: Support AVX10_V2_AUX instructions
  url: https://inbox.sourceware.org/binutils/c8532d49-3a19-4412-9177-e2b7fa535249@suse.com
  n: 1
  total: 2
- title: Support AVX10_V2_AUX instructions
  url: https://inbox.sourceware.org/binutils/36607945-e0ac-4293-84eb-54229815a24e@suse.com
  n: 1
  total: 2
- title: Support AVX10_V2_AUX instructions
  url: https://inbox.sourceware.org/binutils/ce0d35ec-b25f-436e-953b-207861f57c52@suse.com
  n: 1
  total: 2
- title: Support AVX10_V2_AUX instructions
  url: https://inbox.sourceware.org/binutils/a6c192c9-4e8e-417d-8473-0db71ba1c0d1@suse.com
  n: 1
  total: 2
- title: Support AVX10_V2_AUX instructions
  url: https://inbox.sourceware.org/binutils/IA4PR11MB90099AD311BE8AAFACDF3873ECE82@IA4PR11MB9009.namprd11.prod.outlook.com
  n: 1
  total: 2
url: https://inbox.sourceware.org/binutils/IA4PR11MB900937DF7F4B109033884985ECE82@IA4PR11MB9009.namprd11.prod.outlook.com
bugzilla_url: null
date: '2026-06-29'
is_stub: false
stub_reason: ''
---

This email addresses a question about a potential dedicated revision of the AVX10 specification to cover AVX10_V2_AUX instructions. The sender confirms that such a revision is not currently planned, as joint documentation already exists. However, they express that it might happen in the future, especially considering that AVX10_V1_AUX is included in the main AVX10 specification.
