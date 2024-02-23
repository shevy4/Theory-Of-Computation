import re

# Define regular expressions
token_patterns = [
    (r'\b(if|else|elif|while|for|in|def|class|return|True|False|None)\b', 'KEYWORD'),
    (r'\b(and|or|not)\b', 'LOGICAL_OPERATOR'),
    (r'[-+]?\d*\.\d+|\d+', 'NUMBER'),  # Match floating point numbers and integers
    (r'"[^"\\]*(?:\\.[^"\\]*)*"', 'STRING'),  # Match strings
    (r'\'[^\'\\]*(?:\\.[^\'\\]*)*\'', 'STRING'),  # Match strings
    (r'\b[A-Za-z_]\w*', 'IDENTIFIER'),  # Match identifiers
    (r'[-+*/%=<>&|^~]', 'OPERATOR'),  # Match operators
    (r'\(|\)', 'PARENTHESES'),  # Match parentheses
    (r'\{|\}', 'BRACE'),  # Match braces
    (r':', 'COLON'),  # Match colons
    (r',', 'COMMA'),  # Match commas
    (r'\s+', None)  # Match whitespace
]


def tokenize(code):
    tokens = []
    while code:
        for pattern, token_type in token_patterns:
            match = re.match(pattern, code)
            if match:
                if token_type:
                    tokens.append((token_type, match.group(0)))
                code = code[match.end():]
                break
    return tokens


if __name__ == "__main__":

    code = """
    
    variable1 = 1
    variable2 = 2
    sum = variable1 + variable2
    print("sum = ", sum)
    
    """
    tokens = tokenize(code)
    for token in tokens:
        print(token)
