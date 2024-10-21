#include "printlib.h"

int main(){
  int toto;
  toto = 27/0;
  println_int(27);
  println_int(toto);
  return 0;
}

// SKIP TEST EXPECTED
// EXECCODE 1
// EXPECTED
// Division by 0