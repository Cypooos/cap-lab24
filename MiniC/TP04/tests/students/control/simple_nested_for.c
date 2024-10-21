#include "printlib.h"

int main(){
  int i,j,n;
  n = 40;
  for(i=0;i<n;i=i+1) {
    for(j=0;j<n;j=j+1) {}
  }
  println_int(i);
  println_int(j);
  return 0;
}

// EXPECTED
// 40
// 40