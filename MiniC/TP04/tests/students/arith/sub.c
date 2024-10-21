#include "printlib.h"

int main(){
  int a,b,c;
  a = 490820;
  b = 102;
  c = -98521;
  println_int(a-b);
  println_int(a-c);
  println_int(b-a);
  return 0;
}

// EXPECTED
// 490718
// 589341
// -490718