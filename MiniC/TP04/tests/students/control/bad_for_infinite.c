#include "printlib.h"

int main(){
  int toto,a;
  toto = 4;
  a = 32;
  for (;;) {
    toto = toto - 1;
    a = a + 42/toto;
    println_int(a);
  }
  return 0;
}

// SKIP TEST EXPECTED
// EXECCODE 1
// EXPECTED
// 46
// 67
// 109
// Division by 0