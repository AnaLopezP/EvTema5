#1) crear fichero txt con el numero 0 por defecto
#2) si el fichero ya existe, leer el contenido
#3) si argumento --> inc: contador + 1 y leer
#4) si argumento --> dec: contador - 1 y leer
#5) si no hay argumento: leer
#6) se vuelve a guardar en el fichero
#7) error fichero corrupto

def leerfich():
    try:
        con = open('contador.txt')
    except FileNotFoundError:
        con = open('contador.txt', 'w')
        con.write('0')
        con.close()
    print(con.read())

def sumres(inc, dec):
    if inc == True:
        con = open('contador.txt', 'r')
        a = int(con.read())
        dato = a + 1
        con2 = open('contador.txt', 'w')
        con2.write(str(dato))
        con2.close()
        leerfich()
    if dec == True:
        con = open('contador.txt', 'r')
        a = int(con.read())
        dato = a - 1
        con2 = open('contador.txt', 'w')
        con2.write(str(dato))
        con2.close()
        leerfich()
    if dec == False and inc == False:
        con = open('contador.txt', 'r')
        print(con.read())



sumres(False, True)