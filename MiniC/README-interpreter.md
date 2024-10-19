# MiniC interpreter and typer
LAB3, MIF08 / CAP / CS444 2022-23

# Authors

BOUROTTE Coda

# Contents

Nothing changed. 

# Howto

`make test-interpret TEST_FILES='TP03/tests/provided/examples/test_print_int.c'` for a single run

`make test` to test all the files in `*/tests/*` according to `EXPECTED` results.

You can select the files you want to test by using `make test TEST_FILES='TP03/**/*bad*.c'` (`**` means
"any number of possibly nested directories").

# Test design 

The folders in `tests/students` are organised as such :
- `arith/` contain test on arithmetic operations,
- `bools/` on booleans,
- `typing/` all sort of typing errors,
- `control/` for all control structure like `if`, `for` or `while`

# Design choices

I implemented C-style for loops. Just like in C, you can have an argument of a C-loop empty (`for (;;) {}`).
A for can have an asignement `for(i=45;;)` or an expression (since in C, assignement are expression). I implemented that.
I decided to implement overflow of integers, that's why most test are concentrated on integers.

# Known bugs

I implemented the `for` extension.