#include "printlib.h"

int main(){
  int b;
  b = 954521;
  println_int(b/2/18);
  println_int(b/18/7);
  return 0;
}

// EXPECTED
// 26514
// 7575