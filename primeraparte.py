import os
os.system("cls")

print("¡BIENVENIDO A 'AGILIZA TU MENTE'!")
print("Este juego matemático pone en desafío tu capacidad de resolver operaciones combinadas en el menor tiempo posible.")

from time import sleep
for i in range(0,5):
    print(5-i)
    sleep(1)
while True:
    de=input("¿Desea jugar?:  (si) (no)")
    if de == "no":
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
            respuesta=int(input("¿Cuanto es 2*"+str(numazar)+"+"+str(numazar1)+"-2"+"  ?"))
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
                print("Respuesta incorrecta :( Suerte para la próxima")
                while True:
                    jugar=input("¿Quieres jugar otra vez? (si)(no) ")
                    if jugar == "no":
                        print("Hasta luego ;-) ")    
                    break
    break