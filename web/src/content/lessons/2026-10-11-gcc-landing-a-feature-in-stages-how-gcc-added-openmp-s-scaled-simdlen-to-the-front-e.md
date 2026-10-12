---
project: gcc
subsystem: openmp
patch_id: null
tags:
- openmp
- simd
- vectorization
- front-end
- tree-ir
lesson_id: gcc:2026-W41
commit_hash: fbcafeec06a66175108be68c34aceafba7a453b9
source_type: github
headline: 'Landing a Feature in Stages: How GCC Added OpenMP''s `scaled` simdlen to
  the Front End While the Middle End Rejects It'
hook: GCC now parses, type-checks and prints a vector-length form it cannot compile
  yet. How that works shows how GCC grows an IR node without breaking the code that
  reads it.
tldr: 'GCC''s C/C++ front ends now accept simdlen(scaled(type[, divisor]) : length),
  stored as two new clause operands. Gimplification turns it into a sorry.'
concept: A new language feature can land front end first. Parse it, give the IR node
  a slot for it, and stop it with a 'sorry' where lowering would start. Optional operands
  that default to NULL let code that never reads them keep working.
prerequisites:
- 'what OpenMP''s #pragma omp simd does'
- basic idea of SIMD vector width
- GCC's front end / middle end split
- what a compiler IR node is
code_tour:
- path: gcc/tree.h
  symbol: OMP_CLAUSE_SIMDLEN_EXPR
  lines: 2163-2170
  why: The three accessors that map the length, the scaled type and the divisor to
    operand slots 0, 1 and 2 of the simdlen clause node.
- path: gcc/tree.cc
  symbol: omp_clause_num_ops
  lines: 366-367
  why: The one-number change from 1 to 3 that gives every OMP_CLAUSE_SIMDLEN node
    its two new slots.
- path: gcc/c/c-parser.cc
  symbol: c_parser_omp_clause_simdlen
  lines: 20178-20275
  why: The bounded lookahead (scaled, open paren, balanced tokens, colon) that tells
    the modifier apart from an expression, plus the type and divisor validation.
- path: gcc/cp/semantics.cc
  symbol: finish_omp_clauses
  lines: 8771-8814
  why: C++ checking of the modifier, which defers checks on dependent types and expressions
    until template instantiation.
- path: gcc/gimplify.cc
  symbol: gimplify_scan_omp_clauses
  lines: 14923-14930
  why: 'The stop point for loop-level simd: a non-NULL TYPE operand removes the clause
    with a sorry.'
- path: gcc/omp-simd-clone.cc
  symbol: simd_clone_clauses_extract
  lines: 346-353
  why: The stop point for declare simd, where the plain length is read and a sorry
    is issued if the scaled type is present.
- path: gcc/omp-general.cc
  symbol: omp_construct_simd_compare
  lines: 2325-2331
  why: declare variant matching records type and divisor, and normalizes a missing
    divisor to integer_one_node.
- path: gcc/testsuite/c-c++-common/gomp/simdlen-scaled-1.c
  symbol: ''
  lines: 1-23
  why: The test that fixes both the sorry text and the GIMPLE-dump form of the scaled
    attribute.
takeaways:
- 'A feature can land front end first: parse, represent, check and print it, then
  put a sorry where lowering would need knowledge that doesn''t exist yet.'
- Optional IR operands that default to NULL leave existing consumers unaffected. The
  code at risk is the code that compares nodes.
- Each equality or matching site has to decide what a missing operand means. Two sites
  can decide differently without anyone noticing.
- Vector width is not always a compile-time constant. Scalable vector ISAs push length
  decisions toward type- and target-relative expressions.
- In C++, check what you can at parse time and defer anything that depends on a template
  parameter until instantiation.
further_reading:
- title: 'GCC commit fbcafeec06a6: OpenMP: Add the ''scaled'' modifier to the ''simdlen''
    clause [PR127723]'
  url: https://github.com/gcc-mirror/gcc/commit/fbcafeec06a66175108be68c34aceafba7a453b9
