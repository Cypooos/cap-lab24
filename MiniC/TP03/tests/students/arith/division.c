#include "printlib.h"

int main(){
  int toto,tete,a,b;
  toto = 42;
  tete = 6;
  b = 954521;
  a = 500421;
  println_int(b/toto);
  println_int(-b/toto);
  println_int(-b/-toto);
  println_int(b/-toto);
  println_int(tete/toto);
  println_int(a/b/2);
  println_int(a/(b/2));
  println_int(b/a/tete);
  println_int(-a/a);
  return 0;
}

// EXPECTED
// 22726
// -22726
// 22726
// -22726
// 0
// 0
// 1
// 0
// -1