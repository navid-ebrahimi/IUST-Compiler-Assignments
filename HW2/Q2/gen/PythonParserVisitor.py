# Generated from /home/navid/Desktop/Com/Q2/PythonParser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PythonParser import PythonParser
else:
    from PythonParser import PythonParser

# This class defines a complete generic visitor for a parse tree produced by PythonParser.

class PythonParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PythonParser#url.
    def visitUrl(self, ctx:PythonParser.UrlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#scheme.
    def visitScheme(self, ctx:PythonParser.SchemeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#host.
    def visitHost(self, ctx:PythonParser.HostContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#subdomain.
    def visitSubdomain(self, ctx:PythonParser.SubdomainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#maindomain.
    def visitMaindomain(self, ctx:PythonParser.MaindomainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#topleveldomain.
    def visitTopleveldomain(self, ctx:PythonParser.TopleveldomainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#port.
    def visitPort(self, ctx:PythonParser.PortContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#path.
    def visitPath(self, ctx:PythonParser.PathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#query.
    def visitQuery(self, ctx:PythonParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#fragmentt.
    def visitFragmentt(self, ctx:PythonParser.FragmenttContext):
        return self.visitChildren(ctx)



del PythonParser