from Lexer import tokenize
from parser import parse


if __name__ == "__main__":
    code = """
      if (1 < 2){
        print("ahh");
        }
    """
    if code.strip():
        tokens = tokenize(code)
        print("Tokens:", tokens)

        parsed_code = parse(code)
        if parsed_code:
            print("Parsed code:", parsed_code)
            # print(generate(parsed_code))
