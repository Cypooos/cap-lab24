grammar Tree;


int_tree_top : int_tree EOF #topper
    ;

int_tree:  INT    #leaf
    | '(' INT int_tree+ ')'  #node
    ;


INT: [0-9]+;
WS  :   (' '|'\t'|'\n')+  -> skip;



