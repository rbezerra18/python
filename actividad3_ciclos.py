"""
Imagina que culminaste el 5º semestre de la universidad, en el cual viste las siguientes
asignaturas: Seguridad Informática, Ingeniería Web, Inteligencia Artificial, Programación Móvil
y Redes; y las notas fueron las siguientes: 5.0, 4.5, 3.6, 3.9 y 4.3 respectivamente.

Teniendo claro esto, escribe un programa que solicite tu nombre completo, el nombre de las cinco
materias y la calificación de cada una. Y como resultado devuelve tu nombre y el promedio obtenido
en el semestre.

Recuerda que la fórmula para calcular el promedio es:
Promedio = (Nota1 + Nota2 + Nota3 + Nota4 + Nota5)/Cantidad de notas
"""

#Solicitar información
nombre = input("Nombre completo: ")
materias = 5

#Hacer un ciclo,pedir datos y sumar la calificación
contador = 1
sumatoria = 0

while contador <= materias:
    nombre_materia = input("Ingresa el nombre de la (" + str(contador) + ") materia: ")
    calificacion = float(input("Calificación obtenida en " + str(nombre_materia) + ": "))

    #Sumar la calificación a la sumatória
    sumatoria = sumatoria + calificacion

    #Aumentar el contador para no hacer un ciclo infinito
    contador += 1

#Hacer cálculos e imprimir resultados
promedio = sumatoria / materias
print("")
print("***RESULTADOS***")
print(f'Hola, {nombre} tienes un promedio de {promedio} en el 5º semestre.')

#Resultado: Roberto Bezerra de Oliveira Júnior, 4.26.