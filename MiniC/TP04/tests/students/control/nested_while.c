#include "printlib.h"

int main(){
  int a,b,c;
  while (a<2) {
    while (b<2) {
      while (c<2) {
        c = c + 1;
        println_int(c);
      }
      b = b + 1;
      println_int(b);
    }
    a = a + 1;
    println_int(a);
  }
  return 0;
}

// EXPECTED
// 1
// 2
// 1
// 2
// 1
// 2
