import os
os.system("cls")




from time import sleep
for i in range(0,5):
    print(5-i)
    sleep(1)



print("instrucciones")


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

    numazar=random.randint(1,10)
    numazar1=random.randint(1,10)
    numazar2=random.randint(1,10)
    r=int(input("¿Cuanto es: "+str(numazar2)+"*"+str(numazar)+"+"+str(numazar1)+ " ?"))

    numazar=random.randint(1,10)
    numazar1=random.randint(1,10)
    numazar2=random.randint(1,10)
    z=int(input("¿Cuanto es: "+str(numazar2)+"+"+str(numazar)+"*"+str(numazar1)+ " ?"))

    numazar=random.randint(1,10)
    numazar1=random.randint(1,10)
    numazar2=random.randint(1,10)
    t=int(input("¿Cuanto es: "+str(numazar2)+"-"+str(numazar)+"+"+str(numazar1)+ " ?"))

x = [r,z,t]
import random
y = random.randint(0,2)

