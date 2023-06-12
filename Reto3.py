instructores2557861={}

while True:
    opcion=input("Digite que opcion deseas realizar : \n 1.Agregar/Modificar \n 2.Buscar \n 3.Borrar \n 4.listar  \n 5.Salir\n")
    if opcion == "1":
        nombre = input("Ingrese el nombre del instructor: ")
        if nombre in instructores2557861:
            print("Nombre: ", nombre)
            print("Materia: ", instructores2557861[nombre]["materia"])
            print("Teléfono: ", instructores2557861[nombre]["telefono"])
            
        else:
            materia = input("Ingrese la materia del instructor: ")
            telefono = input("Ingrese el teléfono del instructor: ")
            instructores2557861[nombre] = {"materia": materia, "telefono": telefono}
            print("Instructor agregado correctamente.")

    elif opcion == "2":
        busqueda = input("Ingrese el texto de búsqueda: ")
        resultados = [nombre for nombre in instructores2557861 if nombre.startswith(busqueda)]
        if resultados:
            print("Instructores cuyos nombres comienzan con '{}':".format(busqueda))
            for nombre in resultados:
                print("- Nombre:", nombre)
                print("  Materia:", instructores2557861[nombre]["materia"])
                print("  Teléfono:", instructores2557861[nombre]["telefono"])
        

    elif opcion == "3":
        nombreborrar = input("Ingrese el nombre del instructor a borrar: ")
        if nombreborrar in instructores2557861:
            confirmacion = input(f"¿Está seguro de que desea borrar '{nombreborrar}' de la agenda? (S/N): ".format(nombreborrar))
            if confirmacion.lower() == "s":
                del instructores2557861[nombreborrar]
                print("Instructor borrado correctamente.")
          

    elif opcion == "4":
        print("Lista de instructores en la agenda:")
        for nombre, datos in instructores2557861.items():
            print("- Nombre:", nombre)
            print("  Materia:", datos["materia"])
            print("  Teléfono:", datos["telefono"])

    elif opcion == "5":
        print("Usted ha esta Saliendo...")
        break

    