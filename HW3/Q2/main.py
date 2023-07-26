from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from antlr4.TokenStreamRewriter import TokenStreamRewriter
from gen.JavaParser import JavaParser
from gen.JavaLexer import JavaLexer
from gen.JavaParserListener import JavaParserListener

class ClassListener(JavaParserListener):
    def __init__(self):
        self.counter = 0
        self.max_count = 0

    def enterStatement(self, ctx:JavaParser.StatementContext):
        try:
            if (ctx.FOR().getText() == 'for'):
                self.counter += 1
            self.max_count = max(self.max_count, self.counter)
        except:
            try:
                if (ctx.WHILE().getText() == 'while'):
                    self.counter += 1
                self.max_count = max(self.max_count, self.counter)
            except:
                pass


    def exitBlock(self, ctx:JavaParser.BlockContext):
        self.counter -= 1

    def exitTypeDeclaration(self, ctx:JavaParser.TypeDeclarationContext):
        print(self.max_count)
        self.counter = 0
        self.max_count = 0



sentences = ""
with open("Sample.java", "r") as myfile:
    sentences = myfile.read()
input_stream = InputStream(sentences)
lexer = JavaLexer(input_stream)
common_token = CommonTokenStream(lexer)
parser = JavaParser(common_token)
tree = parser.compilationUnit()
listener = ClassListener()
walker = ParseTreeWalker()
walker.walk(listener, tree)

