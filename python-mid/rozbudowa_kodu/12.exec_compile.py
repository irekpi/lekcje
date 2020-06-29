import math, time

# exec
# the open method takes loc, mode ('r' - read, 'w' - write, 'a' - append, 'r+' - special read/write)
with open("pomoce/math_scripts.py", 'r') as file:
    source = file.read()
    exec(source)
    print('---------------')

# Compile

formulas_list = [
    "abs(x**3 - x**0.5)",
    "abs(math.sin(x) * x**2)"
]

arguments_list = []
for item in range(100000):
    arguments_list.append(item/10)

result_list = []

for formula in formulas_list:
    print('Formula not compiled {}'.format(formula))
    time_start = time.time()
    for item in arguments_list:
        result_list.append(eval(formula))
    print(max(result_list), min(result_list))
    time_end = time.time()
    time_spent = time_end-time_start
    print(time_spent)

print('----------------------')
for formula in formulas_list:
    print('Formula compiled {}'.format(formula))
    compiled_formula = compile(formula, formula, 'eval')
    time_start = time.time()
    for item in arguments_list:
        result_list.append(eval(compiled_formula))
    print(max(result_list), min(result_list))
    time_end = time.time()
    time_spent = time_end-time_start
    print(time_spent)





