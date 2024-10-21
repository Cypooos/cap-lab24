#include "printlib.h"

int main(){
  int toto,a;
  toto = 42;
  for (;toto > 0;) {
    a = a + 1;
    toto = toto - 10;
  }
  println_int(a);
  println_int(toto);
  return 0;
}

// EXPECTED
// 5
// -8