#include "printlib.h"

int main(){
  int a,b;
  a = 77779;
  b = 485;
  println_int(a*-b);
  println_int(-a*-b);
  return 0;
}

// EXPECTED
// -37722815
// 37722815