from antlr4 import *
from gen.CPP14Lexer import CPP14Lexer
from gen.CPP14Parser import CPP14Parser

with open('Sample1.cpp', 'r') as f:
    input_file = f.read()

lexer = CPP14Lexer(InputStream(input_file))
tokens = CommonTokenStream(lexer)
parser = CPP14Parser(tokens)
tree = parser.translationUnit()


