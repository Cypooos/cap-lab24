# Generated from Tree.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TreeParser import TreeParser
else:
    from TreeParser import TreeParser

# This class defines a complete listener for a parse tree produced by TreeParser.
class TreeListener(ParseTreeListener):

    # Enter a parse tree produced by TreeParser#topper.
    def enterTopper(self, ctx:TreeParser.TopperContext):
        pass

    # Exit a parse tree produced by TreeParser#topper.
    def exitTopper(self, ctx:TreeParser.TopperContext):
        pass


    # Enter a parse tree produced by TreeParser#leaf.
    def enterLeaf(self, ctx:TreeParser.LeafContext):
        pass

    # Exit a parse tree produced by TreeParser#leaf.
    def exitLeaf(self, ctx:TreeParser.LeafContext):
        pass


    # Enter a parse tree produced by TreeParser#node.
    def enterNode(self, ctx:TreeParser.NodeContext):
        pass

    # Exit a parse tree produced by TreeParser#node.
    def exitNode(self, ctx:TreeParser.NodeContext):
        pass



del TreeParser