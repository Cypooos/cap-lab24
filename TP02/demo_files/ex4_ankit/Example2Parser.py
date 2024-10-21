# Generated from Example2.g4 by ANTLR 4.12.0
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
        4,1,6,22,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,3,1,20,8,1,1,1,0,0,2,0,2,0,0,22,0,4,1,0,0,0,
        2,19,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,20,1,0,0,0,8,
        9,5,1,0,0,9,10,3,2,1,0,10,11,5,2,0,0,11,12,3,2,1,0,12,20,1,0,0,0,
        13,14,5,3,0,0,14,15,3,2,1,0,15,16,5,4,0,0,16,17,3,2,1,0,17,20,1,
        0,0,0,18,20,1,0,0,0,19,7,1,0,0,0,19,8,1,0,0,0,19,13,1,0,0,0,19,18,
        1,0,0,0,20,3,1,0,0,0,1,19
    ]

class Example2Parser ( Parser ):

    grammarFileName = "Example2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "CHARS", "EMP" ]

    RULE_full_expr = 0
    RULE_expr = 1

    ruleNames =  [ "full_expr", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    CHARS=5
    EMP=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Full_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(Example2Parser.ExprContext,0)


        def EOF(self):
            return self.getToken(Example2Parser.EOF, 0)

        def getRuleIndex(self):
            return Example2Parser.RULE_full_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFull_expr" ):
                listener.enterFull_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFull_expr" ):
                listener.exitFull_expr(self)




    def full_expr(self):

        localctx = Example2Parser.Full_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_full_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr()
            self.state = 5
            self.match(Example2Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Example2Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Example2Parser.ExprContext,i)


        def getRuleIndex(self):
            return Example2Parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = Example2Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 19
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 8
                self.match(Example2Parser.T__0)
                self.state = 9
                self.expr()
                self.state = 10
                self.match(Example2Parser.T__1)
                self.state = 11
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 13
                self.match(Example2Parser.T__2)
                self.state = 14
                self.expr()
                self.state = 15
                self.match(Example2Parser.T__3)
                self.state = 16
                self.expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





