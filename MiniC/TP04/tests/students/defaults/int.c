#include "printlib.h"

int main() {
    int x;
	println_int(x);
    x = x*x;
	println_int(x+1);
	return 0;
}

// EXPECTED
// 0
// 1