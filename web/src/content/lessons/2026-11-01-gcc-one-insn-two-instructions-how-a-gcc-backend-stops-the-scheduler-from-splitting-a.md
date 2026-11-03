---
project: gcc
subsystem: rs6000
patch_id: null
tags:
- instruction-fusion
- scheduling
- machine-description
- powerpc
- toc
lesson_id: gcc:2026-W44
commit_hash: 9833d3d84694c57e10af82f5284c9d3e03d15d91
source_type: github
headline: 'One insn, two instructions: how a GCC backend stops the scheduler from
  splitting a pair the CPU wants to fuse'
hook: POWER10 fuses addis+addi into one operation, but only when the two sit next
  to each other. GCC's scheduler kept separating them. The fix shows how GCC backends
  keep instructions together.
tldr: On POWER10-fusion targets, rs6000 now emits large-TOC address loads as one RTL
  insn that prints addis and addi together, so the scheduler cannot pull them apar…
concept: The scheduler reorders insns, not assembler lines. A define_insn whose output
  template prints several instructions becomes one unit the scheduler cannot split.
  Backends use this when the hardware rewards adjacency, and they switch off the old
  split patterns behind the same flag.
prerequisites:
- what RTL is and that backends describe it in .md files
- what an instruction scheduler does
- PowerPC addis/addi and 16-bit immediates
- position-independent data access through a table pointer
- what a code model (small vs. large) means
code_tour:
- path: gcc/config/rs6000/rs6000.md
  symbol: '*largetocp10'
  lines: 11681-11688
  why: 'The ELF combined pattern: one set of an UNSPEC_TOCREL whose output template
    prints addis and addi joined by \;.'
- path: gcc/config/rs6000/rs6000.md
  symbol: '*largetocp10_plus_aix<mode>'
  lines: 11710-11719
  why: The XCOFF symbol-plus-constant form, which joins its two instructions with
    a plain ';' and uses la for the low half.
- path: gcc/config/rs6000/rs6000.md
  symbol: '*largetoc_high'
  lines: 11621-11629
  why: The old high-half pattern modelled as (high (unspec ... UNSPEC_TOCREL)), now
    disabled under !TARGET_P10_FUSION.
- path: gcc/config/rs6000/rs6000.md
  symbol: '*largetoc_low'
  lines: 11665-11671
  why: The old lo_sum low-half pattern that emitted a separate addi, the second insn
    the scheduler could move away from the first.
- path: gcc/config/rs6000/rs6000.md
  symbol: '*tocref<mode>'
  lines: 11722-11731
  why: A define_insn_and_split whose post-reload split produces the same high/lo_sum
    pair, so it is also disabled on fusion targets.
- path: gcc/config/rs6000/rs6000-cpus.def
  symbol: OTHER_FUSION_MASKS
  lines: 57-59
  why: Shows how earlier (P8) fusion options are defined as ISA option masks, for
    comparison with the P10 flag.
takeaways:
- The scheduler reorders RTL insns, not assembler lines; only a single insn guarantees
  two instructions stay adjacent.
- A define_insn whose output template contains several instructions separated by \;
  is the standard way to make a sequence atomic to later passes.
- Combining instructions into one insn hides the intermediate value from every RTL
  pass, which is both the purpose and the cost.
- When a new pattern overlaps an old one, guard them with mirrored conditions (FLAG
  / !FLAG) so codegen for other targets does not change.
- -dp lets a test check which insn pattern GCC chose, which is not the same as checking
  runtime behaviour.
further_reading:
- title: 'rs6000: Add POWER10 wide-immediate fusion patterns [PR108018] (commit)'
  url: https://github.com/gcc-mirror/gcc/commit/9833d3d84694c57e10af82f5284c9d3e03d15d91
primer_expert: In rs6000.md, large-cmodel TOC addresses were built from `*largetoc_high*`
  (high of UNSPEC_TOCREL → addis) plus `*largetoc_low*` (lo_sum → addi/la), and the
  `*tocref<mode>` post-reload split produced the same pair. Under `TARGET_P10_FUSION`
  these are disabled and `*largetocp10*` emits both halves from one insn, so sched2
  can't separate them. This is separate from the fusion.md peepholes. Where the flag
  is defined isn't established, but the tests suggest it follows -mtune.
primer_glossary:
- term: TOC
  definition: 'Table of Contents: the PowerPC ELF/AIX area holding addresses and small
    data, reached from a dedicated base register (r2). Code finds globals through
    offsets from that register.'
