from matplotlib import pyplot


def get_loan_info():
    loan = {}
    loan['principal'] = float(input('Wpisz ile chcesz pozyczyc?'))
    loan['rates'] = float(input('Procent pozyczki??')) / 100
    loan['monthly_payment'] = float(input('Ile chcesz placic miesiecznie?'))
    loan['money_paid'] = 0
    return loan


def show_loan_info(loan, month_number):
    print('Info pozyczki po {} miesiacach'.format(month_number))
    for key, value in loan.items():
        print('{} : {:2}'.format(key.title(), value))


def collect_interest(loan):
    loan['principal'] = loan['principal'] + loan['principal'] * loan['rates'] / 12


def make_monthly_payment(loan):
    loan['principal'] = loan['principal'] - loan['monthly_payment']
    if loan['principal'] > 0:
        loan['money_paid'] += loan['principal']
    else:
        loan['money_paid'] += loan['monthly_payment'] + loan['principal']


def summarize_loan(loan, month_number, initial_principal):
    print('Splaciles caly kredyt w {}'.format(month_number))
    print('Brales na poczatku  {} z oprocentowaniem {}'.format(initial_principal, 100 * loan['rates']))
    print('Miesiecznie placiles {}'.format(loan['monthly_payment']))
    print('Calkowicie wydales {}'.format(loan['money_paid']))
    interest = round(loan['money_paid'] - initial_principal, 2)
    print('Na splate wydales {}'.format(interest))


def create_graph(data, loan):
    x_values = []
    y_values = []
    for point in data:
        x_values.append(point[0])
        y_values.append(point[1])
    pyplot.plot(x_values, y_values)
    pyplot.xlabel('Miesiac')
    pyplot.ylabel('Rata')
    pyplot.show()


month_number = 0
my_loan = get_loan_info()
starting_principal = my_loan['principal']
data_to_plot = []
show_loan_info(my_loan, month_number)
input('Nacisnij enter zeby placici')

while my_loan['principal'] > 0:
    if my_loan['principal'] > starting_principal:
        break
    month_number += 1
    collect_interest(my_loan)
    make_monthly_payment(my_loan)
    data_to_plot.append((month_number, my_loan['principal']))
    show_loan_info(my_loan, month_number)
if my_loan['principal'] <= 0:
    summarize_loan(my_loan, month_number, starting_principal)
    create_graph(data_to_plot, my_loan)
else:
    print('Nie dasz rade tego splacic ;(')
