#lib
import random
import operator

LEVEL_0 = 10
LEVEL_1 = 100
LEVEL_2 = 1000

def generate_function(level):
    list_operation = {'+':operator.add, 
                      '-':operator.sub #, '*':operator.mul
                      }
    operator_symbol = '+' #random.choice(list(list_operation.keys()))
    operator_f = list_operation[operator_symbol]
    x = random.randrange(1,level)
    y = random.randrange(1,level)
    resultado = operator_f(x, y)
    function_s = f"{x} {operator_symbol} {y} = "
    if level == LEVEL_2:
        z = random.randrange(1,level)
    
    return (function_s, str(resultado))