- term: code model
  definition: A compiler setting (-mcmodel) that bounds how far code may reach data.
    On rs6000, CMODEL_SMALL assumes TOC offsets fit in 16 bits. Larger models build
    the offset in two halves.
- term: addis / addi / la
  definition: PowerPC add instructions with a 16-bit immediate. addis shifts its immediate
    left by 16 bits, so it adds a high half. addi and la add a low half.
- term: '@toc@ha / @toc@l'
  definition: Relocation operators that ask for the high-adjusted and low 16 bits
    of a symbol's TOC-relative offset. 'High-adjusted' compensates for the low half
    being sign-extended.
- term: XCOFF
  definition: The object file format used on AIX. GCC tests it with TARGET_XCOFF,
    and its assembler syntax for address halves (@u, @l) differs from ELF's.
- term: instruction fusion
  definition: A CPU feature that executes certain adjacent instruction pairs as a
    single internal operation. It usually requires the two instructions to be next
    to each other.
- term: RTL
  definition: Register Transfer Language, GCC's low-level intermediate representation.
    Backend patterns in .md files match RTL insns and say how to print them as assembly.
- term: insn
  definition: One RTL instruction object. Passes such as the scheduler and register
    allocator treat it as an indivisible unit, even if it prints as several machine
    instructions.
- term: define_insn
  definition: A machine-description entry that gives an RTL pattern, a condition saying
    when it is enabled, and an output template for printing it as assembly.
- term: define_insn_and_split
  definition: A define_insn that can also be rewritten (split) into several simpler
    insns once a split condition holds, often after reload.
landing_slug: 2026-10-26-rs6000-9833d3d8
url: https://github.com/gcc-mirror/gcc/commit/9833d3d84694c57e10af82f5284c9d3e03d15d91
week_start: '2026-10-26'
week_end: '2026-11-01'
commit_date: '2026-10-26'
date: '2026-11-01'
is_stub: false
stub_reason: ''
---

## Background: building a TOC address in two halves

On PowerPC ELF and AIX/XCOFF, a function reaches global data through the TOC (Table of Contents), a data area addressed from a dedicated base register. PowerPC immediates are 16 bits wide. Under a large code model, where `TARGET_CMODEL != CMODEL_SMALL`, a TOC-relative offset can be too big for one displacement. The compiler therefore builds the address in two steps: `addis` adds the high-adjusted half of the offset to the TOC base, and `addi` (or `la` on XCOFF) adds the low half.

On ELF the pair looks like this:

```
addis rD, r2, sym@toc@ha
addi  rD, rD, sym@toc@l
```

`@toc@ha` and `@toc@l` are relocation operators. They ask the assembler and linker for the high-adjusted and low 16 bits of the symbol's TOC-relative offset. XCOFF spells the same idea `sym@u(reg)` and `sym@l(reg)`.

POWER10 can fuse this pair, executing the two instructions as one internal operation. The catch is that fusion depends on the two instructions sitting next to each other in the instruction stream. Anything the compiler places between them cancels it.

## The mechanism: why two patterns invite the scheduler to interfere

Before this commit, `gcc/config/rs6000/rs6000.md` described the sequence as two independent RTL insns. The high half is a `(set (high ...))` around an `UNSPEC_TOCREL`:

```
(define_insn "*largetoc_high"
  [(set (match_operand:DI 0 "gpc_reg_operand" "=b*r")
        (high:DI
	  (unspec [(match_operand:DI 1 "" "")
		   (match_operand:DI 2 "gpc_reg_operand" "b")]
		  UNSPEC_TOCREL)))]
   ...
   "addis %0,%2,%1@toc@ha")
```

The low half is a separate `lo_sum` insn that prints `addi %0,%1,%2@l` (ELF) or `la %0,%2@l(%1)` (XCOFF). The `_plus` variants do the same for symbol-plus-constant addresses. The `*tocref<mode>` `define_insn_and_split` produces the same pair late. After reload, it splits a TOC reference into `(set (match_dup 0) (high:P (match_dup 1)))` followed by `(set (match_dup 0) (lo_sum:P (match_dup 0) (match_dup 1)))`.

The instruction scheduler works on insns. It sees two separate insns joined only by a data dependence, so it may place unrelated work between them to shorten a dependency chain. The commit message says this is what happened: "the scheduler was breaking these pairs apart to optimize for dependency chains, losing the fusion benefit." The schedule was legal, but it cancelled the fusion.

