#include "printlib.h"

int main(){
  if (false) {
    println_float(45); // check if even if the condition is false, we visit also the else in the typechecker
  } else {
  }
  return 0;
}

// EXITCODE 2
// EXPECTED
// In function main: Line 5 col 4: invalid type for println_float statement: integer