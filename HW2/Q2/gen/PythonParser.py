# Generated from /home/navid/Desktop/Com/Q2/PythonParser.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,26,59,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,3,0,24,8,0,1,0,3,0,27,8,0,
        1,0,3,0,30,8,0,1,0,3,0,33,8,0,1,1,1,1,1,2,3,2,38,8,2,1,2,1,2,1,2,
        1,2,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,
        1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,0,53,0,20,1,0,0,0,2,34,1,0,
        0,0,4,37,1,0,0,0,6,43,1,0,0,0,8,46,1,0,0,0,10,48,1,0,0,0,12,50,1,
        0,0,0,14,52,1,0,0,0,16,54,1,0,0,0,18,56,1,0,0,0,20,21,3,2,1,0,21,
        23,3,4,2,0,22,24,3,12,6,0,23,22,1,0,0,0,23,24,1,0,0,0,24,26,1,0,
        0,0,25,27,3,14,7,0,26,25,1,0,0,0,26,27,1,0,0,0,27,29,1,0,0,0,28,
        30,3,16,8,0,29,28,1,0,0,0,29,30,1,0,0,0,30,32,1,0,0,0,31,33,3,18,
        9,0,32,31,1,0,0,0,32,33,1,0,0,0,33,1,1,0,0,0,34,35,5,19,0,0,35,3,
        1,0,0,0,36,38,3,6,3,0,37,36,1,0,0,0,37,38,1,0,0,0,38,39,1,0,0,0,
        39,40,3,8,4,0,40,41,5,12,0,0,41,42,3,10,5,0,42,5,1,0,0,0,43,44,5,
        20,0,0,44,45,5,12,0,0,45,7,1,0,0,0,46,47,5,21,0,0,47,9,1,0,0,0,48,
        49,5,22,0,0,49,11,1,0,0,0,50,51,5,23,0,0,51,13,1,0,0,0,52,53,5,24,
        0,0,53,15,1,0,0,0,54,55,5,25,0,0,55,17,1,0,0,0,56,57,5,26,0,0,57,
        19,1,0,0,0,5,23,26,29,32,37
    ]

