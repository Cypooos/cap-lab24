#include "printlib.h"

int main(){
  int a,b;
  a = 512;
  b = 718;
  println_bool(a > b);
  println_bool(b > a);
  println_bool(a > a);
  return 0;
}


// EXPECTED
// 0
// 1
// 0
