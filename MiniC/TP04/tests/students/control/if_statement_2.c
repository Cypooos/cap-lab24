#include "printlib.h"

int main(){
  int toto;
  toto = 45;
  if (toto < 200) {
    toto = 17;
  } else {
    println_int(1/0);
  }
  println_int(toto);
  return 0;
}

// EXPECTED
// 17