class PythonParser ( Parser ):

    grammarFileName = "PythonParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'&'", "'='", "'+'", "'#'", "'.'", "'/'", "'-'", "'_'", 
                     "'?'", "'%'" ]

    symbolicNames = [ "<INVALID>", "PART1", "PART2", "PART3", "PART4", "PART5", 
                      "PART6", "WS", "AMP", "EQ", "PLUS", "HASH", "DOT", 
                      "SLASH", "DASH", "UNDERSCORE", "QUESTION", "PERCENT", 
                      "UNKNOWN", "SCHEME", "SUBDOMAIN", "MAINDOMAIN", "TOPLEVELDOMAIN", 
                      "PORT", "PATH", "QUERY", "FRAGMENT" ]

    RULE_url = 0
    RULE_scheme = 1
    RULE_host = 2
    RULE_subdomain = 3
    RULE_maindomain = 4
    RULE_topleveldomain = 5
    RULE_port = 6
    RULE_path = 7
    RULE_query = 8
    RULE_fragmentt = 9

    ruleNames =  [ "url", "scheme", "host", "subdomain", "maindomain", "topleveldomain", 
                   "port", "path", "query", "fragmentt" ]

    EOF = Token.EOF
    PART1=1
    PART2=2
    PART3=3
    PART4=4
    PART5=5
    PART6=6
    WS=7
    AMP=8
    EQ=9
    PLUS=10
    HASH=11
    DOT=12
    SLASH=13
    DASH=14
    UNDERSCORE=15
    QUESTION=16
    PERCENT=17
    UNKNOWN=18
    SCHEME=19
    SUBDOMAIN=20
    MAINDOMAIN=21
    TOPLEVELDOMAIN=22
    PORT=23
    PATH=24
    QUERY=25
    FRAGMENT=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class UrlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scheme(self):
            return self.getTypedRuleContext(PythonParser.SchemeContext,0)


        def host(self):
            return self.getTypedRuleContext(PythonParser.HostContext,0)


        def port(self):
            return self.getTypedRuleContext(PythonParser.PortContext,0)


        def path(self):
            return self.getTypedRuleContext(PythonParser.PathContext,0)


        def query(self):
            return self.getTypedRuleContext(PythonParser.QueryContext,0)


        def fragmentt(self):
            return self.getTypedRuleContext(PythonParser.FragmenttContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_url

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUrl" ):
                listener.enterUrl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUrl" ):
                listener.exitUrl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUrl" ):
                return visitor.visitUrl(self)
            else:
                return visitor.visitChildren(self)




    def url(self):

        localctx = PythonParser.UrlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_url)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.scheme()
            self.state = 21
            self.host()
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 22
                self.port()


            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 25
                self.path()


            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 28
                self.query()


            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 31
                self.fragmentt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SchemeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCHEME(self):
            return self.getToken(PythonParser.SCHEME, 0)

        def getRuleIndex(self):
            return PythonParser.RULE_scheme

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScheme" ):
                listener.enterScheme(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScheme" ):
                listener.exitScheme(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScheme" ):
                return visitor.visitScheme(self)
            else:
                return visitor.visitChildren(self)




    def scheme(self):

        localctx = PythonParser.SchemeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_scheme)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(PythonParser.SCHEME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HostContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def maindomain(self):
            return self.getTypedRuleContext(PythonParser.MaindomainContext,0)


        def DOT(self):
            return self.getToken(PythonParser.DOT, 0)

        def topleveldomain(self):
            return self.getTypedRuleContext(PythonParser.TopleveldomainContext,0)


        def subdomain(self):
            return self.getTypedRuleContext(PythonParser.SubdomainContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_host

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHost" ):
                listener.enterHost(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHost" ):
                listener.exitHost(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHost" ):
                return visitor.visitHost(self)
            else:
                return visitor.visitChildren(self)




    def host(self):

        localctx = PythonParser.HostContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_host)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 36
                self.subdomain()


            self.state = 39
            self.maindomain()
            self.state = 40
            self.match(PythonParser.DOT)
            self.state = 41
            self.topleveldomain()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubdomainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBDOMAIN(self):
            return self.getToken(PythonParser.SUBDOMAIN, 0)

        def DOT(self):
            return self.getToken(PythonParser.DOT, 0)

        def getRuleIndex(self):
            return PythonParser.RULE_subdomain

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubdomain" ):
                listener.enterSubdomain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubdomain" ):
                listener.exitSubdomain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubdomain" ):
                return visitor.visitSubdomain(self)
            else:
                return visitor.visitChildren(self)




    def subdomain(self):

        localctx = PythonParser.SubdomainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_subdomain)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(PythonParser.SUBDOMAIN)
            self.state = 44
            self.match(PythonParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MaindomainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAINDOMAIN(self):
            return self.getToken(PythonParser.MAINDOMAIN, 0)

        def getRuleIndex(self):
            return PythonParser.RULE_maindomain

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMaindomain" ):
                listener.enterMaindomain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMaindomain" ):
                listener.exitMaindomain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMaindomain" ):
                return visitor.visitMaindomain(self)
            else:
                return visitor.visitChildren(self)




    def maindomain(self):

        localctx = PythonParser.MaindomainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_maindomain)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(PythonParser.MAINDOMAIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopleveldomainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TOPLEVELDOMAIN(self):
            return self.getToken(PythonParser.TOPLEVELDOMAIN, 0)

        def getRuleIndex(self):
            return PythonParser.RULE_topleveldomain

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopleveldomain" ):
                listener.enterTopleveldomain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopleveldomain" ):
                listener.exitTopleveldomain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopleveldomain" ):
                return visitor.visitTopleveldomain(self)
            else:
                return visitor.visitChildren(self)




    def topleveldomain(self):

        localctx = PythonParser.TopleveldomainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_topleveldomain)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(PythonParser.TOPLEVELDOMAIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PortContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PORT(self):
            return self.getToken(PythonParser.PORT, 0)

        def getRuleIndex(self):
            return PythonParser.RULE_port

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPort" ):
                listener.enterPort(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPort" ):
                listener.exitPort(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPort" ):
                return visitor.visitPort(self)
            else:
                return visitor.visitChildren(self)




    def port(self):

        localctx = PythonParser.PortContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_port)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(PythonParser.PORT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PATH(self):
            return self.getToken(PythonParser.PATH, 0)

        def getRuleIndex(self):
            return PythonParser.RULE_path

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPath" ):
                listener.enterPath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPath" ):
                listener.exitPath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPath" ):
                return visitor.visitPath(self)
            else:
                return visitor.visitChildren(self)




    def path(self):

        localctx = PythonParser.PathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_path)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(PythonParser.PATH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUERY(self):
            return self.getToken(PythonParser.QUERY, 0)

        def getRuleIndex(self):
            return PythonParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)




    def query(self):

        localctx = PythonParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(PythonParser.QUERY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FragmenttContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FRAGMENT(self):
            return self.getToken(PythonParser.FRAGMENT, 0)

        def getRuleIndex(self):
            return PythonParser.RULE_fragmentt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFragmentt" ):
                listener.enterFragmentt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFragmentt" ):
                listener.exitFragmentt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFragmentt" ):
                return visitor.visitFragmentt(self)
            else:
                return visitor.visitChildren(self)




    def fragmentt(self):

        localctx = PythonParser.FragmenttContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_fragmentt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(PythonParser.FRAGMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





