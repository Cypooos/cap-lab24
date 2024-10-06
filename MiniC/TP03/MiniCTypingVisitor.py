# Visitor to *typecheck* MiniC files
from typing import List, NoReturn
from MiniCVisitor import MiniCVisitor
from MiniCParser import MiniCParser
from Lib.Errors import MiniCInternalError, MiniCTypeError

from enum import Enum


class BaseType(Enum):
    Float, Integer, Boolean, String = range(4)


# Basic Type Checking for MiniC programs.
class MiniCTypingVisitor(MiniCVisitor):

    def __init__(self):
        self._memorytypes = dict()  # id -> types
        # For now, we don't have real functions ...
        self._current_function = "main"

    # All typing errors goes here
    def _raise(self, ctx, for_what, *types):
        raise MiniCTypeError(
            'In function {}: Line {} col {}: invalid type for {}: {}'.format(
                self._current_function,
                ctx.start.line, ctx.start.column, for_what,
                ' and '.join(t.name.lower() for t in types)))

    # "equality operands ONLY" -- only comparaisons
    def _assertSameType(self, ctx, for_what, *types):
        if not all(types[0] == t for t in types):
            raise MiniCTypeError(
                'In function {}: Line {} col {}: type mismatch for {}: {}'.format(
                    self._current_function,
                    ctx.start.line, ctx.start.column, for_what,
                    ' and '.join(t.name.lower() for t in types)))

    def _raiseNonType(self, ctx, message) -> NoReturn:
        raise MiniCTypeError(
            'In function {}: Line {} col {}: {}'.format(
                self._current_function,
                ctx.start.line, ctx.start.column, message))

    # type declaration
    def visitVarDecl(self, ctx) -> None:
        varnames = self.visit(ctx.id_l())
        inner_type = self.visit(ctx.typee())
        for varname in varnames:
            if self._memorytypes.get(varname, None) == None:
                self._memorytypes[varname] = inner_type
            else:
                self._raiseNonType(ctx,
                    f'Variable {varname} already declared')


    def visitBasicType(self, ctx):
        assert ctx.mytype is not None
        if ctx.mytype.type == MiniCParser.INTTYPE:
            return BaseType.Integer
        elif ctx.mytype.type == MiniCParser.FLOATTYPE:
            return BaseType.Float
        elif ctx.mytype.type == MiniCParser.BOOLTYPE:
            return BaseType.Boolean
        elif ctx.mytype.type == MiniCParser.STRINGTYPE:
            return BaseType.String
        else:
            self._raiseNonType(ctx,
                "Unknow type {}".format(ctx.mytype.getText()))

    def visitIdList(self, ctx) -> List[str]:
        v = self.visit(ctx.id_l())
        v.append(ctx.ID().getText()) # will actually reverse the list too
        return v

    def visitIdListBase(self, ctx) -> List[str]:
        return [ctx.ID().getText()]

    # typing visitors for expressions, statements !

    # visitors for atoms --> type
    def visitParExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitIntAtom(self, ctx):
        return BaseType.Integer

    def visitFloatAtom(self, ctx):
        return BaseType.Float

    def visitBooleanAtom(self, ctx):
        return BaseType.Boolean

    def visitIdAtom(self, ctx):
        try:
            return self._memorytypes[ctx.getText()]
        except KeyError:
            self._raiseNonType(ctx,
                               "Undefined variable {}".format(ctx.getText()))

    def visitStringAtom(self, ctx):
        return BaseType.String

    # now visit expr

    def visitAtomExpr(self, ctx):
        return self.visit(ctx.atom())

    def visitOrExpr(self, ctx):
        type_left = self.visit(ctx.expr(0))
        type_right = self.visit(ctx.expr(1))
        if type_left != BaseType.Boolean or type_right != BaseType.Boolean:
            self._raise(ctx, 'or statement', type_left, type_right)
        return BaseType.Boolean

    def visitAndExpr(self, ctx):
        type_left = self.visit(ctx.expr(0))
        type_right = self.visit(ctx.expr(1))
        if type_left != BaseType.Boolean or type_right != BaseType.Boolean:
            self._raise(ctx, 'and statement', type_left)
        return BaseType.Boolean

    def visitEqualityExpr(self, ctx):
        type_left = self.visit(ctx.expr(0))
        type_right = self.visit(ctx.expr(1))
        if type_left != type_right:
            self._assertSameType(ctx, 'equality', type_left, type_right)
        return BaseType.Boolean

    def visitRelationalExpr(self, ctx):
        type_left = self.visit(ctx.expr(0))
        type_right = self.visit(ctx.expr(1))
        if type_left != type_right:
            self._assertSameType(ctx, 'comparaison operator', type_left, type_right)
        if type_left != BaseType.Float and type_left != BaseType.Integer:
            self._raise(ctx, 'comparaison operator', type_left)
        return BaseType.Boolean

    def visitAdditiveExpr(self, ctx):
        assert ctx.myop is not None
        type_left = self.visit(ctx.expr(0))
        type_right = self.visit(ctx.expr(1))
        if type_left != type_right:
            self._assertSameType(ctx, 'additive operands', type_left, type_right)
        if type_left == BaseType.Boolean:
            self._raise(ctx, 'additive operands', type_left, type_right)
        return type_left

    def visitMultiplicativeExpr(self, ctx):
        assert ctx.myop is not None
        type_left = self.visit(ctx.expr(0))
        type_right = self.visit(ctx.expr(1))
        if type_left != type_right:
            self._raise(ctx, 'multiplicative operands', type_left, type_right)
        if type_left != BaseType.Float and type_left != BaseType.Integer:
            self._raise(ctx, 'multiplicative operands', type_left)
        if  ctx.myop.type == MiniCParser.MOD and type_left != BaseType.Integer:
            self._raise(ctx, 'modulo', type_left)
        return type_left

    def visitNotExpr(self, ctx):
        type_inner = self.visit(ctx.expr())
        if type_inner != BaseType.Boolean:
            self._raise(ctx, 'not expression', type_inner)
        return BaseType.Boolean

    def visitUnaryMinusExpr(self, ctx):
        type_inner = self.visit(ctx.expr())
        if type_inner != BaseType.Integer  and type_inner != BaseType.Float:
            self._raise(ctx, 'unary minus', type_inner)
        return type_inner

    # visit statements

    def visitPrintlnintStat(self, ctx):
        etype = self.visit(ctx.expr())
        if etype != BaseType.Integer:
            self._raise(ctx, 'println_int statement', etype)

    def visitPrintlnfloatStat(self, ctx):
        etype = self.visit(ctx.expr())
        if etype != BaseType.Float:
            self._raise(ctx, 'println_float statement', etype)

    def visitPrintlnboolStat(self, ctx):
        etype = self.visit(ctx.expr())
        if etype != BaseType.Boolean:
            self._raise(ctx, 'println_bool statement', etype)

    def visitPrintlnstringStat(self, ctx):
        etype = self.visit(ctx.expr())
        if etype != BaseType.String:
            self._raise(ctx, 'println_string statement', etype)

    def visitAssignStat(self, ctx):
        val_tp = self.visit(ctx.expr())
        var_name = ctx.ID().getText()
        if not var_name in self._memorytypes:
            self._raiseNonType(ctx, f'Undefined variable {var_name}')
        if self._memorytypes[var_name] != val_tp:
            self._assertSameType(ctx, var_name, self._memorytypes[var_name], val_tp)
        return val_tp # assignement are expressions that returns the value in C


    def visitIfStat(self, ctx) -> None:
        cond = self.visit(ctx.expr())
        if cond != BaseType.Boolean:
            self._raise(ctx, 'if statement', cond)
        self.visit(ctx.then_block)
        if ctx.else_block != None:
            self.visit(ctx.else_block)

    def visitWhileStat(self, ctx) -> None:
        cond = self.visit(ctx.expr())
        if cond != BaseType.Boolean:
            self._raise(ctx, 'while loop', cond)
        self.visit(ctx.body())