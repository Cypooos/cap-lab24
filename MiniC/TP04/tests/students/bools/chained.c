#include "printlib.h"

int main(){
  int a,b;
  a = 42;
  b = 43;
  println_bool(a == b == false);
  println_bool(a != b != false);
  println_bool(a != b != (a == b));
  println_bool(a != b == (a == b));
  return 0;
}

// EXPECTED
// 1
// 1
// 1
// 0