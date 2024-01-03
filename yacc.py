import ply.yacc as yacc
import utils.ast as AST
from lexer import tokens

# Precedence des opérateurs
precedence = (
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES", "DIVIDE"),
)


def p_program(p):
    """program : statement_list"""
    p[0] = p[1]


def p_statement_list(p):
    """statement_list : statement
                      | statement_list statement
                      | statement_list NEWLINE"""
    if len(p) >= 3:
        if type(p[2]) is not str:
            p[0] = AST.ProgramNode(p[1].children + [p[2]])
        else:
            p[0] = p[1]
    else:
        p[0] = AST.ProgramNode([p[1]])


def p_statement(p):
    """statement : assignment
                 | if_statement
                 | while_statement
                 | return_statement
                 | function
                 | function_call
                 | statement NEWLINE"""
    p[0] = p[1]


def p_block(p):
    """block : INDENT statement_list DEDENT
             | block NEWLINE"""
    if len(p) == 4:
        p[0] = p[2]
    elif len(p) == 3:
        p[0] = p[1]


def p_assignment(p):
    """assignment : ID ASSIGN expression
                  | ID COLON type ASSIGN expression"""
    if len(p) == 4:
        p[0] = AST.AssignNode([AST.TokenNode(p[1]), p[3]])
    else:
        p[0] = AST.AssignNode([AST.TokenNode(p[1], p[3]), p[5]], p[3])


def p_if_statement(p):
    """if_statement : IF logical COLON block
                    | IF logical COLON block NEWLINE ELSE COLON block"""

    if len(p) == 9:
        p[0] = AST.IfNode(p[2], p[4], p[8])
    else:
        p[0] = AST.IfNode(p[2], p[4])


def p_while_statement(p):
    """while_statement : WHILE logical COLON block
                       | WHILE TRUE COLON block"""
    p[0] = AST.WhileNode([p[2], p[4]])


def p_return_statement(p):
    """return_statement : RETURN expression"""
    p[0] = AST.ReturnNode(p[2])


def p_id(p):
    """id : ID"""
    p[0] = AST.TokenNode(p[1])


def p_boolean_value(p):
    """boolean : TRUE
               | FALSE"""
    p[0] = AST.ValueNode(bool(p[1]), "bool")


def p_integer_value(p):
    """integer : INTEGER_VALUE"""
    p[0] = AST.ValueNode(int(p[1]), "int")


def p_float_value(p):
    """float : FLOAT_VALUE"""
    p[0] = AST.ValueNode(float(p[1]), "float")


def p_string_value(p):
    """string : STRING_VALUE"""
    p[0] = AST.ValueNode(str(p[1]), "string")


def p_value(p):
    """value : integer
             | float
             | boolean
             | string"""
    p[0] = p[1]


def p_variable(p):
    """variable : id
                | function_call"""
    p[0] = p[1]


def p_factor(p):
    """factor : value
              | variable"""

    p[0] = p[1]


def p_unary(p):
    """unary : NOT"""
    p[0] = AST.OpNode("not", p[2])


def p_logical(p):
    """logical : factor LT factor
               | factor LE factor
               | factor GT factor
               | factor GE factor
               | factor EQUALS factor
               | factor NEQUALS factor
               | factor AND factor
               | factor OR factor"""

    p[0] = AST.OpNode(p[2], [p[1], p[3]])


def p_math(p):
    """math : factor PLUS factor
            | factor MINUS factor
            | factor TIMES factor
            | factor DIVIDE factor"""

    p[0] = AST.OpNode(p[2], [p[1], p[3]])


def p_binary(p):
    """binary : logical
              | math"""

    p[0] = p[1]


def p_expression(p):
    """expression : factor
                  | unary
                  | binary"""

    p[0] = p[1]


def p_type(p):
    """type : INT
            | FLOAT
            | STR
            | BOOL
            | VOID"""
    p[0] = p[1]


def p_argument_list_definition(p):
    """argument_list_definition : ID COLON type
                     | ID COLON type COMMA argument_list_definition"""
    a = AST.ArgNode(p[1], AST.TypeNode(p[3]))

    if len(p) == 4:  # expression
        p[0] = a
    else:  # argument_list COMMA expression
        p[0] = AST.OpNode("arguments", [a, p[5]])


def p_function_definition(p):
    """function : DEF ID LPAREN argument_list_definition RPAREN RETURN_TYPE type COLON block"""
    p[0] = AST.DefNode(p[2], p[4], AST.TypeNode(p[7]), p[9])


def p_function_call(p):
    """function_call : ID LPAREN RPAREN
                     | ID LPAREN argument_list_call RPAREN"""
    if len(p) == 4:  # ID LPAREN RPAREN
        p[0] = AST.CallNode(p[1], [])
    else:  # ID LPAREN argument_list RPAREN
        p[0] = AST.CallNode(p[1], p[3].children)


def p_argument_list_call(p):
    """argument_list_call : expression
                     | expression COMMA argument_list_call"""
    if len(p) == 2:  # expression
        p[0] = AST.ArgumentsNode([p[1]])
    else:  # argument_list COMMA expression
        p[0] = AST.ArgumentsNode([p[1]] + p[3].children)


def p_error(p):
    if p:
        # Erreur syntaxique trouvée
        print(f"Syntax error in line {p.lineno}")
        yacc.errok()
    else:
        # Aucun token disponible pour poursuivre l'analyse
        print("Unexpected end of input")


yacc.yacc(outputdir="generated")


def parse(program, debug=False):
    return yacc.parse(program, debug=debug)


if __name__ == "__main__":
    import sys
    import os

    prog = open(sys.argv[1]).read()
    result = parse(prog, debug=True)
    print(result)

    grap = result.make_graphical_tree()
    name = os.path.splitext(sys.argv[1])[0] + "-ast.pdf"
    grap.write_pdf(name)
    print(f"Wrote {name}")
