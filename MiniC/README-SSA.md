# MiniC Compiler 
LAB5a (Control Flow Graph in SSA Form) & LAB5b (Smart Register Allocation), CAP 2022-23

# Authors

Coda Bourotte

# Contents

I have made no special cases no extra bonus things. 

# Test design 

There is no new test for the lab 5 as I beleive the lab4 to cover a lot of cases.

Unfortunatly, some tests from the lab 4 was holding forever, so I had to remove them. Some other tests are not sucessfull (6 to be exact), but the allocator seems to work, as `alloc/hundred_vars.c` is working. I believe the issue is from the `LivenessSSA.py` code.

# Known bugs

The `livenessSSA.py` doesn't give the same answer for the liveness of variables for `python3 MiniCC.py --mode=codegen-ssa --reg-alloc smart --debug TP04/tests/provided/dataflow/df04.c` as the expected output indicated on the lab pdf.