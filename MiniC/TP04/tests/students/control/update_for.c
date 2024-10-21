#include "printlib.h"


int main(){
  int i,j,n,sum;
  n = 481400;
  for(i=1;i<n;i=i*3) {
    sum = sum + 1;
    for(j=0;j<i;j=j+1) n = n +1;
  }
  println_int(sum);
  return 0;
}

// EXPECTED
// 13