#include "printlib.h"

int main(){
  int toto;
  toto = 42;
  if (toto < 20) {
    toto = toto + 10;
  } else if (toto >30) {
    toto = toto + 50;
  }
  println_int(toto);
  return 0;
}

// EXPECTED
// 92