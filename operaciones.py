def suma(num1, num2):
    try:
        sum = num1 + num2
    except TypeError:
        print('Error: tipo de dato no válido. Introduzca números, por favor: ')
        num1 = int(input('Primer numero: '))
        num2 = int(input('Segundo número: '))
        sum = num1 + num2
    return str(num1) + "+" + str(num2) + "=" + str(sum)

def resta(num1, num2):
    try:
        res = num1 - num2
    except TypeError:
        print('Error: tipo de dato no válido. Introduzca dos numeros, por favor: ')
        num1 = int(input('Primer numero: '))
        num2 = int(input('Segundo número: '))
        res = num1 - num2
    return str(num1) + "-" + str(num2) + "=" + str(res)

def producto(num1, num2):
    try:
        prod = num1*num2
    except TypeError:
        print('Error: tipo de dato no válido. Introduzca dos numeros, por favor: ')
        num1 = int(input('Primer numero: '))
        num2 = int(input('Segundo número: '))
        prod = num1*num2
    return str(num1) + "*" + str(num2) + "=" + str(prod)

def division(num1, num2):
    try:
        div = num1/num2
    except ZeroDivisionError:
        print('Error: No se puede dividir entre 0. Vuelva a introducir los numeros: ')
        num1 = int(input('Primer numero: '))
        num2 = int(input('Segundo número: '))
        div = num1/num2
    return str(num1) + "/" + str(num2) + "=" + str(div)
