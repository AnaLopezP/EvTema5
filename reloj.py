from time import *
from os import *

def hora():
    tiempo = strftime("%H:%M:%S")
    system('cls')
    return tiempo

print(hora())
while True:
    print(hora())
    sleep(1)