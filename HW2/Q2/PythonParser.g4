parser grammar PythonParser;

options {
  tokenVocab=PythonLexer;
}

url: protocol domainname port? path? query? fragment_unit?;

protocol: PROTOCOL;
domainname: DOMAINNAME;
port: PORT;
path: PATH;
query: QUERY;
fragment_unit: FRAGMENTUNIT;
