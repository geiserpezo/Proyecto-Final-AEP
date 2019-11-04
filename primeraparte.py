import os
os.system("cls")




from time import sleep
for i in range(0,5):
    print(5-i)
    sleep(1)
print("instrucciones")
print("---------------")


print("Este juego estaba basado en resolver operaciones combinadas el la cual saldran aleatoriamente; y a su ves depedera de la habilidad mental para resolverlos e ingresar el resultado")


print("Comienza el juego")

from time import sleep
for i in range(0,5):
    print(5-i)
    sleep(1)


import time
import random

print("Responde lo mas rapido posible")
jugar= "si"
while jugar=="si":
    inicio=time.time()
    numazar=random.randint(1,15)
    numazar1=random.randint(1,15)
    respuesta=int(input("¿Cuanto es 2*"+str(numazar)+"+"+str(numazar1)+"-2+"+"  ?"))
    final=time.time()
    tiempo=round(final-inicio,0)
    if respuesta == numazar*2+numazar1-2:
        print("Felicidades, resultado correcto",end=" ")
        if tiempo < 7:
            print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Excelente!")
        if tiempo >= 7 and tiempo < 16:
            print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡lo puedes hacer mejor!")
        if tiempo >= 16:
            print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡te falta practicar velocidad mental, pero vamos bien!")
    else:
        print("Suerte para la proxima")
        jugar=input("¿Quieres jugar otra vez? (si)(no)   ")
        if jugar == "NO":
            break
print(" Hasta luego ;-)  ")


