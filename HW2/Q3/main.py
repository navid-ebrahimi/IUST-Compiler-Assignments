from antlr4 import *
from gen.CPP14Lexer import CPP14Lexer
# from gen.CPP14Parser import CPP14Parser

with open('classes.cpp', 'r') as f:
    input_file = f.read()

lexer = CPP14Lexer(InputStream(input_file))
token = lexer.nextToken()
list_of_classNames = []
while(token.type != token.EOF):
    text = token.text
    if (token.type == lexer.Class):
        list_of_classNames.append(lexer.nextToken().text)

    token = lexer.nextToken()
print(list_of_classNames)
print(len(list_of_classNames))


