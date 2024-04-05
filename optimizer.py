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


