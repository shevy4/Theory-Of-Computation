from Lexer import tokenize
from parser import parse
from code_gen import generate

if __name__ == "__main__":
    code = """
      IF 5 < 6
    """
    if code.strip():
        tokens = tokenize(code)
        print("Tokens:", tokens)

        parsed_code = parse(code)
        if parsed_code:
            print("Parsed code:", parsed_code)
            # print(generate(parsed_code))
