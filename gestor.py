from pickle import *

class Personaje():
    def __init__(self, vida, ataq, defen, alcance, nombre):
        self.nombre = nombre
        self.vida = vida
        self.ataq = ataq
        self.defen = defen
        self.alcance = alcance
        if Personaje.comprobar(self, vida) == False:
            print('Vuelva a introducir la vida:')
            self.vida = int(input())

        if Personaje.comprobar(self, ataq) == False:
            print('Vuelva a introducir el ataque:')
            self.ataq = int(input())

        if Personaje.comprobar(self, defen) == False:
            print('Vuelva a introducir la defensa:')
            self.defen = int(input())

        if Personaje.comprobar(self, alcance) == False:
            print('Vuelva a introducir el alcance:')
            self.alcance = int(input())
        else:
            print('Tu personaje se ha creado correctamente')

    def comprobar(self, valor):
        if valor > 0:
            return True
        else: 
            return False

    def __str__(self):
        return "NOMBRE: " +  str(self.nombre) + "\n" + "VIDA: " +  str(self.vida) + "\n" + "ATAQUE: " +  str(self.ataq) + "\n" + "DEFENSA: " +  str(self.defen) + "\n" + "ALCANCE: " +  str(self.alcance) + "\n"

class Gestor():
    def __init__(self, personaje):
        self.personaje = personaje

    def añadir(self, fichero):
        f = open(fichero, 'wb')
        dump(self.personaje, f)
        f.close()

    def eliminar(self):
        pass

    def mostrar(self, fichero):
        f = open(fichero, 'rb')
        datos = load(f)
        print(datos)
        f.close()
        

    
lista = []
p = Personaje(3, 4, 61, 7, 'pepe')
a = Personaje(4, 4, 4, 4, 'anabelle')
#ichero = open('personajes.pckl', 'wb')
pepe = Gestor(p)
anabelle = Gestor(a)
lista.append(pepe)
lista.append(anabelle)
#print(pepe.personaje)
print(lista)
for i in range(len(lista)):
    lista[i].añadir('personajes.pckl')
    lista[i].mostrar('personajes.pckl')