# Generated from /home/navid/Desktop/Com/Q2/PythonLexer.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,19,140,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,55,8,0,
        1,1,4,1,58,8,1,11,1,12,1,59,1,1,1,1,4,1,64,8,1,11,1,12,1,65,5,1,
        68,8,1,10,1,12,1,71,9,1,1,2,1,2,4,2,75,8,2,11,2,12,2,76,1,3,1,3,
        4,3,81,8,3,11,3,12,3,82,1,3,1,3,4,3,87,8,3,11,3,12,3,88,5,3,91,8,
        3,10,3,12,3,94,9,3,1,4,1,4,4,4,98,8,4,11,4,12,4,99,1,5,1,5,4,5,104,
        8,5,11,5,12,5,105,1,6,4,6,109,8,6,11,6,12,6,110,1,6,1,6,1,7,1,7,
        1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,
        1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,18,1,18,0,0,19,1,1,3,2,
        5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,
        15,31,16,33,17,35,18,37,19,1,0,5,3,0,48,57,65,90,97,122,1,0,48,57,
        5,0,37,38,48,57,61,61,65,90,97,122,5,0,45,45,48,57,65,90,95,95,97,
        122,3,0,9,10,13,13,32,32,150,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,
        0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,
        17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,
        27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,
        37,1,0,0,0,1,54,1,0,0,0,3,57,1,0,0,0,5,72,1,0,0,0,7,78,1,0,0,0,9,
        95,1,0,0,0,11,101,1,0,0,0,13,108,1,0,0,0,15,114,1,0,0,0,17,116,1,
        0,0,0,19,118,1,0,0,0,21,120,1,0,0,0,23,122,1,0,0,0,25,124,1,0,0,
        0,27,126,1,0,0,0,29,128,1,0,0,0,31,130,1,0,0,0,33,132,1,0,0,0,35,
        134,1,0,0,0,37,136,1,0,0,0,39,40,5,104,0,0,40,41,5,116,0,0,41,42,
        5,116,0,0,42,43,5,112,0,0,43,44,5,58,0,0,44,45,5,47,0,0,45,55,5,
        47,0,0,46,47,5,104,0,0,47,48,5,116,0,0,48,49,5,116,0,0,49,50,5,112,
        0,0,50,51,5,115,0,0,51,52,5,58,0,0,52,53,5,47,0,0,53,55,5,47,0,0,
        54,39,1,0,0,0,54,46,1,0,0,0,55,2,1,0,0,0,56,58,7,0,0,0,57,56,1,0,
        0,0,58,59,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,69,1,0,0,0,61,63,
        3,25,12,0,62,64,7,0,0,0,63,62,1,0,0,0,64,65,1,0,0,0,65,63,1,0,0,
        0,65,66,1,0,0,0,66,68,1,0,0,0,67,61,1,0,0,0,68,71,1,0,0,0,69,67,
        1,0,0,0,69,70,1,0,0,0,70,4,1,0,0,0,71,69,1,0,0,0,72,74,3,19,9,0,
        73,75,7,1,0,0,74,73,1,0,0,0,75,76,1,0,0,0,76,74,1,0,0,0,76,77,1,
        0,0,0,77,6,1,0,0,0,78,80,3,27,13,0,79,81,7,0,0,0,80,79,1,0,0,0,81,
        82,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,92,1,0,0,0,84,86,3,27,
        13,0,85,87,7,0,0,0,86,85,1,0,0,0,87,88,1,0,0,0,88,86,1,0,0,0,88,
        89,1,0,0,0,89,91,1,0,0,0,90,84,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,
        0,92,93,1,0,0,0,93,8,1,0,0,0,94,92,1,0,0,0,95,97,3,33,16,0,96,98,
        7,2,0,0,97,96,1,0,0,0,98,99,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,
        100,10,1,0,0,0,101,103,3,23,11,0,102,104,7,3,0,0,103,102,1,0,0,0,
        104,105,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,12,1,0,0,0,107,
        109,7,4,0,0,108,107,1,0,0,0,109,110,1,0,0,0,110,108,1,0,0,0,110,
        111,1,0,0,0,111,112,1,0,0,0,112,113,6,6,0,0,113,14,1,0,0,0,114,115,
        5,38,0,0,115,16,1,0,0,0,116,117,5,61,0,0,117,18,1,0,0,0,118,119,
        5,58,0,0,119,20,1,0,0,0,120,121,5,43,0,0,121,22,1,0,0,0,122,123,
        5,35,0,0,123,24,1,0,0,0,124,125,5,46,0,0,125,26,1,0,0,0,126,127,
        5,47,0,0,127,28,1,0,0,0,128,129,5,45,0,0,129,30,1,0,0,0,130,131,
        5,95,0,0,131,32,1,0,0,0,132,133,5,63,0,0,133,34,1,0,0,0,134,135,
        5,37,0,0,135,36,1,0,0,0,136,137,9,0,0,0,137,138,1,0,0,0,138,139,
        6,18,0,0,139,38,1,0,0,0,12,0,54,59,65,69,76,82,88,92,99,105,110,
        1,6,0,0
    ]

class PythonLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PROTOCOL = 1
    DOMAINNAME = 2
    PORT = 3
    PATH = 4
    QUERY = 5
    FRAGMENTUNIT = 6
    WS = 7
    AMP = 8
    EQ = 9
    COLON = 10
    PLUS = 11
    HASHTAG = 12
    DOT = 13
    SLASH = 14
    DASH = 15
    UNDERSCORE = 16
    QUESTION = 17
    PERCENT = 18
    UNKNOWN = 19

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'&'", "'='", "':'", "'+'", "'#'", "'.'", "'/'", "'-'", "'_'", 
            "'?'", "'%'" ]

    symbolicNames = [ "<INVALID>",
            "PROTOCOL", "DOMAINNAME", "PORT", "PATH", "QUERY", "FRAGMENTUNIT", 
            "WS", "AMP", "EQ", "COLON", "PLUS", "HASHTAG", "DOT", "SLASH", 
            "DASH", "UNDERSCORE", "QUESTION", "PERCENT", "UNKNOWN" ]

    ruleNames = [ "PROTOCOL", "DOMAINNAME", "PORT", "PATH", "QUERY", "FRAGMENTUNIT", 
                  "WS", "AMP", "EQ", "COLON", "PLUS", "HASHTAG", "DOT", 
                  "SLASH", "DASH", "UNDERSCORE", "QUESTION", "PERCENT", 
                  "UNKNOWN" ]

    grammarFileName = "PythonLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

