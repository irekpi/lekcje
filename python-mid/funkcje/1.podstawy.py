def show_progress(character = '*', how_many=1):
    item = character * how_many
    print(item)


show_progress(10)
show_progress(15)
show_progress(30)

show_progress('-', 10)
show_progress('+', 15)


# Kwargs as dict to produce m2
def calculate_paint(efficency_ltr_per_m2, **kwargs,):
    total_ltr = 0
    for item in kwargs:
        total_ltr += kwargs[item]

    total_ltr_with_efficiency = total_ltr*efficency_ltr_per_m2
    print(total_ltr_with_efficiency)


# Args as list to produce m2
def calculate_paint_args(efficency_ltr_per_m2, *args):
    total_ltr = 0
    for item in args:
        total_ltr += item
    total_ltr_with_efficiency = total_ltr * efficency_ltr_per_m2
    print(total_ltr_with_efficiency)


calculate_paint(1, room=10, bathroom=11)
calculate_paint_args(1, 10, 11)


# Args with saving in file
def log_it(*args):
    path = 'pomoce/log_it.txt'
    with open(path, 'w') as file:
        for item in args:
            file.write(item+' ')
        file.write('\n')
        file.close()


log_it('cos', 'bede', 'dzis', 'pisal', 'w', 'wezu')
