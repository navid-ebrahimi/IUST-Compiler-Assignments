// Generated from java-escape by ANTLR 4.11.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class PythonLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.11.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PART1=1, PART2=2, PART3=3, PART4=4, PART5=5, PART6=6, WS=7, AMP=8, EQ=9, 
		PLUS=10, HASH=11, DOT=12, SLASH=13, DASH=14, UNDERSCORE=15, QUESTION=16, 
		PERCENT=17, UNKNOWN=18;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"PART1", "PART2", "PART3", "PART4", "PART5", "PART6", "WS", "AMP", "EQ", 
			"PLUS", "HASH", "DOT", "SLASH", "DASH", "UNDERSCORE", "QUESTION", "PERCENT", 
			"UNKNOWN"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, "'&'", "'='", "'+'", 
			"'#'", "'.'", "'/'", "'-'", "'_'", "'?'", "'%'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PART1", "PART2", "PART3", "PART4", "PART5", "PART6", "WS", "AMP", 
			"EQ", "PLUS", "HASH", "DOT", "SLASH", "DASH", "UNDERSCORE", "QUESTION", 
			"PERCENT", "UNKNOWN"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public PythonLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "PythonLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0012\u008d\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0003\u00005\b\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001;\b\u0001\u0001\u0001"+
		"\u0004\u0001>\b\u0001\u000b\u0001\f\u0001?\u0001\u0001\u0001\u0001\u0004"+
		"\u0001D\b\u0001\u000b\u0001\f\u0001E\u0004\u0001H\b\u0001\u000b\u0001"+
		"\f\u0001I\u0001\u0002\u0001\u0002\u0004\u0002N\b\u0002\u000b\u0002\f\u0002"+
		"O\u0001\u0003\u0001\u0003\u0004\u0003T\b\u0003\u000b\u0003\f\u0003U\u0001"+
		"\u0003\u0001\u0003\u0004\u0003Z\b\u0003\u000b\u0003\f\u0003[\u0005\u0003"+
		"^\b\u0003\n\u0003\f\u0003a\t\u0003\u0001\u0004\u0001\u0004\u0004\u0004"+
		"e\b\u0004\u000b\u0004\f\u0004f\u0001\u0005\u0001\u0005\u0004\u0005k\b"+
		"\u0005\u000b\u0005\f\u0005l\u0001\u0006\u0004\u0006p\b\u0006\u000b\u0006"+
		"\f\u0006q\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001"+
		"\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001"+
		"\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0000"+
		"\u0000\u0012\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b"+
		"\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b"+
		"\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012\u0001\u0000\u0005\u0003\u0000"+
		"09AZaz\u0001\u000009\u0005\u0000%&09==AZaz\u0005\u0000--09AZ__az\u0003"+
		"\u0000\t\n\r\r  \u0098\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003"+
		"\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007"+
		"\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001"+
		"\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000"+
		"\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000"+
		"\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000"+
		"\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000"+
		"\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000"+
		"\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000"+
		"\u00014\u0001\u0000\u0000\u0000\u0003:\u0001\u0000\u0000\u0000\u0005K"+
		"\u0001\u0000\u0000\u0000\u0007Q\u0001\u0000\u0000\u0000\tb\u0001\u0000"+
		"\u0000\u0000\u000bh\u0001\u0000\u0000\u0000\ro\u0001\u0000\u0000\u0000"+
		"\u000fu\u0001\u0000\u0000\u0000\u0011w\u0001\u0000\u0000\u0000\u0013y"+
		"\u0001\u0000\u0000\u0000\u0015{\u0001\u0000\u0000\u0000\u0017}\u0001\u0000"+
		"\u0000\u0000\u0019\u007f\u0001\u0000\u0000\u0000\u001b\u0081\u0001\u0000"+
		"\u0000\u0000\u001d\u0083\u0001\u0000\u0000\u0000\u001f\u0085\u0001\u0000"+
		"\u0000\u0000!\u0087\u0001\u0000\u0000\u0000#\u0089\u0001\u0000\u0000\u0000"+
		"%&\u0005h\u0000\u0000&\'\u0005t\u0000\u0000\'(\u0005t\u0000\u0000()\u0005"+
		"p\u0000\u0000)*\u0005:\u0000\u0000*+\u0005/\u0000\u0000+5\u0005/\u0000"+
		"\u0000,-\u0005h\u0000\u0000-.\u0005t\u0000\u0000./\u0005t\u0000\u0000"+
		"/0\u0005p\u0000\u000001\u0005s\u0000\u000012\u0005:\u0000\u000023\u0005"+
		"/\u0000\u000035\u0005/\u0000\u00004%\u0001\u0000\u0000\u00004,\u0001\u0000"+
		"\u0000\u00005\u0002\u0001\u0000\u0000\u000067\u0005w\u0000\u000078\u0005"+
		"w\u0000\u000089\u0005w\u0000\u00009;\u0005.\u0000\u0000:6\u0001\u0000"+
		"\u0000\u0000:;\u0001\u0000\u0000\u0000;=\u0001\u0000\u0000\u0000<>\u0007"+
		"\u0000\u0000\u0000=<\u0001\u0000\u0000\u0000>?\u0001\u0000\u0000\u0000"+
		"?=\u0001\u0000\u0000\u0000?@\u0001\u0000\u0000\u0000@G\u0001\u0000\u0000"+
		"\u0000AC\u0005.\u0000\u0000BD\u0007\u0000\u0000\u0000CB\u0001\u0000\u0000"+
		"\u0000DE\u0001\u0000\u0000\u0000EC\u0001\u0000\u0000\u0000EF\u0001\u0000"+
		"\u0000\u0000FH\u0001\u0000\u0000\u0000GA\u0001\u0000\u0000\u0000HI\u0001"+
		"\u0000\u0000\u0000IG\u0001\u0000\u0000\u0000IJ\u0001\u0000\u0000\u0000"+
		"J\u0004\u0001\u0000\u0000\u0000KM\u0005:\u0000\u0000LN\u0007\u0001\u0000"+
		"\u0000ML\u0001\u0000\u0000\u0000NO\u0001\u0000\u0000\u0000OM\u0001\u0000"+
		"\u0000\u0000OP\u0001\u0000\u0000\u0000P\u0006\u0001\u0000\u0000\u0000"+
		"QS\u0005/\u0000\u0000RT\u0007\u0000\u0000\u0000SR\u0001\u0000\u0000\u0000"+
		"TU\u0001\u0000\u0000\u0000US\u0001\u0000\u0000\u0000UV\u0001\u0000\u0000"+
		"\u0000V_\u0001\u0000\u0000\u0000WY\u0005/\u0000\u0000XZ\u0007\u0000\u0000"+
		"\u0000YX\u0001\u0000\u0000\u0000Z[\u0001\u0000\u0000\u0000[Y\u0001\u0000"+
		"\u0000\u0000[\\\u0001\u0000\u0000\u0000\\^\u0001\u0000\u0000\u0000]W\u0001"+
		"\u0000\u0000\u0000^a\u0001\u0000\u0000\u0000_]\u0001\u0000\u0000\u0000"+
		"_`\u0001\u0000\u0000\u0000`\b\u0001\u0000\u0000\u0000a_\u0001\u0000\u0000"+
		"\u0000bd\u0005?\u0000\u0000ce\u0007\u0002\u0000\u0000dc\u0001\u0000\u0000"+
		"\u0000ef\u0001\u0000\u0000\u0000fd\u0001\u0000\u0000\u0000fg\u0001\u0000"+
		"\u0000\u0000g\n\u0001\u0000\u0000\u0000hj\u0005#\u0000\u0000ik\u0007\u0003"+
		"\u0000\u0000ji\u0001\u0000\u0000\u0000kl\u0001\u0000\u0000\u0000lj\u0001"+
		"\u0000\u0000\u0000lm\u0001\u0000\u0000\u0000m\f\u0001\u0000\u0000\u0000"+
		"np\u0007\u0004\u0000\u0000on\u0001\u0000\u0000\u0000pq\u0001\u0000\u0000"+
		"\u0000qo\u0001\u0000\u0000\u0000qr\u0001\u0000\u0000\u0000rs\u0001\u0000"+
		"\u0000\u0000st\u0006\u0006\u0000\u0000t\u000e\u0001\u0000\u0000\u0000"+
		"uv\u0005&\u0000\u0000v\u0010\u0001\u0000\u0000\u0000wx\u0005=\u0000\u0000"+
		"x\u0012\u0001\u0000\u0000\u0000yz\u0005+\u0000\u0000z\u0014\u0001\u0000"+
		"\u0000\u0000{|\u0005#\u0000\u0000|\u0016\u0001\u0000\u0000\u0000}~\u0005"+
		".\u0000\u0000~\u0018\u0001\u0000\u0000\u0000\u007f\u0080\u0005/\u0000"+
		"\u0000\u0080\u001a\u0001\u0000\u0000\u0000\u0081\u0082\u0005-\u0000\u0000"+
		"\u0082\u001c\u0001\u0000\u0000\u0000\u0083\u0084\u0005_\u0000\u0000\u0084"+
		"\u001e\u0001\u0000\u0000\u0000\u0085\u0086\u0005?\u0000\u0000\u0086 \u0001"+
		"\u0000\u0000\u0000\u0087\u0088\u0005%\u0000\u0000\u0088\"\u0001\u0000"+
		"\u0000\u0000\u0089\u008a\t\u0000\u0000\u0000\u008a\u008b\u0001\u0000\u0000"+
		"\u0000\u008b\u008c\u0006\u0011\u0000\u0000\u008c$\u0001\u0000\u0000\u0000"+
		"\r\u00004:?EIOU[_flq\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}