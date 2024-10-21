from TreeLexer import TreeLexer
from TreeParser import TreeParser
from MyTreeVisitor import MyTreeVisitor, UnknownIdentifier

from antlr4 import InputStream, CommonTokenStream
import sys

4

def main():
    lexer = TreeLexer(InputStream(sys.stdin.read()))
    stream = CommonTokenStream(lexer)
    parser = TreeParser(stream)
    tree = parser.int_tree_top()
    print("Parsing : done.")
    visitor = MyTreeVisitor()
    is_binary_tree: bool = visitor.visit(tree)
    print("Is it a binary tree ? " + str(is_binary_tree))


if __name__ == '__main__':
    main()
