#include "printlib.h"

int main(){
  if (45 > 2) {
    println_int(42);
  } else {
    println_int(1/0);
  }
  return 0;
}

// EXPECTED
// 42