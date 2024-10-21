#include "printlib.h"

// too many variables for naive allocator, buut works in all-in-mem
int main(){
  int toto;
  toto = 45;
  println_int(toto + toto + toto + toto + toto + toto + toto + toto + toto + toto + toto+ toto+ toto+ toto+ toto+ toto+ toto);
  return 0;
}

// EXPECTED
// 765