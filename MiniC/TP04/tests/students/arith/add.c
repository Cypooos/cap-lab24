#include "printlib.h"

int main(){
  int a,b,c;
  a = 490820;
  b = 102;
  c = -98521;
  println_int(a+b);
  println_int(a+c);
  println_int(b+c);
  return 0;
}

// EXPECTED
// 490922
// 392299
// -98419