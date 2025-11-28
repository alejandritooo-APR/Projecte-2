from robot import robot
import random

def janken():
    print("Benvingut a la meva maquina Janken, a continuació et mostrare diferents nombres per poder triar entres les diferents modalitats")
    usuari = input("Tria un dels següents nombres per poder començar el joc: 1: (Nivell fàcil) És jugaran tres rondes. 2: (Difícl) Al millor de 5 rondes;   ")
    if usuari == 1:
        print("Has triat la modalitat fàcil, anem a començar el joc")
        usuari = input("Escolleig entre pedra,paper,tisora;  ")
        if usuari == "pedra":
            print("Has triat Pedra")    
        elif usuari == "paper":
            print("Has triat paper")
        elif usuari == "tisora":
            print("Has triat tisora")
    if usuari == "pedra" and robot == "tisora":
        print("Has guanyat")
    elif usuari == "pedra" and robot == "paper":      
        print("Has perdut")
    elif usuari == "paper" and robot == "pedra":
        print("Has guanyat")
    elif usuari == "paper" and robot == "tisora":
        print("Has perdut")
    elif usuari == "tisora" and robot == "paper":
        print("Has guanyat")
    elif usuari == "tisora" and robot == "pedra":
        print("Has perdut")  
    robot.playing()  
    if usuari == 2:
        print("Has triat la modalitat difícil, anem a començar el joc")
        objectes = input("Escolleig entre pedra,paper,tisora;  ")       
        if objectes == "pedra":
                print("Has triat Pedra")
        elif objectes == "paper":
                print("Has triat paper")
        elif objectes == "tisora":
                print("Has triat tisora")
        maquina = random.choice("pedra", "paper", "tisora")
        print("La maquina ha triat: ", maquina)
        usuari = objectes
        if usuari == "pedra" and maquina == "tisora":
                print("Has guanyat")
        elif usuari == "pedra" and maquina == "paper":
                print("Has perdut")
        elif usuari == "paper" and maquina == "pedra":
                print("Has guanyat")
        elif usuari == "paper" and maquina == "tisora":
                print("Has perdut")
        elif usuari == "tisora" and maquina == "paper":
                print("Has guanyat")
        elif usuari == "tisora" and maquina == "pedra":
                print("Has perdut")