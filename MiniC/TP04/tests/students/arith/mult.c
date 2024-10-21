#include "printlib.h"

int main(){
  int toto,tete,a,b;
  toto = 45;
  tete = -7;
  println_int(toto*toto);
  println_int(toto*485*2);
  return 0;
}

// EXPECTED
// 2025
// 43650