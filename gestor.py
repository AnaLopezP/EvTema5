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
        return "NOMBRE: " +  str(self.nombre) + "\n" + "VIDA: " +  str(self.vida) + "\n" + "ATAQUE: " +  str(self.ataq) + "\n" + "DEFENSA: " +  str(self.defen) + "\n" + "ALCANCE: " +  str(self.alcance)

class Gestor():
    def __init__(self):
        self.personaje = []

    def añadir(self, dato):
        self.personaje.append(dato)
        fichero = open('personajes.pckl', 'wb')
        dump(dato, fichero)
        fichero.close()
    
    def leer(self):
        for i in self.personaje:
            print(i)
    
    def borrar(self):
        p = input('Nombre del personaje a eliminar: ')
        for i in self.personaje:
            if i.nombre == p:
                self.personaje.remove(i)
                print('El personaje ha sido eliminado correctamente')
        fichero = open('personajes.pckl', 'wb')
        dump(self.personaje, fichero)

c = Personaje(4, 2, 4, 2, 'Caballero')
g = Personaje(2, 4, 2, 4, 'Guerrero')
a = Personaje(2, 4, 1, 8, 'Arquero')

gestor = Gestor()
gestor.añadir(c)
gestor.añadir(g)
gestor.añadir(a)

print('\nLEEMOS EL ARCHIVO')
gestor.leer()

print('\nELIMINAMOS AL ARQUERO')
gestor.borrar()
gestor.leer()