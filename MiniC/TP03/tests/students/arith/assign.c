#include "printlib.h"

int main(){
  int toto;
  toto = toto + 580;
  toto = toto * 2;
  toto = toto + 3;
  toto = (toto + 2) / 5;
  println_int(toto);
  return 0;
}

// EXPECTED
// 233