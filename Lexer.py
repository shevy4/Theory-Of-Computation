from ply import lex

# Define lexer tokens
tokens = (
    'KEYWORD',
    'LOGICAL_OPERATOR',
    'NUMBER',
    'STRING',
    'IDENTIFIER',
    'OPERATOR',
    'PARENTHESES',
    'BRACE',
    'COLON',
    'COMMA',
)

# Define regular expressions for lexer tokens
t_KEYWORD = r'\b(if|else|elif|while|for|in|def|class|return|True|False|None)\b'
t_LOGICAL_OPERATOR = r'\b(and|or|not)\b'
t_NUMBER = r'[-+]?\d*\.\d+|\d+'
t_STRING = r'"[^"\\]*(?:\\.[^"\\]*)*"|\''  # Improved regular expression for strings
t_IDENTIFIER = r'\b[A-Za-z_]\w*'
t_OPERATOR = r'[-+*/%=<>&|^~]'
t_PARENTHESES = r'\(|\)'
t_BRACE = r'\{|\}'
t_COLON = r':'
t_COMMA = r','

# Ignore whitespace
t_ignore = ' \t\r'

# Define a rule for tracking line numbers (optional)
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Define a rule for tracking column numbers (optional)
def find_column(input, token):
    last_cr = input.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

# Error handling rule (optional)
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Define tokenize function
def tokenize(code):
    lexer.input(code)
    tokens = []
    for token in lexer:
        tokens.append((token.type, token.value))
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
