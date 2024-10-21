#include "printlib.h"

int main(){
  bool a,b;
  a = true;
  b = true;
  while (a) {
    println_int(40);
    while (b) {
      println_int(17);
      b = false;
    }
    println_int(28);
    a = false;
  }
  return 0;
}

// EXPECTED
// 40
// 17
// 28
