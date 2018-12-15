
def convert(num, to_base=10, from_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert(n // to_base, to_base) + alphabet[n % to_base]



def plus(num1, base1, num2, base2, out_base):
    num1 = convert(num1, 10, base1)
    num2 = convert(num2, 10, base2)
    output = str(int(num1) + int(num2))
    return convert(output, out_base)


def minus(num1, base1, num2, base2, out_base):
    num1 = convert(num1, 10, base1)
    num2 = convert(num2, 10, base2)
    output = str(int(num1) - int(num2))
    return convert(output, out_base)


def mult(num1, base1, num2, base2, out_base):
    num1 = convert(num1, 10, base1)
    num2 = convert(num2, 10, base2)
    output = str(int(num1) * int(num2))
    return convert(output, out_base)


def div(num1, base1, num2, base2, out_base):
    num1 = convert(num1, 10, base1)
    num2 = convert(num2, 10, base2)
    output = str(int(int(num1) / int(num2)))
    return convert(output, out_base)
