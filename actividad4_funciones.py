"""
¿Se acercan tus próximas vacaciones en el extranjero y aún no has definido tu presupuesto?
Muy bien, un conversor de monedas puede ser muy útil en estos casos, porque te permitirá
conocer el valor de tu moneda en otro país y de esta manera puedes prepararte para pasear
y comprar el producto que más te guste. ¡Genial!

Escribamos un programa que permita calcular el valor de dólares o euros a:
- Pesos colombianos
- Yuanes
- Libras esterlinas

En esta actividad usaremos un valor promedio para determinar la equivalencia, mire las
siguientes tablas:

Dólar (USD)     Equivale a      Moneda
1               3750            pesos colombianos
1               6.37            yuanes
1               0.76            libras esterlinas

Euro (€)        Equivale a      Moneda
1               4000            pesos colombianos
1               6.93            yuanes
1               0.83            libras esterlinas

La función principal tendrá como parámetros:
- El nombre de la moneda actual
- El valor de la moneda actual
- Y el nombre de la moneda a convertir.

Y dentro de la función principal estarán dos subfunciones dolarTo() y euroTo(), las cuales
se encargarán de ejecutar las condiciones que permitirán obtener el valor equivalente a la
moneda actual.

Nota: Para obtener la equivalencia de una moneda u otra solo basta multiplicar:
moneda actual x equivalente. Por ejemplo, si un dólar es igual a 6.37 yuanes.
¿A cuánto equivale 8 dólares? Simplemente, multiplicamos: 8 x 6.37 = 50.94 yuanes.
"""

print("Bienvenido al conversor de monedas\n")

def conversor(moneda_actual, valor, moneda_a_convertir):
    if moneda_actual == 1:

        def dolarTo():
            if moneda_a_convertir == "1":
                print(f"$ {valor} dólares equivale a $ {valor * 3750:.2f} pesos colombianos.")
            elif moneda_a_convertir == "2":
                print(f"$ {valor} dólares equivale a ¥ {valor * 6.37:.2f} yuanes.")
            elif moneda_a_convertir == "3":
                print(f"$ {valor} dólares equivale a £ {valor * 0.76:.2f} libras esterlinas.")
            else:
                print("No se reconoce la moneda a convertir.")

        dolarTo()

    elif moneda_actual == 2:

        def euroTo():
            if moneda_a_convertir == "1":
                print(f"€ {valor} euros equivale a $ {valor * 4000:.2f} pesos colombianos.")
            elif moneda_a_convertir == "2":
                print(f"€ {valor} euros equivale a ¥ {valor * 6.93:.2f} yuanes.")
            elif moneda_a_convertir == "3":
                print(f"€ {valor} euros equivale a £ {valor * 0.83:.2f} libras esterlinas.")
            else:
                print("No se reconoce la moneda a convertir.")

        euroTo()

    else:
        print("No se reconoce la moneda a convertir.")

#Run
moneda_actual = int(input("Ingrese su moneda actual:\n"
                          "1. Dólar\n"
                          "2. Euro\n"))

print("")

valor = float(input("Ingrese el valor a convertir: \n"))

print("")

moneda_a_convertir = input("¿A qué moneda quiere convertilo?\n"
                               "1. Pesos colombianos\n"
                               "2. Yuanes\n"
                               "3. Libras esterlinas\n")

print("")

conversor(moneda_actual, valor, moneda_a_convertir)

"""
Realice un comentario multilínea dentro del programa y responda las siguientes preguntas:
50 dólares en pesos colombianos son 187500.00
30 euros en yuanes son 207.90
15 euros en libras esterlinas son 12.45

"""