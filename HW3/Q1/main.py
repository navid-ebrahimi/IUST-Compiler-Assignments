from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from antlr4.TokenStreamRewriter import TokenStreamRewriter
from gen.JavaParser import JavaParser
from gen.JavaLexer import JavaLexer
from gen.JavaParserListener import JavaParserListener

class ClassListener(JavaParserListener):
    def __init__(self):
        self.dictionary = {"public": [], "private": [], "protected": []}
        self.counter = 1

    def enterClassBodyDeclaration(self, ctx: JavaParser.ClassBodyDeclarationContext):
        class_modifier = ctx.modifier()[0].classOrInterfaceModifier().getText()
        try:
            self.dictionary[f"{class_modifier}"].append(ctx.memberDeclaration().methodDeclaration().identifier().getText())
        except:
            try:
                self.dictionary[f"{class_modifier}"].append(ctx.memberDeclaration().classDeclaration().identifier().getText())
            except:
                self.dictionary[f"{class_modifier}"].append(ctx.memberDeclaration().fieldDeclaration().variableDeclarators().variableDeclarator()[0].variableDeclaratorId().identifier().getText())


    def exitTypeDeclaration(self, ctx:JavaParser.TypeDeclarationContext):
        print("Class " + str(self.counter))
        self.counter+=1
        print("public: ", end=' ')
        print(', '.join(self.dictionary["public"]))
        print("private: ", end=' ')
        print(', '.join(self.dictionary["private"]))
        print("protected: ", end=' ')
        print(', '.join(self.dictionary["protected"]))
        self.dictionary["public"] = []
        self.dictionary["private"] = []
        self.dictionary["protected"] = []



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

