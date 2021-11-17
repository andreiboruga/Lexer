# Lexer
"Lexer.py" contains a line of code which runs the
runlexer() function which has 3 parameters as file paths:
lexer configuration(DFAs configuration), text to be parsed,
output file.

There are some sets of tests in the folders: T1.5 and T1.6.
For example in folder T1.5 T1.5.lex is the lexer configuration
and in T1.5/input there are multiple text files which can be
used for parsing.

Based on the lexer configuration file format you can create
your own lexer configuration and then your own tests.

For example, the line "runlexer("T1.5/T1.5.lex", "T1.5/input/T1.5.1.in", "output.txt")"
will run the lexer with the configuration from "T1.5/T1.5.lex" on the input:
"T1.5/input/T1.5.1.in" and will print the output in "output.txt".



