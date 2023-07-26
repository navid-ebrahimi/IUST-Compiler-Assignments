# Generated from E:/university software/git/Compiler/project/Phase1/test\XMLParser.g4 by ANTLR 4.12.0
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
        4,1,18,63,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,5,0,29,8,0,10,0,12,0,32,9,0,1,0,3,0,35,8,0,1,1,3,1,38,8,1,1,1,
        1,1,1,1,1,1,1,1,3,1,45,8,1,1,1,3,1,48,8,1,5,1,50,8,1,10,1,12,1,53,
        9,1,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,2,1,0,
        4,5,2,0,6,6,9,9,67,0,34,1,0,0,0,2,37,1,0,0,0,4,54,1,0,0,0,6,56,1,
        0,0,0,8,60,1,0,0,0,10,11,5,7,0,0,11,15,5,16,0,0,12,14,3,6,3,0,13,
        12,1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,18,1,0,0,
        0,17,15,1,0,0,0,18,19,5,10,0,0,19,20,3,2,1,0,20,21,5,7,0,0,21,22,
        5,13,0,0,22,23,5,16,0,0,23,24,5,10,0,0,24,35,1,0,0,0,25,26,5,7,0,
        0,26,30,5,16,0,0,27,29,3,6,3,0,28,27,1,0,0,0,29,32,1,0,0,0,30,28,
        1,0,0,0,30,31,1,0,0,0,31,33,1,0,0,0,32,30,1,0,0,0,33,35,5,12,0,0,
        34,10,1,0,0,0,34,25,1,0,0,0,35,1,1,0,0,0,36,38,3,8,4,0,37,36,1,0,
        0,0,37,38,1,0,0,0,38,51,1,0,0,0,39,45,3,0,0,0,40,45,3,4,2,0,41,45,
        5,2,0,0,42,45,5,18,0,0,43,45,5,1,0,0,44,39,1,0,0,0,44,40,1,0,0,0,
        44,41,1,0,0,0,44,42,1,0,0,0,44,43,1,0,0,0,45,47,1,0,0,0,46,48,3,
        8,4,0,47,46,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,49,44,1,0,0,0,50,
        53,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,3,1,0,0,0,53,51,1,0,0,
        0,54,55,7,0,0,0,55,5,1,0,0,0,56,57,5,16,0,0,57,58,5,14,0,0,58,59,
        5,15,0,0,59,7,1,0,0,0,60,61,7,1,0,0,61,9,1,0,0,0,7,15,30,34,37,44,
        47,51
    ]

