from pickle import *

class Personaje():
    def __init__(self, vida, ataq, defen, alcance):
        self.vida = vida
        self.ataq = ataq
        self.defen = defen
        self.alcance = alcance
        #poner las condiciones con la funcion comprobar

    def comprobar(self, valor):
        if valor > 0:
            print('Tu personaje se ha creado correctamente')
            return True
        else: 
            print('Las características del personaje tienen que ser mayores que 0. Vuelva a introducir los datos.')
            return False

    def __str__(self):
        return "VIDA: " +  str(self.vida) + "\n" + "ATAQUE: " +  str(self.ataq) + "\n" + "DEFENSA: " +  str(self.defen) + "\n" + "ALCANCE: " +  str(self.alcance) + "\n"

class Gestor():
    pass

pepe = Personaje(3, 4, 5, 7)
print(pepe)