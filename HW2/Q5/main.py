from antlr4 import *
from gen.CPP14Lexer import CPP14Lexer
# from gen.CPP14Parser import CPP14Parser

with open('Sample.cpp', 'r') as f:
    input_file = f.read()

lexer = CPP14Lexer(InputStream(input_file))
token = lexer.nextToken()
while(token.type != token.EOF):
    text = token.text
    flag = False
    if (token.type == lexer.BlockComment):
        for i in range(len(text)):
            if (text[i] == '\n'):
                flag = True
                break
        if (not flag):
            token.type = lexer.LineComment
            print('//' + text[2:-2] + '//')
        else:
            print(text)
    else:
        print(text)

    token = lexer.nextToken()

