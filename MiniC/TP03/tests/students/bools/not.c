#include "printlib.h"

int main(){
  bool a,b;
  b = true;
  println_bool(!a);
  println_bool(!!a);
  println_bool(!b);
  println_bool(!!b);
  return 0;
}

// EXPECTED
// 1
// 0
// 0
// 1