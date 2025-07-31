"""
Imagina que la tienda donde usted trabaja ofrece descuentos a los clientes en navidad,
de acuerdo con el monto de su compra. El criterio para establecer el descuento se muestra
a continuación:

Compra (USD)                                        Porcentaje
Si es menor a 80                                    0%
Si es mayor o igual a 80 y menor que 150            10%
Si es mayor o igual a 150 y menor o igual a 300     15%
Si es mayor a 300 y menor a 500                     20%

Teniendo en cuenta la tabla, te piden que escribas un programa que solicite el nombre del
cliente y el valor de la compra. Y que arroje como resultado:
- Nombre del cliente
- Valor de la compra sin descuento
- Valor de la compra con descuento.

Recuerde que para calcular el descuento primero debe multiplicar el valor de la compra por
el porcentaje. Luego, debe restar el valor obtenido al valor de la compra y con eso obtiene
el precio con descuento.
    descuento = valor_compra x porcentaje
    precio final = valor_compra - descuento
"""

#Solicitar información
nombre = input("Ingrese el nombre del cliente: ")
valor_compra = float(input("Ingrese el valor de la compra ($): "))

#Establecer condiciones
if valor_compra < 80:
    descuento = 0
elif 80 <= valor_compra < 150:
    descuento = 0.1
elif 150 <= valor_compra <= 300:
    descuento = 0.15
elif 300 < valor_compra < 500:
    descuento = 0.2

precio_final = valor_compra - (valor_compra * descuento)

print(f'Hola, {nombre}. El valor a pagar es\n'
      f'- Compra sin descuento $: {valor_compra:.2f}.\n'
      f'- Compra con descuento $: {precio_final:.2f}.')

"""
Ejemplos:
Angel Mario Villa Lopez realizó una compra de 455 usd. Con descuento: 364.00
Rosa Diaz realizó una compra de 105 usd. Con descuento: 94.50
Dilan Gonzales realizó una compra de 250 usd. Con descuento: 212.50
Kelly Daza realizó una compra de 430 usd. Con descuento: 344.00
"""