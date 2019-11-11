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
                if jugar == "no":
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
                if jugar == "no":
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
                if jugar == "no":
                    break

            import time
            import random

            print("Pasaste al Segundo nivel")
            print("Empieza en")
            from time import sleep
            for i in range(0,5):
                print(5-i)
                sleep(1)

            for a in range(0,2):
                inicio=time.time()

                numazar=random.randint(1,10)
                numazar1=random.randint(1,10)
                numazar2=random.randint(1,10)
                r=float(input("¿ Cuánto es: "+str(numazar2)+"*"+str(numazar)+"+"+str(numazar1)+ " ? = "))
                final=time.time()
                tiempo=round(final-inicio,0)
                r1=numazar2*numazar+numazar1

                if r == r1:
                    print("Respuesta correcta")
                    if tiempo < 7:
                        print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Excelente!")
                    if tiempo >= 7 and tiempo < 16:
                        print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡lo puedes hacer mejor!")
                    if tiempo >= 16:
                        print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡te falta practicar velocidad mental, pero vamos bien!")
                else:
                    print("Respuesta incorrecta")
                    print("GAME OVER")
                    break
               

                numazar=random.randint(1,10)
                numazar1=random.randint(1,10)
                numazar2=random.randint(1,10)
                z=int(input("¿ Cuánto es: "+str(numazar2)+"+"+str(numazar)+"-"+str(numazar1)+ " ? = "))
                final=time.time()
                tiempo=round(final-inicio,0)
    
                z1=numazar2+numazar-numazar1

                if z == z1:
                    print("Respuesta correcta")
                    if tiempo < 7:
                        print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Excelente!")
                    if tiempo >= 7 and tiempo < 16:
                        print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡lo puedes hacer mejor!")
                    if tiempo >= 16:
                        print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡te falta practicar velocidad mental, pero vamos bien!")
                    
                else:
                    print("Respuesta incorrecta")
                    print("GAME OVER ")
                    break
               

                numazar=random.randint(1,10)
                numazar1=random.randint(1,10)
                numazar2=random.randint(1,10)
                t=int(input("¿ Cuánto es: "+str(numazar2)+"-"+str(numazar)+"*"+str(numazar1)+ " ? = "))
                final=time.time()
                tiempo=round(final-inicio,0)
                t1=numazar2-numazar*numazar1
                if t == t1:
                    print("Respuesta correcta")
                    if tiempo < 7:
                        print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Excelente!")
                    if tiempo >= 7 and tiempo < 16:
                        print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡lo puedes hacer mejor!")
                    if tiempo >= 16:
                        print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡te falta practicar velocidad mental, pero vamos bien!")

                else:
                    print("Respuesta incorrecta")
                    break
               
                
                print("Next level")
                import time
                import random

                print("Pasaste al tercer nivel")
                print("Empieza en")
                from time import sleep
                for i in range(0,5):
                    print(5-i)
                    sleep(1)

                for a in range(0,2):
                    inicio=time.time()

                    numazar=random.randint(1,10)
                    numazar1=random.randint(1,10)
                    numazar2=2
                    numazar3=random.randint(1,10)
                    r=float(input("¿ Cuánto es: "+str(numazar)+"-"+str(numazar1)+"/"+str(numazar2)+"+"+str(numazar3)+ " ? = "))
                    final=time.time()
                    tiempo=round(final-inicio,0)
                    r1=numazar-numazar1/numazar2+numazar3

                    if r == r1:
                        print("Respuesta correcta")
                        if tiempo < 7:
                            print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Excelente!")
                        if tiempo >= 7 and tiempo < 16:
                            print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡lo puedes hacer mejor!")
                        if tiempo >= 16:
                             print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡te falta practicar velocidad mental, pero vamos bien!")
       
                    else:
                        print("Respuesta incorrecta")
                        print("GAME OVER")
                        break
                  

                    numazar=random.randint(1,10)
                    numazar1=random.randint(1,10)
                    numazar2=random.randint(1,10)
                    numazar3=4
                    z=float(input("¿ Cuánto es: "+str(numazar)+"-"+str(numazar1)+"*"+str(numazar2)+"/"+str(numazar3)+ " ? = "))
                    final=time.time()
                    tiempo=round(final-inicio,0)
                    z1=numazar-numazar1*numazar2/numazar3

                    if z == z1:
                        print("Respuesta correcta")
                        if tiempo < 7:
                             print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Excelente!")
                        if tiempo >= 7 and tiempo < 16:
                             print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡lo puedes hacer mejor!")
                        if tiempo >= 16:
                             print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡te falta practicar velocidad mental, pero vamos bien!")
       
                        
                    else:
                        print("Respuesta incorrecta")
                        print("GAME OVER ")
                        break
            
                   

                    numazar=random.randint(1,10)
                    numazar1=random.randint(1,10)
                    numazar2=random.randint(1,10)
                    numazar3=random.randint(1,10)
                    t=float(input("¿ Cuánto es: "+str(numazar)+"*"+str(numazar1)+"+"+str(numazar2)+"-"+str(numazar3)+ " ? = "))
                    final=time.time()
                    tiempo=round(final-inicio,0)
                    t1=numazar*numazar1+numazar2-numazar3
                    if t == t1:
                        print("Respuesta correcta")
                        if tiempo < 7:
                            print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Excelente!")
                        if tiempo >= 7 and tiempo < 16:
                            print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡lo puedes hacer mejor!")
                        if tiempo >= 16:
                            print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡te falta practicar velocidad mental, pero vamos bien!")
       
                        print("Ganaste el juego, mil de IQ")
                    else:
                        print("Respuesta incorrecta")
                        break
        
           
    print(" Hasta luego, regresa pronto ;-)  ")