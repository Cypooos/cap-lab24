#include "printlib.h"

int main(){
  bool a,b;
  a = true;
  b = false;
  println_bool(a == b);
  println_bool(a == true);
  return 0;
}


// EXPECTED
// 0
// 1
