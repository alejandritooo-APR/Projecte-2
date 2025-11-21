import robot
import random

def janken():
    print("Benvingut a la meva maquina Janken, a continuació et mostrare diferents nombres per poder triar entres les diferents modalitats")
    nombre = input("Tria un dels següents nombres per poder començar el joc: 1: (Nivell fàcil) És jugaran tres rondes. 2: (Difícl) Al millor de 5 rondes")
    if nombre == 1:
        print("Has triat la modalitat fàcil, anem a començar el joc")
        objectes = input ("Escolleig entre 1:Pedra 2:Tissora 3:Paper;  ")
        if objectes == 1:
    if nombre == 2:
        print("Has triat la modalitat difícil, anem a començar el joc")
        objectes = input ("Escolleig entre 1:Pedra 2:Tissora 3:Paper;  ")


