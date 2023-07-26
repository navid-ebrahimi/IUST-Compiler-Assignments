from antlr4 import *
from gen.CPP14Lexer import CPP14Lexer
# from gen.CPP14Parser import CPP14Parser

def PraceRecursion(lexer, token):
    list_tokens = []
    while(token.text != '{'):
        list_tokens.append(token.text)
        token = lexer.nextToken()
    list_tokens.append(token.text)
    token = lexer.nextToken()
    while(token.text != '}'):
        if (token.type == lexer.For or token.type == lexer.If or token.type == lexer.Else):
            list_tokens.extend(PraceRecursion(lexer, token))
        else:
            list_tokens.append(token.text)
        token = lexer.nextToken()
    if (list_tokens[len(list_tokens) - 1] != '}'):
        list_tokens.append('}')
    pure_tokens = []
    if (list_tokens.count(';') < 2):
        for i in range(len(list_tokens)):
            if (list_tokens[i] != '{' and list_tokens[i] != '}'):
                pure_tokens.append(list_tokens[i])
        return pure_tokens
    else:
        return list_tokens




with open('Sample.cpp', 'r') as f:
    input_file = f.read()

lexer = CPP14Lexer(InputStream(input_file))
token = lexer.nextToken()
pure_tokens = []
while(token.type != token.EOF):
    text = token.text
    counter = 0
    s = ""
    flag = False
    if (token.type == lexer.For or token.type == lexer.While or token.type == lexer.If or token.type == lexer.Else):
        pure_tokens.extend(PraceRecursion(lexer, token))
        for i in range(len(pure_tokens)):
            print(pure_tokens[i])
        flag = True
    if (not flag):
        print(text)
    token = lexer.nextToken()