primer_expert: 'OMP_CLAUSE_SIMDLEN grows from one to three operands (omp_clause_num_ops),
  adding TYPE and DIVISOR for OpenMP 6.1''s scaled(T[,d]):len form. C/C++ parse and
  validate it, but gimplify_scan_omp_clauses and simd_clone_clauses_extract sorry
  on it, so no simd clone mangling or vectorizer path sees a VL-relative length. Watch
  for an inconsistency: omp_declare_simd_clauses_equal treats a NULL divisor as distinct
  from 1, while omp_construct_simd_compare normalizes it to integer_one_node.'
primer_glossary:
- term: simdlen
  definition: An OpenMP clause that tells the compiler how many SIMD lanes to target
    for a loop or a vectorized function. Before OpenMP 6.1 it took only a positive
    integer constant.
- term: safelen
  definition: An OpenMP clause giving the largest number of loop iterations that can
    safely run concurrently in SIMD lanes. It caps simdlen.
- term: declare simd
  definition: An OpenMP directive asking the compiler to emit vector versions of a
    function, so that vectorized loops can call it once per group of lanes.
- term: SIMD clone
  definition: A compiler-generated vector version of a function produced for declare
    simd. In GCC, omp-simd-clone.cc builds them.
- term: declare variant
  definition: An OpenMP directive that substitutes a different function at call sites
    whose context matches a given selector.
- term: context selector
  definition: The part of a declare variant directive that describes when the variant
    applies, for example a construct like simd with particular traits such as simdlen.
- term: TR14
  definition: OpenMP Technical Report 14, the published draft that became OpenMP 6.1.
    GCC tracks features from such reports ahead of the final spec.
- term: VL
  definition: 'Vector length: how many elements of a given type fit in one hardware
    vector. On scalable-vector targets such as AArch64 and RISC-V it may only be known
    at runtime.'
- term: OMP_CLAUSE
  definition: The GCC tree node kind for one OpenMP clause. It carries a clause code,
    a fixed number of operand slots, and a chain pointer to the next clause.
- term: error_mark_node
  definition: A sentinel tree GCC uses for an erroneous construct, so that later code
    can skip it quietly instead of issuing follow-on errors.
landing_slug: 2026-10-07-openmp-fbcafeec
url: https://github.com/gcc-mirror/gcc/commit/fbcafeec06a66175108be68c34aceafba7a453b9
week_start: '2026-10-05'
week_end: '2026-10-11'
commit_date: '2026-10-07'
date: '2026-10-11'
is_stub: false
stub_reason: ''
---

## Background: simdlen and the fixed-width assumption

OpenMP gives programmers a portable way to ask for vectorization. `#pragma omp simd` marks a loop for SIMD execution. `#pragma omp declare simd` asks the compiler to emit vector variants (SIMD clones) of a function. `declare variant` lets a programmer say "call this other function when the context matches", and that context can include a `simd` trait. On all three, the `simdlen` clause names the number of lanes the programmer wants: `simdlen(8)` means eight elements at a time.

A single integer is enough when the vector width is fixed for the ISA, such as 128-bit SSE or 256-bit AVX. The commit message names the targets where it is not: AArch64 and RISC-V, whose vector length (VL) depends on the target and on the element type, and "might be only known at runtime". A literal `8` can't express "as many `float`s as one hardware vector holds".

OpenMP 6.1 (published as Technical Report 14) adds an optional modifier for this:

```c
simdlen( scaled(arith-type [, divisor]) : length )
```

The commit message defines the scale factor as `max(1, round_down(VL(type) / divisor))`. When the modifier is absent the factor is one. `divisor` and `length` must be constants >= 1, and `type` must be an arithmetic type (a numeric intrinsic type in Fortran). The modifier is allowed on `declare simd`, on the `simd` directive, and in a `declare variant` context selector.

## Mechanism: one clause node, three operand slots

GCC represents OpenMP clauses as `OMP_CLAUSE` tree nodes. Each clause code gets a fixed number of operand slots, which `omp_clause_num_ops` in `gcc/tree.cc` records. This commit changes the entry for simdlen from 1 to 3:

