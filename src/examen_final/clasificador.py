*Ejercicio CLASIFICAADOR*: Clasificador de Clima (Condicionales if-elif-else)
Escribe un programa que pida al usuario la temperatura actual en grados Celsius (numero decimal) y muestre un mensaje segun los siguientes rangos:
- Si es menor a 10: "Mucho frio"
- Si esta entre 10 y 25 (inclusive): "Clima templado"
- Si esta entre 26 y 35 (inclusive): "Clima calido"
- Si es mayor a 35: "Alerta de calor extremo"
# Solicitar la temperatura actual al usuario

temperatura = float(input("Introduce la temperatura actual en grados Celsius: "))

if temperatura < 10:
    print("Mucho frio")
elif 10 <= temperatura <= 25:
    print("Clima templado")
elif 26 <= temperatura <= 35:
    print("Clima calido")
else:
    print("Alerta de calor extremo")
