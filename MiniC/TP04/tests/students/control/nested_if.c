#include "printlib.h"

int main(){
  bool toto;
  if (toto) {
    println_int(1);
  } else {
    if (!toto) toto = true;
    if (toto) {
        println_int(70);
    } else {
        println_int(17);
    }
  } 
  return 0;
}

// EXPECTED
// 70