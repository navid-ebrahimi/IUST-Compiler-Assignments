from gen.JavaLexer import JavaLexer
from gen.JavaParser import JavaParser
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from gen.JavaParserVisitor import JavaParserVisitor
from antlr4.TokenStreamRewriter import TokenStreamRewriter


class MyJavaVisitor(JavaParserVisitor):
    def __init__(self, rewriter: TokenStreamRewriter):
        self.children = []
        self.rewriter = rewriter


    def visitClassBodyDeclaration(self, ctx:JavaParser.ClassBodyContext):
        for child in ctx.children:
          if (isinstance(child, JavaParser.ModifierContext)):
              self.children.append(child.getText())
          if (isinstance(child, JavaParser.MemberDeclarationContext)):
              self.visit(child)
        s = ""
        if (len(self.children) > 2):
            if (self.children[1] != "final"):
                s += f"\n\tpublic set{self.children[2]}({self.children[1]} value)\n\t{{\n\t\t{self.children[2]}=value;\n\t}}\n\tpublic {self.children[1]} get{self.children[2]}()\n\t{{\n\t\treturn {self.children[2]};\n\t}}\n\t"
                self.rewriter.replace(from_idx=ctx.children[len(ctx.children)-1].stop.tokenIndex+1, to_idx=ctx.children[len(ctx.children)-1].stop.tokenIndex+1, text=s, program_name=self.rewriter.DEFAULT_PROGRAM_NAME)
            else:
                s += f"\n\tpublic {self.children[2]} get{self.children[3]}()\n\t{{\n\t\treturn {self.children[3]}\n\t}}\n\t"
                self.rewriter.replace(from_idx=ctx.children[len(ctx.children)-1].stop.tokenIndex+1, to_idx=ctx.children[len(ctx.children)-1].stop.tokenIndex+1, text=s, program_name=self.rewriter.DEFAULT_PROGRAM_NAME)

        self.children = []

    def visitFieldDeclaration(self, ctx:JavaParser.FieldDeclarationContext):
        for child in ctx.children:
            if (isinstance(child, JavaParser.TypeTypeContext) or isinstance(child, JavaParser.VariableDeclaratorsContext)):
                self.children.append(child.getText())


with open("Sample.java", "r") as myfile:
    sentences = myfile.read()
input_stream = InputStream(sentences)
lexer = JavaLexer(input_stream)
common_token = CommonTokenStream(lexer)
parser = JavaParser(common_token)
tree = parser.compilationUnit()
rewriter = TokenStreamRewriter(common_token)
visitor = MyJavaVisitor(rewriter)
ast = visitor.visit(tree)
print(rewriter.getText(rewriter.DEFAULT_PROGRAM_NAME, 0, len(common_token.tokens)))
