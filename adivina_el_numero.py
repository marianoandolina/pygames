from random import randint
import time

print('Bienvenido a adivina el Numero!')
print()
print('Como es tu nombre?')
nombre = input()
print()
print(f'Hola {nombre}')
print()
time.sleep(2)
print()
print('Estoy pensando un numero entre 1 y 40')
print('Puedes adivinarlo en no mas de 5 intentos?')
print('Ingresa el numero que creas que estoy pensado')

intentos = 0
numero_random = randint(1, 40)

while intentos < 5:

    numero_usuario = int(input())

    intentos = intentos + 1

    if numero_usuario < numero_random:
        print('El numero ingresado es menor al que tengo pensado')
    elif numero_usuario > numero_random:
        print('El numero ingresado es mayor al que tengo pensado')
    elif numero_usuario == numero_random:
        print('Adivinaste!')
        break

if numero_usuario == numero_random:
    print()
    print(f"Muy bien {nombre}, adivinaste el numero en {intentos} intentos!!")
    print("******** FELICITACIONES *********")
    print("Leiste mi pensamiento a la perfeccion")

if numero_usuario != numero_random:
    print()
    print('Agotaste la cantidad de intentos!')
    print()
    print(f'El numero que estaba pensando era el {numero_random}')
    print()
    print("No te preocupes, puedes volver a intentar")
