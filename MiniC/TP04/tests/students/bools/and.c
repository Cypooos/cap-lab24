#include "printlib.h"

int main(){
  bool a,b;
  b = true;
  println_bool(a && a);
  println_bool(a && b);
  println_bool(b && a);
  println_bool(b && b);
  return 0;
}

// EXPECTED
// 0
// 0
// 0
// 1