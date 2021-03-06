from math import *
from re import *

def calculate(expression):
    try:


        if "√" in expression:
            expression = func_sqrt(expression)
        if "!" in expression:
            expression = func_fac(expression)

        if "°" in expression:
            expression = func_grad(expression)

        expression = sub('\^', r'**', expression)


        expression = sub('!', r'', expression)


        expression = sub('°', r'', expression)
        expression = sub('π', r'pi', expression)

        x = eval(expression)
        if abs(x-int(x)) < 1e-5:
            x = int(x)
        return x
    except ZeroDivisionError:
        pass
    


def func(string):
    try:
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
    except: pass


def func_sqrt(string):
    while "√" in string:
        count_open = 0
        count_close = 0
        index = str.index(string, "√")
        string = string[0:index] + "sqrt(" +string[index+1:]
        index += 5

        while count_open != count_close or string[index] not in "+-=*%":
            x = string[index]
            if string[index] == "(":
                count_open += 1
            if string[index] == ")":
                count_close += 1
            index += 1

            if index == len(string):
                break


        if index != len(string):
            string = string[0:index] + ")" + string[index:]
        else:
            string = string + ")"

    return string


def func_fac(string):
    try:


        while "!" in string:
            count_open = 0
            count_close = 0
            index = string.index("!")
            index_0 = index
            while True:
                index_0-=1

                if string[index_0] == "(":
                    count_open += 1
                if string[index_0] == ")":
                    count_close += 1

                if (string[index_0] in "+-/*%" or index_0 == 0) and count_close == count_open:
                    str_r = "factorial(" + string[index_0+1: index] + ")"
                    string = string[:index_0+1] + str_r + string[index+1:]
                    break

        return string

    except: pass

def func_grad(string):
    try:

        while "°" in string:
            count_open = 0
            count_close = 0
            index = string.index("°")
            index_0 = index
            while True:
                index_0 -= 1

                if string[index_0] == "(":
                    count_open += 1
                if string[index_0] == ")":
                    count_close += 1

                if (string[index_0] in "+-/*%" or index_0 == 0) and count_close == count_open:
                    str_r = "radians(" + string[index_0 + 1: index] + ")"
                    string = string[:index_0 + 1] + str_r + string[index + 1:]
                    break

        return string

    except:
        pass
