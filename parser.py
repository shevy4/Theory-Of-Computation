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
                 | print_statement
                 | for_loop
                 | if_statement"""
    p[0] = p[1]


def p_for_loop(p):
    """for_loop : for expression in range lparen expression rparen colon"""
    p[0] = ('for', (p[4], (p[2], p[6])))


def p_if_statement(p):
    """
    if_statement : if expression colon statement
                 | if expression colon statement else colon statement
    """
    temp = p
    p[0] = ('if', p[2], p[4])

    if len(temp) > 5:
        p[0] = ('if', p[2], p[4]), ('else', p[7])


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
    """print_statement : print expression"""
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
        try:
            # print("Statement = ", statement)
            if statement[0] == 'assignment':
                variable_name = statement[1]
                expression = statement[2]

                # Perform type checking for assignment
                if isinstance(expression, tuple):
                    operator, operand1, operand2 = expression
                    if operator in ('+', '-', '*', '/'):
                        # Type check for arithmetic operations
                        if not (isinstance(operand1, int) and isinstance(operand2, int)):
                            if operand1 and operand2 in symbol_table:
                                pass
                            else:
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
                    if statement[1][0] == '"':
                        pass
                        # Check if identifier exists in symbol table
                    elif statement[1] not in symbol_table:
                        print(f"Semantic Error: Identifier '{statement[1]}' not declared.")
                        return False

            elif statement[0] == 'if':
                condition = statement[1]
                body = statement[2]
                print(condition, body)
                if bool(body):
                    pass
                # Ensure condition expression is of type bool
                elif not isinstance(condition, bool):
                    print("Semantic Error: 'if' statement condition must evaluate to a boolean value.")
                    return False
                # Perform semantic analysis on the body of the if statement
                if not semantic_analysis(body):
                    return False

            elif statement[0] == 'for':
                if statement[1][1][1] not in symbol_table:
                    if not isinstance(statement[1][1][1], int):
                        print(f"Semantic Error: Range '{statement[1][1][1]}' not of type int.")
                        return False

            elif statement[0][0] == "if":
                condition = statement[0][1]
                body = statement[0][2]
                if not bool(condition):
                    print("Semantic Error: 'if' statement condition must evaluate to a boolean value.")
                    return False

                if not semantic_analysis(body):
                    return False

        except:
            print("Invalid syntax")
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
