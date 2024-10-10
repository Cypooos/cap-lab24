#include "printlib.h"

int main(){
  int toto,a,b,c;
  toto = 45;
  a = 2147483648;
  b = 2147483647;
  println_int(a);
  println_int(-a);
  println_int(b);
  println_int(-b);
  println_int(-(-b+a+a+b+ -(toto-a-(-8452-b))));
  return 0;
}

// EXPECTED
// -2147483648
// -2147483648
// 2147483647
// -2147483647
// 8496