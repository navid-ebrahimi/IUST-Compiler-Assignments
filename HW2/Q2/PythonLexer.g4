lexer grammar PythonLexer;

PROTOCOL: 'http://' | 'https://';
DOMAINNAME: [a-zA-Z0-9]+ (DOT [a-zA-Z0-9]+)*;
PORT: COLON [0-9]+;
PATH: SLASH [a-zA-Z0-9]+ (SLASH [a-zA-Z0-9]+)*;
QUERY: QUESTION [a-zA-Z0-9%&=]+;
FRAGMENTUNIT: HASHTAG [a-zA-Z0-9_-]+;


WS: [ \t\n\r]+ -> skip;

AMP: '&';
EQ: '=';
COLON: ':';
PLUS: '+';
HASHTAG: '#';
DOT: '.';
SLASH: '/';
DASH: '-';
UNDERSCORE: '_';
QUESTION: '?';
PERCENT: '%';

UNKNOWN: . -> skip;
