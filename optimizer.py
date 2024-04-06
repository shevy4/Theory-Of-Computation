def eliminate_common_subexpressions(parsed_code):
    expressions = {}
    new_code = []

    for operation in parsed_code:
        if operation[0] == 'assignment':
            target_var = operation[1]
            expression = operation[2]

            if isinstance(expression, tuple):
                if expression not in expressions.values():
                    expressions[target_var] = expression
                    new_code.append(operation)
                else:
                    for var, expr in expressions.items():
                        if expr == expression:
                            new_code.append(('assignment', target_var, var))
                            break
            else:
                new_code.append(operation)
        else:
            new_code.append(operation)

    return new_code


def eliminate_dead_code(parsed_code):
    used_variables = set()
    new_code = []

    # Find used variables
    for operation in parsed_code:
        if operation[0] == 'assignment':
            target_var = operation[1]
            expression = operation[2]

            if isinstance(expression, tuple):
                for var in expression:
                    if var not in ('+', '-', '*', '/'):
                        used_variables.add(var)

    # Filter out unused assignments
    for operation in parsed_code:
        if operation[0] == 'assignment':
            target_var = operation[1]
            if target_var in used_variables:
                new_code.append(operation)
        else:
            new_code.append(operation)

    return new_code


def fold_constants(parsed_code):
    new_code = []

    for operation in parsed_code:
        if operation[0] == 'assignment':
            target_var = operation[1]
            expression = operation[2]

            if isinstance(expression, tuple):
                evaluated_expr = fold(expression)
                if evaluated_expr is not None:  # If the expression can be evaluated to a constant
                    new_code.append(('assignment', target_var, evaluated_expr))
                else:
                    new_code.append(operation)
            else:
                new_code.append(operation)
        else:
            new_code.append(operation)

    return new_code


def fold(expression):
    if isinstance(expression, tuple):
        operator = expression[0]
        operand1 = expression[1]
        operand2 = expression[2]

        if isinstance(operand1, int) and isinstance(operand2, int):
            if operator == '+':
                return operand1 + operand2
            elif operator == '-':
                return operand1 - operand2
            elif operator == '*':
                return operand1 * operand2
            elif operator == '/':
                if operand2 != 0:
                    return (operand1 / operand2).__round__(2)
                else:
                    return None  # Division by zero
        else:
            return None  # Expression contains non-constant operands
    else:
        return None  # Expression is already a constant


def propagate_copies(parsed_code):
    replacements = {}
    new_code = []

    for operation in parsed_code:
        if operation[0] == 'assignment':
            target_var = operation[1]
            expression = operation[2]

            if isinstance(expression, tuple):
                new_expr = replace_variables(expression, replacements)
                new_code.append((operation[0],target_var, new_expr))

            else:
                new_code.append(operation)
                replacements[target_var] = expression

    return new_code


def replace_variables(expression, replacements):
    if isinstance(expression, tuple):
        operator = expression[0]
        operand1 = expression[1]
        operand2 = expression[2]

        if isinstance(operand1, str) and operand1 in replacements:
            operand1 = replacements[operand1]

        if isinstance(operand2, str) and operand2 in replacements:
            operand2 = replacements[operand2]

        return (operator, operand1, operand2)
    else:
        return expression
