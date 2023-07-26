# Generated from E:/university software/git/Compiler/project/Phase1/test\XMLParser.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .XMLParser import XMLParser
else:
    from XMLParser import XMLParser

# This class defines a complete generic visitor for a parse tree produced by XMLParser.

class XMLParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by XMLParser#widget.
    def visitWidget(self, ctx:XMLParser.WidgetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#content.
    def visitContent(self, ctx:XMLParser.ContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#reference.
    def visitReference(self, ctx:XMLParser.ReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#attribute.
    def visitAttribute(self, ctx:XMLParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#chardata.
    def visitChardata(self, ctx:XMLParser.ChardataContext):
        return self.visitChildren(ctx)



del XMLParser