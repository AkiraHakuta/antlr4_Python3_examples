# Generated from PyEmbInTxt.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("\23\4\2\t\2\4\3\t\3\3\2\3\2\3\2\7\2\n\n\2\f\2\16\2\r\13")
        buf.write("\2\3\3\3\3\5\3\21\n\3\3\3\2\2\4\2\4\2\2\2\24\2\13\3\2")
        buf.write("\2\2\4\20\3\2\2\2\6\n\5\4\3\2\7\n\7\5\2\2\b\n\7\b\2\2")
        buf.write("\t\6\3\2\2\2\t\7\3\2\2\2\t\b\3\2\2\2\n\r\3\2\2\2\13\t")
        buf.write("\3\2\2\2\13\f\3\2\2\2\f\3\3\2\2\2\r\13\3\2\2\2\16\21\7")
        buf.write("\3\2\2\17\21\7\4\2\2\20\16\3\2\2\2\20\17\3\2\2\2\21\5")
        buf.write("\3\2\2\2\5\t\13\20")
        return buf.getvalue()


class PyEmbInTxtParser ( Parser ):

    grammarFileName = "PyEmbInTxt.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "PYCODE", "PYPRN", "SP", "COMMENT", "LINE_COMMENT", 
                      "OTHER" ]

    RULE_stat = 0
    RULE_py = 1

    ruleNames =  [ "stat", "py" ]

    EOF = Token.EOF
    PYCODE=1
    PYPRN=2
    SP=3
    COMMENT=4
    LINE_COMMENT=5
    OTHER=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def py(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PyEmbInTxtParser.PyContext)
            else:
                return self.getTypedRuleContext(PyEmbInTxtParser.PyContext,i)


        def SP(self, i:int=None):
            if i is None:
                return self.getTokens(PyEmbInTxtParser.SP)
            else:
                return self.getToken(PyEmbInTxtParser.SP, i)

        def OTHER(self, i:int=None):
            if i is None:
                return self.getTokens(PyEmbInTxtParser.OTHER)
            else:
                return self.getToken(PyEmbInTxtParser.OTHER, i)

        def getRuleIndex(self):
            return PyEmbInTxtParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)




    def stat(self):

        localctx = PyEmbInTxtParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PyEmbInTxtParser.PYCODE) | (1 << PyEmbInTxtParser.PYPRN) | (1 << PyEmbInTxtParser.SP) | (1 << PyEmbInTxtParser.OTHER))) != 0):
                self.state = 7
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [PyEmbInTxtParser.PYCODE, PyEmbInTxtParser.PYPRN]:
                    self.state = 4
                    self.py()
                    pass
                elif token in [PyEmbInTxtParser.SP]:
                    self.state = 5
                    self.match(PyEmbInTxtParser.SP)
                    pass
                elif token in [PyEmbInTxtParser.OTHER]:
                    self.state = 6
                    self.match(PyEmbInTxtParser.OTHER)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PyEmbInTxtParser.RULE_py

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PypContext(PyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PyEmbInTxtParser.PyContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PYPRN(self):
            return self.getToken(PyEmbInTxtParser.PYPRN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPyp" ):
                listener.enterPyp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPyp" ):
                listener.exitPyp(self)


    class PycContext(PyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PyEmbInTxtParser.PyContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PYCODE(self):
            return self.getToken(PyEmbInTxtParser.PYCODE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPyc" ):
                listener.enterPyc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPyc" ):
                listener.exitPyc(self)



    def py(self):

        localctx = PyEmbInTxtParser.PyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_py)
        try:
            self.state = 14
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PyEmbInTxtParser.PYCODE]:
                localctx = PyEmbInTxtParser.PycContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.match(PyEmbInTxtParser.PYCODE)
                pass
            elif token in [PyEmbInTxtParser.PYPRN]:
                localctx = PyEmbInTxtParser.PypContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.match(PyEmbInTxtParser.PYPRN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





