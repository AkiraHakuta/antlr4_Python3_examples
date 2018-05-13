# Generated from PyEmbInTxt.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write("_\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7")
        buf.write("\2\35\n\2\f\2\16\2 \13\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\63\n\3\f\3")
        buf.write("\16\3\66\13\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\7\5F\n\5\f\5\16\5I\13\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\7\6W\n\6\f\6\16\6Z")
        buf.write("\13\6\3\6\3\6\3\7\3\7\5\36\64G\2\b\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\3\2\4\3\2\"\"\4\2\f\f\17\17\2b\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\3\17\3\2\2\2\5+\3\2\2\2\7=\3\2\2\2\t?\3\2\2\2\13")
        buf.write("Q\3\2\2\2\r]\3\2\2\2\17\20\7^\2\2\20\21\7d\2\2\21\22\7")
        buf.write("g\2\2\22\23\7i\2\2\23\24\7k\2\2\24\25\7p\2\2\25\26\7}")
        buf.write("\2\2\26\27\7r\2\2\27\30\7{\2\2\30\31\7e\2\2\31\32\7\177")
        buf.write("\2\2\32\36\3\2\2\2\33\35\13\2\2\2\34\33\3\2\2\2\35 \3")
        buf.write("\2\2\2\36\37\3\2\2\2\36\34\3\2\2\2\37!\3\2\2\2 \36\3\2")
        buf.write("\2\2!\"\7^\2\2\"#\7g\2\2#$\7p\2\2$%\7f\2\2%&\7}\2\2&\'")
        buf.write("\7r\2\2\'(\7{\2\2()\7e\2\2)*\7\177\2\2*\4\3\2\2\2+,\7")
        buf.write("^\2\2,-\7r\2\2-.\7{\2\2./\7r\2\2/\60\7}\2\2\60\64\3\2")
        buf.write("\2\2\61\63\13\2\2\2\62\61\3\2\2\2\63\66\3\2\2\2\64\65")
        buf.write("\3\2\2\2\64\62\3\2\2\2\65\67\3\2\2\2\66\64\3\2\2\2\67")
        buf.write("8\7\61\2\289\7r\2\29:\7{\2\2:;\7r\2\2;<\7\177\2\2<\6\3")
        buf.write("\2\2\2=>\t\2\2\2>\b\3\2\2\2?@\7\61\2\2@A\7\61\2\2AB\7")
        buf.write("\61\2\2BC\7,\2\2CG\3\2\2\2DF\13\2\2\2ED\3\2\2\2FI\3\2")
        buf.write("\2\2GH\3\2\2\2GE\3\2\2\2HJ\3\2\2\2IG\3\2\2\2JK\7,\2\2")
        buf.write("KL\7\61\2\2LM\7\61\2\2MN\7\61\2\2NO\3\2\2\2OP\b\5\2\2")
        buf.write("P\n\3\2\2\2QR\7\61\2\2RS\7\61\2\2ST\7\61\2\2TX\3\2\2\2")
        buf.write("UW\n\3\2\2VU\3\2\2\2WZ\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y[\3")
        buf.write("\2\2\2ZX\3\2\2\2[\\\b\6\2\2\\\f\3\2\2\2]^\13\2\2\2^\16")
        buf.write("\3\2\2\2\7\2\36\64GX\3\b\2\2")
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


