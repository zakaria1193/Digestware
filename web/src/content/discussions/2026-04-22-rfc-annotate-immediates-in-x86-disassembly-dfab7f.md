---
project: binutils
subsystem: rfc
patch_id: null
tags:
- disassembler
- x86
- annotation
- debugging
- reverse engineering
discussion_id: 87fr4njrlb.fsf@redhat.com
source_type: public_inbox
title: 'Re: RFC: Annotate immediates in x86 disassembly'
headline: 'RFC: Annotate immediates in x86 disassembly'
tldr: Proposes a new disassembler option to display symbol names alongside immediate
  values in x86 disassembly output.
proposer: '"H.J. Lu" <hjl.tools@gmail.com>'
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Adds complexity to the disassembler.
- May increase disassembly time due to symbol lookup.
- The option parser accepts imprecise matches for the option name.
exchanges:
- author: Nick Clifton <nickc@redhat.com>
  role: proposer
  position: Proposes a new target-specific option to the x86 and x86_64 disassemblers
    to annotate immediate operands with their corresponding symbol names.
  quote: If enabled immediate operands which match a symbol's value will have the
    name of that symbol displayed alongside them.
- author: H.J. Lu <hjl.tools@gmail.com>
  role: other
  position: Notes that the current implementation doesn't handle shared libraries.
  quote: Should it also handle shared libraries?
- author: Nick Clifton <nickc@redhat.com>
  role: reviewer
  position: Acknowledges the issue and plans to fix it in the next version of the
    patch.
  quote: 'Yes, yes it should. :-)


    I will fix this in the v2 patch.'
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Asks if the option will work from the gdb prompt.
  quote: Will something equivalent then also work from the gdb prompt?
- author: Nick Clifton <nickc@redhat.com>
  role: reviewer
  position: States that the option does not work in gdb.
  quote: 'Actually it appears not. At least not in the very basic test I ran:'
primer_expert: This RFC introduces a new disassembler option, `-M annotate-immediates`,
  which adds symbol annotations to immediate values in x86 disassembly. The implementation
  involves modifying the x86-specific disassembler code to lookup symbols corresponding
  to immediate values.  The feature is disabled for object files due to frequent collisions
  with constants.
primer_general: Disassemblers convert machine code back into human-readable assembly
  code.  This proposal adds a feature to the x86 disassembler that will show the name
  of a variable or function next to immediate values (constants) in the disassembled
  code. This makes it easier to understand what the constants represent, especially
  when they are addresses of functions or global variables.  This feature is targetted
  at developers debugging or reverse-engineering x86 code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOpeVtC4g1yzsiTX7oJLDKe_QS3C7yKoQF+9zZMKWL9Lsg@mail.gmail.com
bugzilla_url: null
date: '2026-04-22'
---

Nick Clifton proposes a new disassembler option `-M annotate-immediates` for x86 and x86_64 architectures.  When enabled, immediate operands in the disassembly output that match a symbol's value will have the symbol name displayed alongside them, which is helpful when inspecting code that loads function addresses. The initial implementation only annotates executables, not object files, because the symbolic addresses in object files too often match small ordinary constants.
