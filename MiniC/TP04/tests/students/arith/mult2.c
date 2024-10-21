#include "printlib.h"

int main(){
  int a,b;
  a = 77779;
  b = 485;
  println_int(-b*45);
  println_int(a*b);
  return 0;
}

// EXPECTED
// -21825
// 37722815