#include "printlib.h"

int main(){
  int toto,tete,a,b;
  toto = 45;
  tete = -7;
  a = 77779;
  b = 485;
  println_int(toto*toto);
  println_int(toto*485*2*74);
  println_int(-b*tete);
  println_int(a*b);
  println_int(a*-b);
  println_int(-a*-b);
  return 0;
}

// EXPECTED
// 2025
// 3230100
// 3395
// 37722815
// -37722815
// 37722815