from Lexer import tokenize
from optimizer import  eliminate_common_subexpressions
from parser import parse

if __name__ == "__main__":
    code = """
    b = 2
    c = 3
    d = 4
    a = b + c
    b = a - d
    c = b + c
    d = a - d
      
    """

    if code.strip():
        tokens = tokenize(code)
        print("Tokens:", tokens)

        parsed_code = parse(code)

        if parsed_code:
            print(parsed_code)
            optimized_code = eliminate_common_subexpressions(parsed_code)
            print("Optimized Code:", optimized_code)

