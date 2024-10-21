#include "printlib.h"

int main(){
  int toto,tete;
  toto = 45;
  tete = -7;
  println_int(-toto%-tete);
  return 0;
}

// EXPECTED
// -3