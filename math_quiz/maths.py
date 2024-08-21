#lib
import random
import operator

levels = {"1": 10, "2": 50, "3": 200, "4": 500}

result_wrong = 'Wrong! Try again!'
result_ok = 'Well done!'

def generate_function(level):
    list_operation = {'+':operator.add, 
                      '-':operator.sub #, '*':operator.mul
                      }
    operator_symbol = random.choice(list(list_operation.keys()))
    operator_f = list_operation[operator_symbol]
    x = random.randrange(1,levels[level])
    y = random.randrange(1,levels[level])
    resultado = operator_f(x, y)
    function_s = f"{x} {operator_symbol} {y} = "
    if level == level:
        z = random.randrange(1,levels[level])
    
    return (function_s, str(resultado))