```c
  1, /* OMP_CLAUSE_SAFELEN  */
  3, /* OMP_CLAUSE_SIMDLEN  */
```

`gcc/tree.h` names the slots:

```c
#define OMP_CLAUSE_SIMDLEN_EXPR(NODE) \
  OMP_CLAUSE_OPERAND (OMP_CLAUSE_SUBCODE_CHECK (NODE, OMP_CLAUSE_SIMDLEN), 0)
#define OMP_CLAUSE_SIMDLEN_TYPE(NODE) \
  OMP_CLAUSE_OPERAND (OMP_CLAUSE_SUBCODE_CHECK (NODE, OMP_CLAUSE_SIMDLEN), 1)
#define OMP_CLAUSE_SIMDLEN_DIVISOR(NODE) \
  OMP_CLAUSE_OPERAND (OMP_CLAUSE_SUBCODE_CHECK (NODE, OMP_CLAUSE_SIMDLEN), 2)
```

Operand 0 still holds the length. Operand 1 holds the arithmetic type from `scaled(...)`. Operand 2 holds the optional divisor. A plain `simdlen(N)` leaves both new slots `NULL_TREE`. Every consumer therefore has to treat NULL as "no modifier", and a consumer that only reads operand 0 sees the same node shape it always did.

The C parser, `c_parser_omp_clause_simdlen` in `gcc/c/c-parser.cc`, has a problem to solve: `scaled(...)` could also be the start of an ordinary expression, such as a call to a function named `scaled`. The parser takes the modifier path only after a bounded lookahead succeeds. The next token must be the identifier `scaled`, the token after it an open paren, the raw tokens inside must balance (`c_parser_check_balanced_raw_token_sequence`), and the token after the closing paren must be `CPP_COLON`. The colon is what tells the two readings apart. Once the path is taken, the parser reads a type name with `c_parser_type_name` and `groktypename`. It accepts only `INTEGRAL_TYPE_P`, `SCALAR_FLOAT_TYPE_P` or `COMPLEX_TYPE` types. If a comma follows, it folds the divisor and requires it to be a positive `INTEGER_CST`.

When the type or the divisor is bad, the parser sets `type = error_mark_node`. It then skips parsing the length and returns the clause list without the new clause. So a malformed modifier produces one diagnostic and a dropped clause, not a cascade of errors. On success it builds the node with all three slots:

```c
c = build_omp_clause (clause_loc, OMP_CLAUSE_SIMDLEN);
OMP_CLAUSE_SIMDLEN_EXPR (c) = t;
OMP_CLAUSE_SIMDLEN_TYPE (c) = type;
OMP_CLAUSE_SIMDLEN_DIVISOR (c) = divisor;
```

C++ splits the work differently because of templates. `cp_parser_omp_clause_simdlen` parses the syntax, and `finish_omp_clauses` in `gcc/cp/semantics.cc` validates it. The type must satisfy `ARITHMETIC_TYPE_P` unless `dependent_type_p` holds. The divisor must be integral unless `type_dependent_expression_p` holds. Only when `!processing_template_decl` does the code run the divisor through `maybe_constant_value` and require a positive `INTEGER_CST`. Inside a template, those checks wait until instantiation. The commit message says `tsubst_omp_clauses` in `gcc/cp/pt.cc` now substitutes the new operands.

## The change: front end complete, middle end says sorry

The commit message states the scope: "This commit adds support for C and C++, only, and currently fails with a sorry in gimplify_scan_omp_clauses and simd_clone_clauses_extract." A `sorry` is GCC's diagnostic for "this is valid input, but this compiler does not implement it yet". It is different from an error, which means the input is wrong.

The gate for loop-level `simd` sits in `gimplify_scan_omp_clauses` in `gcc/gimplify.cc`, where OpenMP clauses are lowered into GIMPLE:

```c
case OMP_CLAUSE_SIMDLEN:
  if (OMP_CLAUSE_SIMDLEN_TYPE (c))
    {
      remove = true;
      sorry_at (OMP_CLAUSE_LOCATION (c),
		"%<simdlen%> clause with %<scaled%> modifier");
    }
  break;
```

