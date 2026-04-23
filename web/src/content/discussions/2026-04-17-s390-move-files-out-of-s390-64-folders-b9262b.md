---
project: glibc
subsystem: s390
patch_id: null
tags:
- s390
- code organization
- refactoring
discussion_id: 1cf5a935-4e7a-4027-a7c8-514d4937d7ea@linaro.org
source_type: public_inbox
title: 'Re: [PATCH 4/5] s390: Move files out of s390-64 folders'
headline: 's390: Move files out of s390-64 folders'
tldr: This patch moves files from the s390/s390-64 subdirectory to s390/, merging
  them when necessary.
stakes: Code reorganization improves maintainability and reduces redundancy by removing
  an unnecessary directory level.
proposer: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
consensus: Ready to Land
outcome: ready
sentiment_score: 9
sentiment_rationale: The patch is addressing code organization and has received positive
  feedback, suggesting it's close to being accepted.
series_id: 'glibc:s390: move files out of s390-64 folders'
series_role: reply
series_parts:
- title: 's390: Move files out of s390-64 folders'
  url: https://inbox.sourceware.org/libc-alpha/4251a039-b97c-4560-b89b-208ba282b96f@linux.ibm.com
  n: 4
  total: 5
url: https://inbox.sourceware.org/libc-alpha/1cf5a935-4e7a-4027-a7c8-514d4937d7ea@linaro.org
bugzilla_url: null
date: '2026-04-17'
---

This patch moves files out of the s390/s390-64 directory and merges them into the s390/ directory. The sysdeps/s390/preconfigure.ac file is updated to reflect the removal of the s390-64 subdirectory.  A question was raised about some compiler flags, which will be investigated in a separate patch.
