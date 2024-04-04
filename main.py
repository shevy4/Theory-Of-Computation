from Lexer import tokenize
from parser import parse

if __name__ == "__main__":
    code = """
      var = 1
      print("Starting")
      if 1 < 2 then:
      print("Hello")
      else:
      print("World")
    """

    if code.strip():
        tokens = tokenize(code)
        print("Tokens:", tokens)

        parsed_code = parse(code)

        if parsed_code:
            print("Parsed code:", parsed_code)

