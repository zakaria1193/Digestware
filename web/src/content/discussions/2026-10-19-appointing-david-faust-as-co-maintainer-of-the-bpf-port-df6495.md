---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- bpf
- maintainership
- linux kernel
discussion_id: 319d878d-5951-28f6-023a-3ea287a6eb0f@pfeifer.com
source_type: public_inbox
title: Appointing David Faust as co-maintainer of the BPF port
headline: Appointing David Faust as co-maintainer of the BPF port
tldr: David Faust is appointed as the co-maintainer for the GCC BPF port.
proposer: Gerald Pfeifer <gerald@pfeifer.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Gerald Pfeifer <gerald@pfeifer.com>
  role: proposer
  position: Announces the appointment of David Faust as co-maintainer for the GCC
    BPF port and requests the MAINTAINERS file be updated.
  quote: 'It have the pleasure to announce David Faust as co-maintainer of the BPF
    port.


    Thanks for your contributions so far – and happy hacking, David!


    Please go ahead and update MAINTAINERS(.yml) accordingly.'
primer_expert: This announcement formalizes the shared maintenance of the BPF (Berkeley
  Packet Filter) target port in GCC. The BPF port enables GCC to generate code for
  the increasingly popular eBPF virtual machine, used heavily in Linux for networking
  and observability. Formalizing co-maintainership helps streamline development and
  review for this specific target.
primer_glossary:
- term: BPF
  definition: BPF (Berkeley Packet Filter), and more commonly its modern variant eBPF
    (extended BPF), is a technology that allows running sandboxed programs within
    the Linux kernel without changing kernel source code or loading kernel modules.
    It's widely used for networking, security, and observability.
- term: port
  definition: In the context of compilers like GCC, a 'port' refers to the implementation
    of support for a specific target architecture or operating system. This includes
    the necessary code generation, instruction selection, and backend optimization
    passes.
- term: MAINTAINERS file
  definition: A file in a software project's repository that lists individuals responsible
    for maintaining specific subsystems or components. It often includes contact information
    and guides for submission processes.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/319d878d-5951-28f6-023a-3ea287a6eb0f@pfeifer.com
bugzilla_url: null
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

Gerald Pfeifer announces the appointment of David Faust as the co-maintainer for the BPF port within GCC. This appointment is a recognition of Faust's contributions and aims to strengthen the maintenance of the BPF backend. The announcement includes a request for Faust to update the relevant `MAINTAINERS` file.
