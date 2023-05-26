from random import randint

print('Bienvenido a adivina el Numero!')
print('Como es tu nombre?')
nombre = input()
print(f'Bueno {nombre}, estoy pensando un numero entre 1 y 40')
print('Puedes adivinarlo?')
print('Ingresa el numero que creas que estoy pensado')

intentos = 0
numero_random = randint(1, 40)

while intentos < 6:

    numero_usuario = int(input())

    intentos = intentos + 1

    if numero_usuario < numero_random:
        print('El numero ingresado es menor al que tengo pensado')
    if numero_usuario > numero_random:
        print('El numero ingresado es mayor al que tengo pensado')
    if numero_usuario == numero_random:
        print('Adivinaste!')
        break

if numero_usuario == numero_usuario:
    print(
        f'Muy bien {nombre}, adivinaste el numero en {intentos} intentos!! Te felicito')

if numero_usuario != numero_random:
    print(f'No, el numero que estaba pensando era {numero_random}')
