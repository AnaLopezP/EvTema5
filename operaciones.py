def suma(num1, num2):
    try:
        sum = num1 + num2
    except TypeError:
        print('Introduzca números, por favor: ')
        num1 = int(input('Primer numero: '))
        num2 = int(input('Segundo número: '))
        sum = num1 + num2
    return num1, num2, sum

def resta(num1, num2):
    try:
        res = num1 - num2
    except TypeError:
        print('Introduzca dos numeros, por favor: ')
        num1 = int(input('Primer numero: '))
        num2 = int(input('Segundo número: '))
        res = num1 - num2
    return num1, num2, res

def producto(num1, num2):
    try:
        prod = num1*num2
    except TypeError:
        print('Introduzca dos numeros, por favor: ')
        num1 = int(input('Primer numero: '))
        num2 = int(input('Segundo número: '))
        prod = num1*num2
    return num1, num2, prod

def division(num1, num2):
    try:
        div = num1/num2
    except ZeroDivisionError:
        print('No se puede dividir entre 0. Vuelva a introducir los numeros: ')
        num1 = int(input('Primer numero: '))
        num2 = int(input('Segundo número: '))
        div = num1/num2
    return num1, num2, div

