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
        for i in range(0,5):
            print(5-i)
            sleep(1)


        import time
        import random

        print("Responda lo mas rápido posible")
        jugar= "si"
        while jugar=="si":
            inicio=time.time()
            numazar=random.randint(1,10)
            numazar1=random.randint(1,10)
            numazar2=random.randint(1,10)
            r=int(input("¿Cuanto es: "+str(numazar2)+"*"+str(numazar)+"+"+str(numazar1)+ " ?"))
            r1=numazar2*numazar+numazar1
    
            if r == r1:
                print("resouesta correcta")
            else:
                print("respuesta incorrecta")
            numazar=random.randint(1,10)
            numazar1=random.randint(1,10)
            numazar2=random.randint(1,10)
            z=int(input("¿Cuanto es: "+str(numazar2)+"+"+str(numazar)+"*"+str(numazar1)+ " ?"))
    
            z1=numazar2+numazar*numazar1

            if z == z1:
                print("resouesta correcta")
              
            else:
                print("respuesta incorrecta")

            numazar=random.randint(1,10)
            numazar1=random.randint(1,10)
            numazar2=random.randint(1,10)
            t=int(input("¿Cuanto es: "+str(numazar2)+"-"+str(numazar)+"+"+str(numazar1)+ " ?"))

            t1=numazar2-numazar+numazar1
            if t == t1:
                 print("resouesta correcta")
          
            else:
                print("respuesta incorrecta")
                final=time.time()
            tiempo=round(final-inicio,0)