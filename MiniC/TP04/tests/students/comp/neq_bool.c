#include "printlib.h"

int main(){
  bool a,b;
  a = true;
  b = false;
  println_bool(a != b);
  println_bool(b != false);
  return 0;
}


// EXPECTED
// 1
// 0
