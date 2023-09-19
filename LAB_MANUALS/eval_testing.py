print("Test Eval")

equation = 'x1 + 2 * x2 + x3'

def modify_value(x1, x2, x3, equa):
    result = eval(equa)
    print(result)
    return result

# a = 5
# modify_value(a,2,3,equation)