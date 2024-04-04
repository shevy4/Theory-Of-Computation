from ply import yacc

from Lexer import tokens


# Define grammar rules
def p_program(p):
    """program : statement_list"""
    p[0] = p[1]


def p_statement_list(p):
    """statement_list : statement
                      | statement_list statement"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]


def p_statement(p):
    """statement : assignment
                 | comparison
                 | expression
                 | keyword
                 | print_statement
                 | if_statement"""
    p[0] = p[1]


def p_if_statement(p):
    """
    if_statement : if expression keyword colon statement
                 | if expression keyword colon statement else colon statement
    """
    temp = p
    p[0] = ('if', p[2], p[5])

    if len(temp) > 6:
        p[0] = ('if', p[2], p[5]), ('else', p[8])


def p_assignment(p):
    """assignment : identifier equals expression"""
    p[0] = ('assignment', p[1], p[3])


def p_comparison(p):
    """comparison : identifier double_equals expression"""
    p[0] = ('comparison', (p[1], p[3]))


def p_expression(p):
    """expression : integer
                  | float
                  | string
                  | identifier
                  | expression operator expression
                  | expression double_equals expression
                  | lparen expression rparen"""
    if len(p) == 2:
        p[0] = p[1]
    elif p[1] == '(':
        p[0] = p[2]
    else:
        p[0] = (p[2], p[1], p[3])


def p_print_statement(p):
    """print_statement : keyword expression"""
    p[0] = ('print', p[2])


def p_expression_list(p):
    """expression_list : expression
                       | expression_list comma expression"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_error(p):
    print("Syntax error:", p)


parser = yacc.yacc()

# Define a symbol table to track variable declarations and scopes
symbol_table = {}


# Define a function for semantic analysis
def semantic_analysis(parsed_code):
    for statement in parsed_code:
        if statement[0] == 'assignment':
            variable_name = statement[1]
            expression = statement[2]

            # Check if the variable is already declared
            if variable_name in symbol_table:
                print(f"Semantic Error: Variable '{variable_name}' redeclaration.")
                return False

            # Perform type checking for assignment
            if isinstance(expression, tuple):
                operator, operand1, operand2 = expression
                if operator in ('+', '-', '*', '/'):
                    # Type check for arithmetic operations
                    if not (isinstance(operand1, int) and isinstance(operand2, int)):
                        print("Semantic Error: Arithmetic operations require integer operands.")
                        return False
                elif operator == '=':
                    # Type check for assignment
                    if not isinstance(operand2, (int, str)):
                        print("Semantic Error: Assignment requires compatible types.")
                        return False

            # Add variable to symbol table
            symbol_table[variable_name] = None

        elif statement[0] == 'print':
            # Perform type checking for print statements
            for expression in statement[1]:
                if isinstance(expression, str):
                    if isinstance(statement[1], str):
                        return True
                    # Check if identifier exists in symbol table
                    elif expression not in symbol_table:
                        print(f"Semantic Error: Identifier '{expression}' not declared.")
                        return False
                elif not isinstance(expression, (int, str)):
                    print("Semantic Error: Print statement requires compatible types.")
                    return False

        elif statement[0] == 'if':
            condition = statement[1][0]
            body = statement[1][0]
            if bool(body):
                return True
            # Ensure condition expression is of type bool
            elif not isinstance(condition, bool):
                print("Semantic Error: 'if' statement condition must evaluate to a boolean value.")
                return False
            # Perform semantic analysis on the body of the if statement
            if not semantic_analysis(body):
                return False

    return True


def parse(code):
    parsed_code = parser.parse(code)
    if parsed_code:
        if semantic_analysis(parsed_code):
            return parsed_code
        else:
            return None
    else:
        return None
