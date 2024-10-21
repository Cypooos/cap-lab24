#include "printlib.h"

int main(){
  int toto,b;
  toto = 42;
  b = 954521;
  println_int(-b/-toto);
  println_int(b/-toto);
  return 0;
}

// EXPECTED
// 22726
// -22726