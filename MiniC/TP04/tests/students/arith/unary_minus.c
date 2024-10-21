#include "printlib.h"

int main(){
  int a,b,c;
  a = 784;
  b = 20168;
  c = -98521;
  println_int(a+-b);
  println_int(-(-c));
  return 0;
}

// EXPECTED
// -19384
// -98521