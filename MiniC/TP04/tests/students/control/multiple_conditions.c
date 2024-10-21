#include "printlib.h"

int main(){
  int toto;
  toto = 42;
  if (toto < 20) {
    toto = toto + 10;
  } else if (toto >30) {
    toto = toto + 50;
  } else {
    toto = toto + 5;
  }
  if (toto == 1) toto = toto + 8888888;
  if (toto == 92) toto = toto + 5;
  println_int(toto);
  return 0;
}

// EXPECTED
// 97