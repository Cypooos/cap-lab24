# Visitor to *interpret* MiniC files
from typing import (
  Dict,
  List)
from MiniCVisitor import MiniCVisitor
from MiniCParser import MiniCParser
from Lib.Errors import MiniCRuntimeError, MiniCInternalError, MiniCUnsupportedError

MINIC_VALUE = int | str | bool | float | List['MINIC_VALUE']

# I decided to consider int as 4 bytes, and implement overflow !
# Since python's int are unbounded, this simple lambda consider them like C with overflow
recenterInt = lambda x: ((x+2147483648) % 4294967296 )-2147483648


class MiniCInterpretVisitor(MiniCVisitor):

    _memory: Dict[str, MINIC_VALUE]

    def __init__(self):
        self._memory = dict()  # store all variable ids and values.
        self.has_main = False

    # visitors for variable declarations

    def visitVarDecl(self, ctx) -> None:
        # Initialise all variables in self._memory
        type_ele = ctx.typee().mytype.type
        varnames = self.visit(ctx.id_l())
        default = None
        match type_ele:
            case MiniCParser.INTTYPE: default = 0
            case MiniCParser.FLOATTYPE: default = 0.0
            case MiniCParser.BOOLTYPE: default = False
            case MiniCParser.STRINGTYPE: default = ""
            case _: raise NotImplementedError(f"Initialization for type {type_ele}")
        for x in varnames: self._memory[x] = default
        return None

    def visitIdList(self, ctx) -> List[str]:
        v = self.visit(ctx.id_l())
        v.append(ctx.ID().getText()) # will actually reverse the list too
        return v

    def visitIdListBase(self, ctx) -> List[str]:
        return [ctx.ID().getText()]

    # visitors for atoms --> value

    def visitParExpr(self, ctx) -> MINIC_VALUE:
        return self.visit(ctx.expr())

    def visitIntAtom(self, ctx) -> int:
        return recenterInt(int(ctx.getText()))

    def visitFloatAtom(self, ctx) -> float:
        return float(ctx.getText())

    def visitBooleanAtom(self, ctx) -> bool:
        return ctx.getText() == "true"

    def visitStringAtom(self, ctx) -> str:
        return ctx.getText()[1:-1]  # Remove the ""

    def visitIdAtom(self, ctx) -> MINIC_VALUE:
        ret = self._memory.get(ctx.getText(),None)
        if ret == None:
            raise MiniCRuntimeError("Undefined variable {}".format(ctx.getText()))
        return ret


    # visit expressions

    def visitAtomExpr(self, ctx) -> MINIC_VALUE:
        return self.visit(ctx.atom())

    def visitOrExpr(self, ctx) -> bool:
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        return lval or rval

    def visitAndExpr(self, ctx) -> bool:
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        return lval and rval

    def visitEqualityExpr(self, ctx) -> bool:
        assert ctx.myop is not None
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        # be careful for float equality
        if ctx.myop.type == MiniCParser.EQ:
            return lval == rval
        else:
            return lval != rval

    def visitRelationalExpr(self, ctx) -> bool:
        assert ctx.myop is not None
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        if ctx.myop.type == MiniCParser.LT:
            return lval < rval
        elif ctx.myop.type == MiniCParser.LTEQ:
            return lval <= rval
        elif ctx.myop.type == MiniCParser.GT:
            return lval > rval
        elif ctx.myop.type == MiniCParser.GTEQ:
            return lval >= rval
        else:
            raise MiniCInternalError(
                f"Unknown comparison operator '{ctx.myop}'"
            )

    def visitAdditiveExpr(self, ctx) -> MINIC_VALUE:
        assert ctx.myop is not None
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        if ctx.myop.type == MiniCParser.PLUS:
            if any(isinstance(x, str) for x in (lval, rval)):
                return '{}{}'.format(lval, rval)
            elif isinstance(lval, int):
                return recenterInt(lval + rval)
            else:
                return lval + rval
        elif ctx.myop.type == MiniCParser.MINUS:
            if isinstance(lval, int):
                return recenterInt(lval - rval)
            else:
                return lval - rval
        else:
            raise MiniCInternalError(
                f"Unknown additive operator '{ctx.myop}'")

    def visitMultiplicativeExpr(self, ctx) -> MINIC_VALUE:
        assert ctx.myop is not None
        lval = recenterInt(self.visit(ctx.expr(0)))
        rval = recenterInt(self.visit(ctx.expr(1)))
        if ctx.myop.type == MiniCParser.MULT:
            if isinstance(rval, int):
                return recenterInt(lval * rval) # we consider them with overflow like in C
            else:
                return lval * rval
        elif ctx.myop.type == MiniCParser.DIV:
            if isinstance(rval, int):
                if rval == 0:
                    raise MiniCRuntimeError("Division by 0")
                return int(lval/rval)
            if isinstance(rval,float):
                if rval == 0.0:
                    raise MiniCRuntimeError("Division by 0")
            return lval/rval
        elif ctx.myop.type == MiniCParser.MOD:
            if rval == 0:
                raise MiniCRuntimeError("Division by 0")
            return (abs(lval) % abs(rval)) if lval >0 else -(abs(lval) % abs(rval)) 
        else:
            raise MiniCInternalError(
                f"Unknown multiplicative operator '{ctx.myop}'")

    def visitNotExpr(self, ctx) -> bool:
        return not self.visit(ctx.expr())

    def visitUnaryMinusExpr(self, ctx) -> MINIC_VALUE:
        return recenterInt(-self.visit(ctx.expr())) # because -2147483648 = 2147483648 in C

    # visit statements

    def visitPrintlnintStat(self, ctx) -> None:
        val = self.visit(ctx.expr())
        print(val)

    def visitPrintlnfloatStat(self, ctx) -> None:
        val = self.visit(ctx.expr())
        if isinstance(val, float):
            val = f"{val:.2f}"
        print(val)

    def visitPrintlnboolStat(self, ctx) -> None:
        val = self.visit(ctx.expr())
        print('1' if val else '0')

    def visitPrintlnstringStat(self, ctx) -> None:
        val = self.visit(ctx.expr())
        print(val)

    def visitAssignStat(self, ctx) -> None:
        val = self.visit(ctx.expr())
        var_name = ctx.ID().getText()
        if not var_name in self._memory:
            raise MiniCRuntimeError("Undefined variable {}".format(var_name))
        self._memory[var_name] = val
        return val # assignement are expressions that returns the value in C

    def visitIfStat(self, ctx) -> None:
        cond = self.visit(ctx.expr())
        if cond == True:
            self.visit(ctx.then_block)
            return
        elif ctx.else_block != None:
            self.visit(ctx.else_block)

    def visitWhileStat(self, ctx) -> None:
        while self.visit(ctx.expr()):
            self.visit(ctx.body)
        return
    
    def visitForStat(self, ctx) -> None:
        if ctx.init != None: self.visit(ctx.init) # the first, middle and last can be empoty in C, so we check that they arn't None before executing them
        while self.visit(ctx.cond) if ctx.cond != None else True:
            self.visit(ctx.body)
            if ctx.looper != None: self.visit(ctx.looper)
    
    # TOPLEVEL
    def visitProgRule(self, ctx) -> None:
        self.visitChildren(ctx)
        if not self.has_main:
            # A program without a main function is compilable (hence
            # it's not a typing error per se), but not executable,
            # hence we consider it a runtime error.
            raise MiniCRuntimeError("No main function in file")

    # Visit a function: ignore if non main!
    def visitFuncDef(self, ctx) -> None:
        funname = ctx.ID().getText()
        if funname == "main":
            self.has_main = True
            self.visit(ctx.vardecl_l())
            self.visit(ctx.block())
        else:
            raise MiniCUnsupportedError("Functions are not supported in evaluation mode")

    def visitFuncCall(self, ctx) -> None:  # pragma: no cover
        raise MiniCUnsupportedError("Functions are not supported in evaluation mode")
