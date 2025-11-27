from jocs import janken
import time
print ("Benvingut a la meva maquina arcade, a continuació et mostraré els jocs que tinc disponibles:")
opcions = input("Tria el numerodel joc que vols jugar: 1: Janken 2: Endivinar numero; ")
if opcions == "1":
    print("El numero seleccionat és 1, per tant jugarem a Janken")
    time.sleep(1)
    janken()
elif opcions == "2":
    print("El numero seleccionat és 2, per tant jugarem a Endivinar numero")
    time.sleep(3)
    endivinar_num()
else:
    print("Opció no vàlida. Intenta-ho de nou.")
