#include "printlib.h"

int main(){
  int a,b,fibo,n,i;
  n = 15; 
  a = 0;
  b = 1;
  for (i=0;i<n;i=i+1){
    fibo = a + b;
    b = a;
    a = fibo;
    println_int(fibo);
  }
  return 0;
}

// EXPECTED
// 1
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