The gate for `declare simd` sits in `simd_clone_clauses_extract` in `gcc/omp-simd-clone.cc`. That function reads the plain length into `clone_info->simdlen` with `TREE_INT_CST_LOW`, then calls `sorry_at` if `OMP_CLAUSE_SIMDLEN_TYPE` is set. In both places a non-NULL TYPE operand acts as the "this is the new feature" flag. That works only because plain `simdlen(N)` leaves the operand NULL.

The commit also updates the code that compares clauses. Two `declare simd` attributes that differ only in their scale must not be treated as the same, and `declare variant` matching needs to see the modifier. `omp_declare_simd_clauses_equal` in `gcc/attribs.cc` now requires the TYPE pointers to match. It also requires either both divisors to be NULL, or both to be present and equal under `simple_cst_equal`. `omp_construct_simd_compare` in `gcc/omp-general.cc` records simdlen, type and divisor for each side, and replaces a missing divisor with `integer_one_node` before comparing.

The two sites handle the default differently. `omp-general.cc` makes `scaled(T)` equivalent to `scaled(T, 1)`. `attribs.cc` treats a NULL divisor and an explicit one as unequal. Nothing in the commit says whether this difference is intended, so read it as an open question, not a confirmed bug. It does show the risk with optional operands: every comparison site has to decide on its own what the missing value means.

The dump printer in `gcc/tree-pretty-print.cc` also learns the modifier, so the attribute survives into `-fdump-tree-gimple` output. The commit message also notes a fix to how `dump_omp_context_selector` prints the `simd` trait.

## Consequences for developers outside OpenMP

If you write OpenMP code for GCC, the syntax is now recognized in C and C++. Malformed uses get real diagnostics: a non-arithmetic type, or a divisor that is not a positive constant. Well-formed uses get a `sorry, unimplemented` and the clause is dropped. Generated code does not change. Fortran is not covered by this commit.

If you work on other parts of GCC, the lesson is the pattern. The commit gives the IR node a home for the information, teaches the parsers and semantic checks to fill it, and teaches equality, matching and printing to respect it. It then puts a clearly labelled stop exactly where lowering would need target knowledge that does not exist yet. Here that knowledge is `VL(type)`, which on the targets in question may only be known at runtime. Later work can replace two `sorry_at` calls instead of rebuilding the front end.

The pattern holds only if the new operand defaults to NULL and every consumer honors that default. Code that never asks about TYPE or DIVISOR keeps working because, for every existing program, those slots are NULL. The code that must change is the code that decides whether two clauses are equal or match. Those sites are where a new operand can quietly change behavior, as the divisor-default difference shows.

## See it yourself

The new test `gcc/testsuite/c-c++-common/gomp/simdlen-scaled-1.c` is the shortest demonstration. It compiles with `-fdump-tree-gimple -w` and declares three functions:

```c
#pragma omp declare simd simdlen(scaled(int, 1): 1)
void g1(int a) { }
#pragma omp declare simd simdlen(scaled(float, 2): 2)
void g2(int a) { }
#pragma omp declare simd simdlen(scaled(_Complex double): 4)
void g3(int a) { }
```

For each function it expects a message of the form "sorry, unimplemented: 'scaled' modifier specified in 'simdlen' clause on 'declare simd' directive for 'g1'". C++ prints the full signature, `'void g1(int)'`. It also scans the GIMPLE dump for the printed attributes, for example `__attribute__((omp declare simd (simdlen(scaled(int,1):1))))` and `simdlen(scaled(complex double):4)`. The sorry fires, yet the attribute still appears in the dump. That confirms the front end built the full three-operand node before the clone code rejected it.

To reproduce, compile the file with `-fopenmp -fdump-tree-gimple` (or `-fopenmp-simd`) and open the `.gimple` dump. Or run the test through the GCC testsuite harness with `make check-gcc RUNTESTFLAGS="gomp.exp=simdlen-scaled-*"`. The commit adds five more tests, `simdlen-scaled-2.c` through `-4.c` and the two `g++.dg/gomp` files. Read them for the error-path and template coverage.
