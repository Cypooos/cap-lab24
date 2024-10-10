#include "printlib.h"

int main(){
  int toto,tete,a,b;
  toto = 45;
  tete = -7;
  a = 2147483648;
  println_int(toto%tete);
  println_int(-toto%tete);
  println_int(toto%-tete);
  println_int(-toto%-tete);
  println_int(toto%a);
  println_int(a%tete+toto);
  return 0;
}

// EXPECTED
// 3
// -3
// 3
// -3
// 45
// 43