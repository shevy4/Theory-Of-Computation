from Lexer import tokenize
from parser import parse

if __name__ == "__main__":
    code = """
    for x in range(3):
    print("test")
      
    """

    if code.strip():
        tokens = tokenize(code)
        print("Tokens:", tokens)

        parsed_code = parse(code)

        if parsed_code:
            print("Parsed code:", parsed_code)

