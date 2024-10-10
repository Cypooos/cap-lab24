#include "printlib.h"

int main(){
  int toto,a,b,c;
  toto = 45;
  a = 2147483648;
  b = a+7585210;
  c = 425253;
  println_int(toto+a+a);
  println_int(toto+b);
  println_int(a+b+c);
  println_int(c+c+c+c+c+c+c+c+c+a+a+b);
  return 0;
}

// EXPECTED
// 45
// -2139898393
// 8010463
// -2136071161