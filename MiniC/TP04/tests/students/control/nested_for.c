#include "printlib.h"

int main(){
  int i,j,n,sum;
  n = 40;
  for(i=0;i<n;i=i+1) {
    for(j=0;j<n;j=j+1) {
      sum = sum + i + j;
    }
  }
  println_int(sum);
  return 0;
}

// EXPECTED
// 62400