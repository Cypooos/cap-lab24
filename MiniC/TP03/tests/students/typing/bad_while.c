#include "printlib.h"

int main(){
  int toto;
  while (toto) {
    println_int(5);
  }
  return 0;
}

// EXITCODE 2
// EXPECTED
// In function main: Line 5 col 2: invalid type for while statement: integer