class XMLParser ( Parser ):

    grammarFileName = "XMLParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'<'", "<INVALID>", 
                     "<INVALID>", "'>'", "<INVALID>", "'/>'", "'/'", "'='" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "CDATA", "DTD", "EntityRef", 
                      "CharRef", "SEA_WS", "OPEN", "XMLDeclOpen", "TEXT", 
                      "CLOSE", "SPECIAL_CLOSE", "SLASH_CLOSE", "SLASH", 
                      "EQUALS", "STRING", "Name", "S", "PI" ]

    RULE_widget = 0
    RULE_content = 1
    RULE_reference = 2
    RULE_attribute = 3
    RULE_chardata = 4

    ruleNames =  [ "widget", "content", "reference", "attribute", "chardata" ]

    EOF = Token.EOF
    COMMENT=1
    CDATA=2
    DTD=3
    EntityRef=4
    CharRef=5
    SEA_WS=6
    OPEN=7
    XMLDeclOpen=8
    TEXT=9
    CLOSE=10
    SPECIAL_CLOSE=11
    SLASH_CLOSE=12
    SLASH=13
    EQUALS=14
    STRING=15
    Name=16
    S=17
    PI=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class WidgetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.OPEN)
            else:
                return self.getToken(XMLParser.OPEN, i)

        def Name(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.Name)
            else:
                return self.getToken(XMLParser.Name, i)

        def CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CLOSE)
            else:
                return self.getToken(XMLParser.CLOSE, i)

        def content(self):
            return self.getTypedRuleContext(XMLParser.ContentContext,0)


        def SLASH(self):
            return self.getToken(XMLParser.SLASH, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XMLParser.AttributeContext,i)


        def SLASH_CLOSE(self):
            return self.getToken(XMLParser.SLASH_CLOSE, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_widget

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWidget" ):
                listener.enterWidget(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWidget" ):
                listener.exitWidget(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWidget" ):
                return visitor.visitWidget(self)
            else:
                return visitor.visitChildren(self)




    def widget(self):

        localctx = XMLParser.WidgetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_widget)
        self._la = 0 # Token type
        try:
            self.state = 34
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.match(XMLParser.OPEN)
                self.state = 11
                self.match(XMLParser.Name)
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==16:
                    self.state = 12
                    self.attribute()
                    self.state = 17
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 18
                self.match(XMLParser.CLOSE)
                self.state = 19
                self.content()
                self.state = 20
                self.match(XMLParser.OPEN)
                self.state = 21
                self.match(XMLParser.SLASH)
                self.state = 22
                self.match(XMLParser.Name)
                self.state = 23
                self.match(XMLParser.CLOSE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.match(XMLParser.OPEN)
                self.state = 26
                self.match(XMLParser.Name)
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==16:
                    self.state = 27
                    self.attribute()
                    self.state = 32
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 33
                self.match(XMLParser.SLASH_CLOSE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def chardata(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.ChardataContext)
            else:
                return self.getTypedRuleContext(XMLParser.ChardataContext,i)


        def widget(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.WidgetContext)
            else:
                return self.getTypedRuleContext(XMLParser.WidgetContext,i)


        def reference(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.ReferenceContext)
            else:
                return self.getTypedRuleContext(XMLParser.ReferenceContext,i)


        def CDATA(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CDATA)
            else:
                return self.getToken(XMLParser.CDATA, i)

        def PI(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.PI)
            else:
                return self.getToken(XMLParser.PI, i)

        def COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.COMMENT)
            else:
                return self.getToken(XMLParser.COMMENT, i)

        def getRuleIndex(self):
            return XMLParser.RULE_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContent" ):
                listener.enterContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContent" ):
                listener.exitContent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContent" ):
                return visitor.visitContent(self)
            else:
                return visitor.visitChildren(self)




    def content(self):

        localctx = XMLParser.ContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==9:
                self.state = 36
                self.chardata()


            self.state = 51
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 44
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [7]:
                        self.state = 39
                        self.widget()
                        pass
                    elif token in [4, 5]:
                        self.state = 40
                        self.reference()
                        pass
                    elif token in [2]:
                        self.state = 41
                        self.match(XMLParser.CDATA)
                        pass
                    elif token in [18]:
                        self.state = 42
                        self.match(XMLParser.PI)
                        pass
                    elif token in [1]:
                        self.state = 43
                        self.match(XMLParser.COMMENT)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 47
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==6 or _la==9:
                        self.state = 46
                        self.chardata()

             
                self.state = 53
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReferenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EntityRef(self):
            return self.getToken(XMLParser.EntityRef, 0)

        def CharRef(self):
            return self.getToken(XMLParser.CharRef, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReference" ):
                listener.enterReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReference" ):
                listener.exitReference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReference" ):
                return visitor.visitReference(self)
            else:
                return visitor.visitChildren(self)




    def reference(self):

        localctx = XMLParser.ReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_reference)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Name(self):
            return self.getToken(XMLParser.Name, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = XMLParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(XMLParser.Name)
            self.state = 57
            self.match(XMLParser.EQUALS)
            self.state = 58
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChardataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(XMLParser.TEXT, 0)

        def SEA_WS(self):
            return self.getToken(XMLParser.SEA_WS, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_chardata

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChardata" ):
                listener.enterChardata(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChardata" ):
                listener.exitChardata(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChardata" ):
                return visitor.visitChardata(self)
            else:
                return visitor.visitChildren(self)




    def chardata(self):

        localctx = XMLParser.ChardataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_chardata)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            _la = self._input.LA(1)
            if not(_la==6 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





