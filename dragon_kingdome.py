import random
import time


def mostrar_introduccion():

    print()
    print()
    print("Estas en una tierra llena de dragones. Frente a ti")
    print("hay dos cuevas. En una de ellas, el dragon es generoso y")
    print("amigable y compartira su tesoro contigo. El otro dragon")
    print("es codicioso y esta hambriento, y te devorara inmediatamente.")
    print()


def elegir_cueva():
    cueva_elegida = ''
    while cueva_elegida != 1 and cueva_elegida != 2:
        print('A que cueva quieres entrar? (1 o 2)')
        cueva_elegida = input()

        return cueva_elegida


def explorar_cueva(cueva_elegida):
    print('Te aproximas a la cueva...')
    time.sleep(2)
    print('Un gran dragon aparece subitamente frente a ti! Abre sus fauces y...')
    print()
    time.sleep(2)


cueva_amigable = random.randint(1, 2)

if __name__ == "__main__":

    mostrar_introduccion()
    cueva_elegida = elegir_cueva()
    explorar_cueva(cueva_elegida)

    if cueva_elegida == str(cueva_amigable):
        print('Te regala su tesoro!!')
    else:
        print('Te engulle de un bocado')

    time.sleep(2)

    print('Quieres jugar de nuevo si o no?')
    x = input()

    if x == 'si' or x == 's':
        print('Cargando...')
        time.sleep(4)
        print()

    jugar_de_nuevo = x
    jugar_de_nuevo = jugar_de_nuevo.lower()

    while jugar_de_nuevo == 'si' or jugar_de_nuevo == 's':

        mostrar_introduccion()

        numero_de_cueva = elegir_cueva()

        explorar_cueva(numero_de_cueva)

        print('Quieres jugar de nuevo si o no?')

        jugar_de_nuevo = input()
