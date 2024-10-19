#include "printlib.h"

int main(){
  float toto,tete,b;
  toto = 42.5;
  tete = 6.95;
  b = 5745.24;
  println_float(b/toto/tete);
  return 0;
}

// EXPECTED
// 19.45