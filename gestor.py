from pickle import *

class Personaje():
    def __init__(self, vida, ataq, defen, alcance):
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
        return "VIDA: " +  str(self.vida) + "\n" + "ATAQUE: " +  str(self.ataq) + "\n" + "DEFENSA: " +  str(self.defen) + "\n" + "ALCANCE: " +  str(self.alcance) + "\n"

class Gestor():
    def __init__(self, personaje):
        self.personaje = personaje

p = Personaje(3, 4, -1, 7)
fichero = open('personajes.pckl', 'wb')
pepe = Gestor(p)
print(pepe.personaje)