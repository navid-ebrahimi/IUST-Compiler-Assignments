# Generated from E:/university software/git/Compiler/project/Phase1/test\XMLParser.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .XMLParser import XMLParser
else:
    from XMLParser import XMLParser

# This class defines a complete listener for a parse tree produced by XMLParser.
class XMLParserListener(ParseTreeListener):

    # Enter a parse tree produced by XMLParser#widget.
    def enterWidget(self, ctx:XMLParser.WidgetContext):
        pass

    # Exit a parse tree produced by XMLParser#widget.
    def exitWidget(self, ctx:XMLParser.WidgetContext):
        pass


    # Enter a parse tree produced by XMLParser#content.
    def enterContent(self, ctx:XMLParser.ContentContext):
        pass

    # Exit a parse tree produced by XMLParser#content.
    def exitContent(self, ctx:XMLParser.ContentContext):
        pass


    # Enter a parse tree produced by XMLParser#reference.
    def enterReference(self, ctx:XMLParser.ReferenceContext):
        pass

    # Exit a parse tree produced by XMLParser#reference.
    def exitReference(self, ctx:XMLParser.ReferenceContext):
        pass


    # Enter a parse tree produced by XMLParser#attribute.
    def enterAttribute(self, ctx:XMLParser.AttributeContext):
        pass

    # Exit a parse tree produced by XMLParser#attribute.
    def exitAttribute(self, ctx:XMLParser.AttributeContext):
        pass


    # Enter a parse tree produced by XMLParser#chardata.
    def enterChardata(self, ctx:XMLParser.ChardataContext):
        pass

    # Exit a parse tree produced by XMLParser#chardata.
    def exitChardata(self, ctx:XMLParser.ChardataContext):
        pass



del XMLParser