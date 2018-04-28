# Generated from PyEmbInTxt.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write("[\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2\32\n\2\f")
        buf.write("\2\16\2\35\13\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3/\n\3\f\3\16\3\62\13\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\7\5B\n\5\f\5\16\5E\13\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\7\6S\n\6\f\6\16\6V\13\6\3\6\3\6\3\7")
        buf.write("\3\7\5\33\60C\2\b\3\3\5\4\7\5\t\6\13\7\r\b\3\2\4\3\2\"")
        buf.write("\"\4\2\f\f\17\17\2^\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\3\17\3\2\2\2\5")
        buf.write("%\3\2\2\2\79\3\2\2\2\t;\3\2\2\2\13M\3\2\2\2\rY\3\2\2\2")
        buf.write("\17\20\7^\2\2\20\21\7r\2\2\21\22\7{\2\2\22\23\7e\2\2\23")
        buf.write("\24\7q\2\2\24\25\7f\2\2\25\26\7g\2\2\26\27\7}\2\2\27\33")
        buf.write("\3\2\2\2\30\32\13\2\2\2\31\30\3\2\2\2\32\35\3\2\2\2\33")
        buf.write("\34\3\2\2\2\33\31\3\2\2\2\34\36\3\2\2\2\35\33\3\2\2\2")
        buf.write("\36\37\7\61\2\2\37 \7e\2\2 !\7q\2\2!\"\7f\2\2\"#\7g\2")
        buf.write("\2#$\7\177\2\2$\4\3\2\2\2%&\7^\2\2&\'\7r\2\2\'(\7{\2\2")
        buf.write("()\7r\2\2)*\7t\2\2*+\7p\2\2+,\7}\2\2,\60\3\2\2\2-/\13")
        buf.write("\2\2\2.-\3\2\2\2/\62\3\2\2\2\60\61\3\2\2\2\60.\3\2\2\2")
        buf.write("\61\63\3\2\2\2\62\60\3\2\2\2\63\64\7\61\2\2\64\65\7r\2")
        buf.write("\2\65\66\7t\2\2\66\67\7p\2\2\678\7\177\2\28\6\3\2\2\2")
        buf.write("9:\t\2\2\2:\b\3\2\2\2;<\7\61\2\2<=\7\61\2\2=>\7\61\2\2")
        buf.write(">?\7,\2\2?C\3\2\2\2@B\13\2\2\2A@\3\2\2\2BE\3\2\2\2CD\3")
        buf.write("\2\2\2CA\3\2\2\2DF\3\2\2\2EC\3\2\2\2FG\7,\2\2GH\7\61\2")
        buf.write("\2HI\7\61\2\2IJ\7\61\2\2JK\3\2\2\2KL\b\5\2\2L\n\3\2\2")
        buf.write("\2MN\7\61\2\2NO\7\61\2\2OP\7\61\2\2PT\3\2\2\2QS\n\3\2")
        buf.write("\2RQ\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2\2UW\3\2\2\2V")
        buf.write("T\3\2\2\2WX\b\6\2\2X\f\3\2\2\2YZ\13\2\2\2Z\16\3\2\2\2")
        buf.write("\7\2\33\60CT\3\b\2\2")
        return buf.getvalue()


class PyEmbInTxtLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PYCODE = 1
    PYPRN = 2
    SP = 3
    COMMENT = 4
    LINE_COMMENT = 5
    OTHER = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "PYCODE", "PYPRN", "SP", "COMMENT", "LINE_COMMENT", "OTHER" ]

    ruleNames = [ "PYCODE", "PYPRN", "SP", "COMMENT", "LINE_COMMENT", "OTHER" ]

    grammarFileName = "PyEmbInTxt.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


