from Lexer import tokenize
from optimizer import eliminate_common_subexpressions, eliminate_dead_code, fold_constants, propagate_copies
from parser import parse
from tqdm import trange
from time import sleep
import tableprint as tp
import numpy as np

''' Common Subexpression Snippet
    a = 1 + 2
    b = 2
    c = 1 + 2
    d = 3
'''
''' Constant Folding Snippet
    PI = 22/7
'''
''' Copy Propagation Snippet
    a = 1
    b = 2
    d = a + b
'''
''' Dead Code Snippet
    a = 1
    x = a
    b = 2 + x
    d = x + b
'''

if __name__ == "__main__":
    code = """

    a = 1 + 2
    b = 2
    c = 1 + 2
    d = 3
      
    """
    tp.banner('Code Optimization using Finite Automata')
    data = np.array(
        ["1", "tokenizing", "2", "Parse Code", "3", "Subexpression Elimination", "4", "Dead Code ""Elimination",
         "5", "Constant Folding", "6", "Copy Propagation"]).reshape(6, 2)
    headers = ['Steps', 'Operation']

    tp.table(data, headers)

    sleep(1)

    # Tokenize & Parse
    tokens = tokenize(code)
    parsed_code = parse(code)
    if parsed_code:
        if code.strip():
            for _ in trange(len(tokens), desc="Tokenizing"):
                sleep(.2)
            print("tokens", tokens)
            sleep(1)
        for _ in trange(len(tokens), desc="Parsing"):
            sleep(.2)

        print("parsed code", parsed_code)
        sleep(1)

        # Eliminate_common_subexpressions
        optimized_code = eliminate_common_subexpressions(parsed_code)
        for _ in trange(len(tokens), desc="Optimizing Subexpressions"):
            sleep(.2)

        print("Code after Subexpression Elimination:", optimized_code)
        sleep(1)

        # eliminate_dead_code
        optimized_code = eliminate_dead_code(parsed_code)
        for _ in trange(len(tokens), desc="Burying Dead Code"):
            sleep(.3)

        print("Code after Dead Code Elimination:", optimized_code)
        sleep(1)

        # Constant Fold
        optimized_code = fold_constants(parsed_code)
        for _ in trange(len(tokens), desc="Folding Constants"):
            sleep(.2)

        print("Code after Constant Folding:", optimized_code)
        sleep(1)

        # Copy Propagating
        optimized_code = propagate_copies(parsed_code)
        for _ in trange(len(tokens), desc="Copy & Pasting"):
            sleep(.2)

        print("Code after Copy Propagation:", optimized_code)
        sleep(1)
