#include "printlib.h"

int main(){
  int four,three;
  four = 4;
  three = 3;
  println_int(four/three);
  println_int(four%three);
  println_int((-four)/three);
  println_int((-four)%three);
  println_int(four/(-three));
  println_int(four%(-three));
  println_int((-four)/(-three));
  println_int((-four)%(-three));
  return 0;
}

// EXPECTED
// 1
// 1
// -1
// -1
// -1
// 1
// 1
// -1