from gen.JavaLexer import JavaLexer
from gen.JavaParser import JavaParser
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from antlr4.TokenStreamRewriter import TokenStreamRewriter
from gen.JavaParserVisitor import JavaParserVisitor
from antlr4.TokenStreamRewriter import TokenStreamRewriter


class MyJavaVisitor(JavaParserVisitor):
    def __init__(self, rewriter: TokenStreamRewriter):
        self.children = []
        self.rewriter = rewriter

    def visitMethodBody(self, ctx:JavaParser.MethodBodyContext):
        s = "\n\t\tthrow new UnsupportedOperationException();\n\t"
        if (len(ctx.children[0].children) == 2):
            self.rewriter.replace(from_idx=ctx.children[0].start.tokenIndex+1, to_idx=ctx.children[0].stop.tokenIndex-1, text=s, program_name=self.rewriter.DEFAULT_PROGRAM_NAME)


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

