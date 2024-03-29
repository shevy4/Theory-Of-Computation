from ply import lex

# Define lexer tokens
tokens = (
    'identifier',
    'integer',
    'float',
    'string',
    'operator',
    'print',
    'lparen',
    'rparen',
    'comma',
    'keyword',
    'equals',
    'double_equals',
)

# Define regular expressions for lexer tokens
t_double_equals = r'=='
t_operator = r'[-+*/%<>&|^~]'
t_print = r'print'
t_lparen = r'\('
t_rparen = r'\)'
t_comma = r','
t_equals = r'='
t_ignore = ' \t\r\n'


def t_float(t):
    r"""\d+\.\d+"""
    t.value = float(t.value)
    return t


def t_integer(t):
    r"""\d+"""
    t.value = int(t.value)
    return t


def t_string(t):
    r""""[^"\\]*(?:\\.[^"\\]*)*"|\'[^\'\\]*(?:\\.[^\'\\]*)*\'"""
    t.value = t.value[1:-1]  # Remove quotes
    return t


def t_keyword(t):
    r'\b(if|IF)\b'
    return t


def t_identifier(t):
    r"""[a-zA-Z_][a-zA-Z0-9_]*"""
    return t


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


# Define tokenize function
def tokenize(code):
    lexer.input(code)
    tokens = []
    for token in lexer:
        tokens.append((token.type, token.value))
    return tokens
