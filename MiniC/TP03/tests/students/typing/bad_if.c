#include "printlib.h"

int main(){
  if (true) {
  } else {
    println_float(45); // check if even if the condition is true, we visit also the else in the typechecker
  }
  return 0;
}

// EXITCODE 2
// EXPECTED
// In function main: Line 6 col 4: invalid type for println_float statement: integer