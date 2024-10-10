#include "printlib.h"

int main(){
  int i,sum,n;
  n = 40;
  for(i=0;i<n;i=i+1) {
    sum = sum + i*i;
  }
  println_int(sum);
  println_int(i);
  return 0;
}

// EXPECTED
// 20540
// 40