## The change: a "fake" insn that prints both halves

The commit adds four patterns, all enabled only under `TARGET_P10_FUSION`: `*largetocp10`, `*largetocp10_aix<mode>`, `*largetocp10_plus` and `*largetocp10_plus_aix<mode>`. Each one describes the whole address computation as a single `set`. There is no `high` and no `lo_sum`, just the `UNSPEC_TOCREL` value (plus a constant in the `_plus` forms). The output template prints both instructions:

```
(define_insn "*largetocp10"
  [(set (match_operand:DI 0 "gpc_reg_operand" "=b")
	(unspec [(match_operand:DI 1 "" "")
		 (match_operand:DI 2 "gpc_reg_operand" "b")]
		UNSPEC_TOCREL))]
   "TARGET_P10_FUSION
    && TARGET_ELF && TARGET_CMODEL != CMODEL_SMALL"
   "addis %0,%2,%1@toc@ha\;addi %0,%0,%1@toc@l")
```

In an output template, `\;` separates instructions within one insn. The rest of the compiler sees one insn with one destination. Only final assembly output sees two machine instructions. Because the scheduler cannot reorder inside an insn, the `addis` and `addi` always come out back to back. The commit message calls these "fake" instructions: as far as the compiler's internals are concerned, the pair is one opaque operation.

The second half of the change stops the old patterns from competing. Every `*largetoc_high*` and `*largetoc_low*` pattern gains `!TARGET_P10_FUSION` in its condition, and so does `*tocref<mode>`. On a fusion target the two-insn forms can no longer match, so the combined form is the only option. On other targets the conditions keep the old patterns enabled and the new ones disabled, so their code generation does not change.

The XCOFF templates are less uniform than the ELF ones. `*largetoc_plus_aix<mode>` joins its two instructions with a plain `;` instead of `\;`. The dossier does not explain why the XCOFF operand order and separator differ, so treat those details as written, not as a deliberate design.

## Consequences: what this teaches outside rs6000

The general lesson: the unit of scheduling is the RTL insn, not the instruction. If the hardware rewards adjacency, through fusion or anything else, then two insns that happen to come out adjacent prove nothing. Only a single insn guarantees it. A multi-instruction output template is the simplest way to get one, and many backends use it for exactly this purpose.

The trade-off follows from the same fact. Once the pair is one insn, no RTL pass can see the intermediate `high` value. No pass can share an `addis` between two nearby addresses or move work into the gap. That is the point here, but it also means the combined pattern takes over the job the old pair did, including addresses with a constant offset (hence the `_plus` variants).

The pattern for coexistence is worth copying too. The old patterns are not deleted. They are fenced off with `!TARGET_P10_FUSION`, and the new ones are fenced in with `TARGET_P10_FUSION`. Two patterns that can match the same RTL under the same conditions cause trouble, and mirrored conditions are the standard way to keep them apart.

The dossier does not confirm where `TARGET_P10_FUSION` comes from. The researcher found it used as a condition in `gcc/config/rs6000/fusion.md` and found `OPTION_MASK_P10_FUSION` in old ChangeLogs, but did not find its definition. `rs6000-cpus.def` shows how the P8 fusion flags are defined as ISA masks (`OPTION_MASK_P8_FUSION | OPTION_MASK_P8_FUSION_SIGN`). The new tests compile with `-mcpu=power9 -mtune=power10`, which suggests the flag follows tuning, not the ISA level. That is an inference, not something the dossier shows.

## See it yourself

The two new tests show the approach. Each compiles a function that returns the sum of the addresses of two static ints:

```
static int foo, bar;

unsigned long test(void)
{
        return (unsigned long)&foo + (unsigned long)&bar;
}
```

`pr108018-elf.c` requires `lp64`, skips AIX, and runs with `-O2 -dp -mcpu=power9 -mtune=power10`. `pr108018-aix.c` runs only on `powerpc*-*-aix*` and adds `-mcmodel=large`. The `-dp` flag annotates each assembler line with the name of the insn pattern that produced it. The checks then look for pattern names, not instructions: the ELF test expects both `largetocp10` and `largetocp10_plus`, and the AIX test expects `largetocp10_aix` exactly twice.

The tests check that GCC chose the combined pattern, not that the hardware fused anything at runtime. To check your own code, compile it with the same flags plus `-S -dp` and look at the comments next to each `addis`. If both halves sit under one `*largetocp10*` annotation, the pair is one insn and the scheduler could not have split it.
