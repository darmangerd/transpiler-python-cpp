from typing import Tuple
import ply.lex as lex

INDENTATION_SIZE = 4

keywords: Tuple[str] = (
    "if",
    "else",
    "while",
    "return",
    "def",
    "and",
    "or",
    "not",
    "True",
    "False",
    "int",
    "float",
    "bool",
    "str",
    "void",
)

# Liste des tokens
tokens: Tuple[str] = [
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "LPAREN",
    "RPAREN",
    "COLON",
    "NEWLINE",
    "COMMA",
    "EQUALS",
    "NEQUALS",
    "LT",
    "LE",
    "GT",
    "GE",
    "ID",
    "INTEGER_VALUE",
    "FLOAT_VALUE",
    "STRING_VALUE",
    "ASSIGN",
    "INDENT",
    "DEDENT",
    "RETURN_TYPE",
] + [k.upper() for k in keywords]

t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_COLON = r":"
t_COMMA = r","
t_EQUALS = r"=="
t_NEQUALS = r"!="
t_ASSIGN = r"="
t_LT = r"<"
t_LE = r"<="
t_GT = r">"
t_GE = r">="
t_RETURN_TYPE = r"->"


def t_ID(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"

    if t.value in keywords:
        t.type = t.value.upper()

    return t


def t_FLOAT_VALUE(t):
    # Positive float, zero with decimal or negative float
    r"0\.\d+|-?\d+\.\d+"
    t.value = float(t.value)
    return t


def t_INTEGER_VALUE(t):
    # Positive integer, zero or negative integer
    r"0|-?[1-9]\d*"
    t.value = int(t.value)
    return t


def t_STRING_VALUE(t):
    r'\"(\\.|[^\\"])*\"'
    return t


def calculate_indentation(line):
    """Calculate the indentation of a line"""
    indentation = 0
    for c in line:
        if c == " ":
            indentation += 1
        else:
            break
    return indentation // INDENTATION_SIZE


def t_INDENT(t):
    r'\n[ \t]*'

    # Calculate the level of indentation
    level = calculate_indentation(t.value.replace("\n", ""))

    if t.lexer.indent_level < level:
        t.lexer.indent_level += 1
        t.type = "INDENT"
        return t

    # Check for decreased or unchanged indentation
    elif t.lexer.indent_level > level:
        # Generate DEDENT tokens for each level of decreased indentation
        while t.lexer.indent_level > level:
            t.lexer.indent_level -= 1
            t.type = "DEDENT"
            t.lexer.lexpos -= 1
            return t

    elif t.lexer.indent_level == level:
        t.type = "NEWLINE"
        t.lexer.lineno += len(t.value)

    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


t_ignore = " \t"

lexer = lex.lex()
lexer.indent_level = 0


if __name__ == "__main__":
    import sys

    prog = open(sys.argv[1]).read()
    lexer.input(prog)

    while True:
        tok = lexer.token()

        if not tok:
            break

        print("line %d: %s(%s)" % (tok.lineno, tok.type, tok.value))
