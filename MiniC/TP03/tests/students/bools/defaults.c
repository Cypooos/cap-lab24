#include "printlib.h"

int main(){
  bool a,b;
  println_bool(true);
  println_bool(false);
  println_bool(a);
  return 0;
}

// EXPECTED
// 1
// 0
// 0