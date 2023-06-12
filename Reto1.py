instructores=[]
repetir="s"
while repetir=="s" or repetir=="s":
    agregarobjeto=input("Digite q opcion desea hacer:\n 1-ingresar un  Nombre de instructor  \n 2-Listar instructores que Estan en la lista \n 3-Modificar un Elemento de una Lista \n 4-Borrar un Elemento de una Lista \n 5-Buscar un elemento Particular  de la lista  \n 6-Ordenar la lista de instructores de la A-Z \n 7-Salir \n ")
    if agregarobjeto=="1":
        instructores.append(input("ingrese su nombre :  "))

    elif agregarobjeto=="2":
        instructores.append(print("lista de instructores  "))
        for i,e in enumerate(instructores):
            print("=================================================")
            print("En la posicion",i,"se encuentra el instructor",e)
         
    elif agregarobjeto=="3":
        modificar=int(input("ingrese su numero: \n"))
        valorNuevo=input("ingrese el nuevo instructor que desea agregar : \n")
        instructores[modificar]=valorNuevo
        print("El instructor ha sido modificado exitosamente.")


    elif agregarobjeto=="4":
        borrarInstructor=int(input("Ingrese el índice del instructor que desea borrar: "))
        instructores.pop(borrarInstructor)
        print("El instructor a sido Borrado Exitosamente")
    elif agregarobjeto=="5":
            nombre = input("Ingrese el nombre del instructor que desea buscar: ")
            encontrado = False
            for instructor in instructores:
                if instructor == nombre.lower():
                    encontrado = True
                    print(" el instructor se encuentra en la lista")
            if not encontrado:
                print("El instructor no se encuentra en la lista.")
                    
          
    elif agregarobjeto=="6":
        instructores.sort()
        print("la lista ha Sido ordenada")
    
    elif agregarobjeto == "7":
        print("=========================")
        print("| Gracias Vuelva Pronto |")
        print("=========================")
        break
