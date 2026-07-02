---
project: gcc
subsystem: gcc/gfortran
patch_id: null
tags:
- gfortran
- diagnostics
- Fortran-standard
- terminology
- user-experience
discussion_id: d47c0506-2ef0-4723-8e92-7fed34224f4e@netcologne.de
source_type: public_inbox
title: Terminology in Fortran error messages and options
headline: Proposes aligning gfortran error messages with Fortran standard terminology
tldr: Thomas Koenig suggests updating gfortran's error messages and options to use
  standard Fortran terminology, particularly concerning variable definition status.
proposer: Thomas Koenig <tkoenig@netcologne.de>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Improvement of user experience and adherence to standards versus the effort required
  to identify and change all non-standard terminology.
- Potential for minor disruption to build systems or scripts that parse existing compiler
  output if message formats change too drastically.
exchanges:
- author: Thomas Koenig <tkoenig@netcologne.de>
  role: proposer
  position: Proposes adopting Fortran standard terminology in gfortran error messages
    and compiler options for better consistency.
  quote: gfortran error messages are sometimes at odds with Fortran standard terminology.
    For example, -Wuninitialized warns about automatic-storage variables which do
    not have a value assigned, and the error messages also are "used uninitialized".
    In Fortran standard terminology, on the other hand, a variable becomes "defined"
    or "undefined", so a Fortran compiler should strive to use that terminology.
primer_expert: This proposal targets the user-facing aspects of the gfortran front-end,
  specifically the wording used in diagnostic messages and compiler options. The core
  issue is the divergence between the internal representation and common programming
  parlance (e.g., "uninitialized") versus the precise terminology defined by the Fortran
  standard (e.g., "defined"/'undefined' status for variables). This impacts the `gcc/fortran/diagnostics.cc`
  and potentially other files responsible for emitting warnings and errors. Changes
  would require careful consideration of existing `gfc_options` and how they map to
  d…
primer_general: This discussion is about making the GCC Fortran compiler (gfortran)
  speak the same language as the official Fortran standard. When you write a program
  and there's a problem, the compiler gives you an error message. Sometimes, these
  messages use general programming terms instead of the specific, precise terms defined
  in the Fortran language standard. For instance, instead of saying a variable is
  'uninitialized,' the Fortran standard might say it's 'undefined.' This proposal
  suggests that gfortran should consistently use the official Fortran terms in its
  error messages and compiler options. This would make gfortran's feedback clearer
  and more accurate for Fortran programmers who are familiar with the standard, reducing
  confusion and making it easier to fix problems in their code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/d47c0506-2ef0-4723-8e92-7fed34224f4e@netcologne.de
bugzilla_url: null
date: '2026-06-06'
is_stub: false
---

Thomas Koenig proposes a cleanup effort for gfortran's error messages and compiler options to align them with the official Fortran standard terminology. The current messages, such as those related to uninitialized variables, often use common programming terms rather than the Fortran standard's 'defined' or 'undefined' status. The proposal suggests consistently using standard terminology for new features and gradually updating existing ones, which would improve clarity and consistency for Fortran developers.
