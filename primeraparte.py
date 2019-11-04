import os
os.system("cls")

print("BIENVENIDO A 'AGILIZA TU MENTE'!)
print("Este un juego matemático donde se pone en desafio tu capacidad de resolver operaciones combinadas en el menor tiempo posible.")

from time import sleep
for i in range(0,5):
    print(5-i)
    sleep(1)
while True:
    de=input("¿Desea jugar?:  (Si)(No)")
    if de == "No":
        print("Vuelva pronto")
        break
    else:
        print("Resuelva las operaciones en el menor tiempo posible")
        
        print("Comienza el juego")

        from time import sleep
        for i in range(0,5):
            print(5-i)
            sleep(1)


        import time
        import random

        print("Responda lo mas rápido posible")
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
                while True:
                    jugar=input("¿Quieres jugar otra vez? (si)(no)   ")
                    if jugar == "no":
                        break
                print(" Hasta luego ;-)  ")
    break


