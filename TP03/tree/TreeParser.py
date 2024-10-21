# Generated from Tree.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,4,20,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,4,1,12,8,1,
        11,1,12,1,13,1,1,1,1,3,1,18,8,1,1,1,0,0,2,0,2,0,0,19,0,4,1,0,0,0,
        2,17,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,18,5,3,0,0,8,
        9,5,1,0,0,9,11,5,3,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,13,1,0,0,0,
        13,11,1,0,0,0,13,14,1,0,0,0,14,15,1,0,0,0,15,16,5,2,0,0,16,18,1,
        0,0,0,17,7,1,0,0,0,17,8,1,0,0,0,18,3,1,0,0,0,2,13,17
    ]

class TreeParser ( Parser ):

    grammarFileName = "Tree.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "INT", "WS" ]

    RULE_int_tree_top = 0
    RULE_int_tree = 1

    ruleNames =  [ "int_tree_top", "int_tree" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    INT=3
    WS=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Int_tree_topContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TreeParser.RULE_int_tree_top

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TopperContext(Int_tree_topContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TreeParser.Int_tree_topContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def int_tree(self):
            return self.getTypedRuleContext(TreeParser.Int_treeContext,0)

        def EOF(self):
            return self.getToken(TreeParser.EOF, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopper" ):
                listener.enterTopper(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopper" ):
                listener.exitTopper(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopper" ):
                return visitor.visitTopper(self)
            else:
                return visitor.visitChildren(self)



    def int_tree_top(self):

        localctx = TreeParser.Int_tree_topContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_int_tree_top)
        try:
            localctx = TreeParser.TopperContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.int_tree()
            self.state = 5
            self.match(TreeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_treeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TreeParser.RULE_int_tree

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NodeContext(Int_treeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TreeParser.Int_treeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(TreeParser.INT, 0)
        def int_tree(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TreeParser.Int_treeContext)
            else:
                return self.getTypedRuleContext(TreeParser.Int_treeContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNode" ):
                listener.enterNode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNode" ):
                listener.exitNode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNode" ):
                return visitor.visitNode(self)
            else:
                return visitor.visitChildren(self)


    class LeafContext(Int_treeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TreeParser.Int_treeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(TreeParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeaf" ):
                listener.enterLeaf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeaf" ):
                listener.exitLeaf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeaf" ):
                return visitor.visitLeaf(self)
            else:
                return visitor.visitChildren(self)



    def int_tree(self):

        localctx = TreeParser.Int_treeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_int_tree)
        self._la = 0 # Token type
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = TreeParser.LeafContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 7
                self.match(TreeParser.INT)
                pass
            elif token in [1]:
                localctx = TreeParser.NodeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 8
                self.match(TreeParser.T__0)
                self.state = 9
                self.match(TreeParser.INT)
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 10
                    self.int_tree()
                    self.state = 13 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==1 or _la==3):
                        break

                self.state = 15
                self.match(TreeParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





