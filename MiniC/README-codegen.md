# MiniC Compiler 
LAB4 (simple code generation), MIF08 / CAP 2022-23

# Authors

Bourotte Coda

# Contents

The code infrastructure didn't changed.

# Test design 

Most tests are made with the naive-implementation in mind, so that they doesn't get skipped upon testing.
That's why the `modulo`, `division`, `mult` and `chained` tests are splitted in differents tests.

Otherwise, tests are split in differents folders:
- `alloc` for the tests that only works with the `all-in-mem` allocator (and `alloc/hundred_vars.c` doesnis too big for the `all-in-mem`)
- `arith` for the test on arithmetic operations (add, sub, minus, mult, div, mod)
- `bools` for the tests on booleans (or, and, not) and chained comparaisons
- `comp` for the tests on comparaison operators (`<`, `<=`, `>`, `>=`, `==`, `==`) on both bool and int
- `control` for the tests on control operations (if-then-else, while, for)
- `defaults` for the test on default values of types (for `bool` it's `false` and for `int` it's `0`)

I tested the CFG of a division by zero with `test/dataflow/bad_div0.c`.

# Design choices

I implemented the `for` loop extension, see the corresponding tests in the `control` test folder

# Known bugs

No known bugs.

# Checklists

A check ([X]) means that the feature is implemented and *tested* with appropriate test cases.

## Code generation

- [X] Number Atom
- [X] Boolean Atom
- [X] Id Atom
- [X] Additive expression
- [X] Multiplicative expression
- [X] UnaryMinus expression
- [X] Or expression
- [X] And expression
- [X] Equality expression
- [X] Relational expression (! many cases -> many tests)
- [X] Not expression

## Statements

- [X] Prog, assignements
- [X] While
- [X] Cond Block
- [X] If
- [X] Nested ifs
- [X] Nested whiles

## Allocation

- [X] Naive allocation
- [X] All in memory allocation
- [X] Massive tests of memory allocation

