repetir=0
while True:
    SubidasSITP=input("Usted Se Subio al Transporte? (s/n): ")
    if SubidasSITP:
        TipoTarjeta=input("Digite su tipo de Tarjeta \nPersonalizada \nNormal \n").lower()
        Saldo=int(input("Digite su Saldo Actual \n"))
        CantidadPasajes=int(input("Digite la cantidad de pasajes que va a pagar \n"))
        Pasaje=2900 
        CantidadPasajesAcumulados=Pasaje*CantidadPasajes
        Saldo=Saldo=CantidadPasajesAcumulados

        if TipoTarjeta=="Personalizada":
            if Saldo<Pasaje and CantidadPasajes==1:
                print("Reacarge su Tarjeta Antes de la Siguiente Parada",Saldo)
            elif Saldo>=0:
                print("Gracias... Su Saldo Actual es: ",Saldo)
            elif Saldo<0:
                 print("Saldo insuficiente ")
            else:
                print("Saldo  iNSUFICIENTE")             
        if  TipoTarjeta=="Normal":
             if Saldo<0:
                print("Saldo Insuficiente !!!!")
             elif Saldo >0:
                 print("Gracias!!... : ")   
    else:
        repetir=input("Desea Reaslizar Transbordo Digite (s/n):")
