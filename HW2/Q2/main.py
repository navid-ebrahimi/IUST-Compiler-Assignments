from antlr4 import *
from gen.PythonLexer import PythonLexer
from gen.PythonParser import PythonParser

URL="www.pythonanywhere.com"

lexer = PythonLexer(InputStream(URL))
tokens = CommonTokenStream(lexer)
parser = PythonParser(tokens)
tree = parser.url()

