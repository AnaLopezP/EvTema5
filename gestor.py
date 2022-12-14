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

class Gestor():
    pass