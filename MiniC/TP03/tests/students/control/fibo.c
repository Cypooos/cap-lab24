#include "printlib.h"

int main(){
  int a,b,fibo,n;
  n = 14; 
  a = 1;
  while (n > 0) {
    fibo = a + b;
    b = a;
    a = fibo;
    n = n - 1;
    println_int(fibo);
  }
  return 0;
}

// EXPECTED
// 1
// 2
// 3
// 5
// 8
// 13
// 21
// 34
// 55
// 89
// 144
// 233
// 377
// 610