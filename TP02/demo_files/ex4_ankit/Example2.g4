//define a tiny grammar for arith expressions with identifiers

grammar Example2;

full_expr: expr EOF;

expr: 
    |'(' expr ')' expr
    |'[' expr ']' expr
    | ;



//OP : '+'| '*' | '-' | '/';
//INT : '0'..'9'+ ;
//ID : ('a'..'z'|'A'..'Z')+ ;


CHARS: ~[()[\]]-> skip ;
EMP: ;