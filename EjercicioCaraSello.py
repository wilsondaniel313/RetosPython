from random import randint
import random
repetir="s"
saldo = 100000
dinero=randint(1,2)



def lanzarMoneda(eleccion):
   eleccion = random.choice(["cara", "sello"])
   return eleccion
def ganar(saldo,DineroApostado):
    saldo=saldo+DineroApostado

def perder(saldo,DineroApostado):
   saldo=saldo-DineroApostado


def jugar():
  print("")
while True:
    print("\2========================\2")
    print(f"| BIENVENIDO A CARISELLAZO |")
    print("\2========================\2")
    DineroApostado=int(input(f"Digite La Cantidad De Dinero Que Va A Apostar, Recuerde Que Su Saldo es de Es De {saldo} mil pesos \n"))
    eleccion=int(input("digite 1 para escoger Cara o 2 Para Sello \n"))
    ganar(eleccion,DineroApostado)
    perder(eleccion,DineroApostado)
 
    if dinero==1 and eleccion==1:
        print(f"Salió Cara, usted escogió cara, Ganaste!...  Su saldo Actual es : {saldo} ")
        saldo=saldo+DineroApostado
    elif dinero==1 and eleccion==2:
        print(f"Salió Cara, usted escogió Sello, Perdiste!...  Su saldo Actual es :  {saldo} ")
        saldo=saldo-DineroApostado
    elif dinero==2 and eleccion==2:
        print(f"Salió Sello, usted escogió Sello, Ganaste!...  Su saldo Actual es :   {saldo} ")
        saldo=saldo+DineroApostado
    elif dinero==2 and eleccion==1:
        print(f"Salió Sello, usted escogió Cara, Perdiste!...   Su saldo Actual es :   {saldo} ")
        saldo=saldo-DineroApostado
    
   
   
    jugarnuevamente = input("¿Deseas jugar nuevamente? (s/n): ")
    if jugarnuevamente.lower() != "s":
     break
    


