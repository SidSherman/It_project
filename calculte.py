from math import *
from re import *

def calculate(expression):
    #try:


        expression = sub('\^', r'**', expression)
        print(expression)
        x = eval(expression)
        if abs(x-int(x)) < 1e-5:
            x = int(x)
        return x
    #except SyntaxError:
        #return "Выражение не валидно!"
    #except ZeroDivisionError:
        #return "Деление на ноль!"


def func(string):
    count_open = 0
    count_close = 0

    if str.replace(string, ".", string).isdigit():
        return "1/" + string

    i = len(string) - 1

    while string[i] not in "+-*/%" or count_open != count_close:
        if string[i] == ")":
            count_close += 1
        if string[i] == "(":
            count_open += 1
        if i == 0:
            break
        i -= 1
    znak = string[i]

    if string[0:i] not in "+-*/%":
        return string[0:i] + znak + "1/" + string[i + 1:len(string)]
    else:
        return "1/" + string[i:len(string)]


