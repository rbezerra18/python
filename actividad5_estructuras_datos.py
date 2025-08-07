"""
Las agendas telefónicas son una guía donde se encuentran los datos de diferentes personas como
su nombre, domicilio y teléfono. Además, sirven para localizar personas, lugares o servicios.

Dicho lo anterior, escribe un programa que permita guardar nombres y números de teléfono.
El programa nos dará el siguiente menú:
(1) Consultar: pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono,
si no indicar que no existe.
(2) Añadir: pide un nombre. Si el nombre se encuentra en la agenda, indicar que ya existe,
si no solicitar el número de teléfono.
(3) Modificar: pide un nombre. Si el nombre no está en la agenda, indicar que no existe,
sino solicitar el nuevo número de teléfono.
(4) Borrar: pide un nombre. Si el nombre no está en la agenda, indicar que no existe,
sino eliminar el número de teléfono.
(5) Salir: si el usuario digita el número 5, detener el ciclo.

Los datos para este ejercicio son los siguientes:
- Jose: 302944
- Mario: 829455
- Angel: 829405
- Luis: 930594
"""

agenda = {
    "Jose": 302944,
    "Mario": 829455,
    "Angel": 829405,
    "Luis": 930594,
}

consultando = True

while consultando:
    print()
    print("MI AGENDA")
    print("----------------")
    print("1. Consultar\n"
          "2. Añadir\n"
          "3. Modificar\n"
          "4. Borrar\n"
          "5. Salir\n")

    opcion = ""

    while opcion not in ("1", "2", "3", "4", "5", "6"):
        opcion = input("-> ")

    if opcion == "1":
        #Pedir nombre
        nombre = input("Nombre: ")
        #Comprobar si el nombre está en el diccionario
        if nombre not in agenda:
            print("Este nombre no existe en la agenda.")
        else:
            telefono = agenda[nombre]
            print(nombre,":",telefono)

    elif opcion == "2":
        #Pedir nombre
        nombre = input("Nombre: ")
        #Comprobar si el nombre está en el diccionario
        if nombre in agenda:
            print("Este nombre ya está en la agenda.")
        else:
            telefono = int(input("Digite el teléfono: "))
            #Añadir el teléfono a la agenda
            agenda[nombre] = telefono
            print("El teléfono se ha añadido correctamente.")

    elif opcion == "3":
        #Pedir nombre
        nombre = input("Nombre: ")
        #Comprobar si el nombre está en el diccionario
        if nombre not in agenda:
            print("Este nombre no existe en la agenda.")
        else:
            telefono = int(input("Digite el teléfono: "))
            #Modificar el teléfono
            agenda[nombre] = telefono
            print("El teléfono se ha modificado correctamente.")

    elif opcion == "4":
        #Pedir nombre
        nombre = input("Nombre: ")
        #Comprobar si el nombre está en el diccionario
        if nombre not in agenda:
            print("Este nombre no existe en la agenda.")
        else:
            #Borrar el teléfono
            del agenda[nombre]
            print("El teléfono se ha borrado correctamente.")

    elif opcion == "5":
        #Cambiar la variable consultando
        consultando = False
        print("\nGracias por utilizar el programa.\n")
#Opcion extra para checar la lista completa
    elif opcion == "6":
        #Listar todos los contatos
        for nombre, telefono in agenda.items():
            print(nombre,":", telefono)