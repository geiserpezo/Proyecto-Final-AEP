import os
os.system("cls")

print("BIENVENIDO A 'AGILIZA TU MENTE'!")
print("Este es un juego matemático donde se pone en desafio tu capacidad de resolver operaciones combinadas en el menor tiempo posible.")

from time import sleep
for i in range(0,5):
    print(5-i)
    sleep(1)
while True:
    de=input("¿Desea jugar?:  (si) (no) =")
    if de == "no":
        print("Vuelva pronto :-)")
        break
    else:
        print("Resuelva las operaciones en el menor tiempo posible")
        
        print("Comienza el juego ")

        from time import sleep
        for i in range(0,3):
            print(3-i)
            sleep(1)


        import time
        import random

        print("Responda lo mas rápido posible")
        jugar= "si"
        for i in range(0,2):
            inicio=time.time()

            numazar=random.randint(1,25)
            numazar1=random.randint(1,25)
            
            r=int(input("¿Cuanto es: "+str(numazar)+"+"+str(numazar1)+ " ?"))
            final=time.time()
            tiempo=round(final-inicio,0)
            r1=numazar+numazar1
    
            if r == r1:
                print("Felicidades, resouesta correcta",end=" ")
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
                break
            
    
            numazar=random.randint(1,25)
            numazar1=random.randint(1,25)
            
            z=int(input("¿Cuanto es: "+str(numazar)+"-"+str(numazar1)+ " ?"))
            final=time.time()
            tiempo=round(final-inicio,0)
    
            z1=numazar-numazar1

            if z == z1:
                print("Felicidades, resouesta correcta",end=" ")
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
                break
           

            numazar=random.randint(1,25)
            numazar1=random.randint(1,25)
            
            t=int(input("¿Cuanto es: "+str(numazar)+"+"+str(numazar1)+ " ?"))
            final=time.time()
            tiempo=round(final-inicio,0)
            t1=numazar+numazar1
            if t == t1:
                print("Felicidades, resouesta correcta",end=" ")
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