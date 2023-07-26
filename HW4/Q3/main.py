from gen.JavaLexer import JavaLexer
from gen.JavaParser import JavaParser
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from antlr4.TokenStreamRewriter import TokenStreamRewriter
from gen.JavaParserVisitor import JavaParserVisitor
from antlr4.TokenStreamRewriter import TokenStreamRewriter


class MyJavaVisitor(JavaParserVisitor):
    def __init__(self, rewriter: TokenStreamRewriter):
        self.flag = False
        self.rewriter = rewriter

    def visitStatement(self, ctx:JavaParser.StatementContext):
        start = 0
        for child in ctx.children:
            if (isinstance(child, JavaParser.CatchClauseContext)):
                if (child.getText() == 'catch(Exceptione){}'):
                    self.flag = True

        s= ""
        if (not self.flag):
            s += f"\n\t\tcatch (Exception e)\n\t\t{{\n\t\t\tSystem.out.println(Exception message:  + e.getMessage());\n\t\t}}\n\t"
            self.rewriter.replace(from_idx=ctx.children[len(ctx.children)-1].stop.tokenIndex+1, to_idx=ctx.children[len(ctx.children)-1].stop.tokenIndex+1, text=s, program_name=self.rewriter.DEFAULT_PROGRAM_NAME)

        self.flag = False


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
