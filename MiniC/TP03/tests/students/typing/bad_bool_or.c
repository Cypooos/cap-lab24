#include "printlib.h"

int main(){
  bool t;
  t = "string here" || t;
  return 0;
}

// EXITCODE 2
// EXPECTED
// In function main: Line 5 col 6: invalid type for or operand: string and boolean