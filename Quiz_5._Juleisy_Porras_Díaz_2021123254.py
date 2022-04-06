"""
Juego de adivinación
Entradas: número probable ingresado por el usuario.
Salidas: indicar si el número es mayor, menor o igual al generado al azar.
Restricciones: ninguna.
Realizado por Juleisy Priscila Porras Díaz
"""

import random

print("Estoy pensando un número entre 1 y 100.")
numeroAleatorio = random.randint(1, 100)
numeroUsuario = int(input("Su intento: "))
intentos = 1
while numeroUsuario != numeroAleatorio:
    intentos += 1
    if numeroUsuario > numeroAleatorio:
        print("Ha fallado, mi número es menor.")
    else:
        print("Ha fallado, mi número es mayor.")
    numeroUsuario = int(input("Su intento: "))

print("¡Felicidades, has adivinado!")
print("Hizo" ,intentos, "intentos en total")
print("Esta es la modificación")
