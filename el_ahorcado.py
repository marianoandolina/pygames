import random 
IMAGENES_AHORCADO = [''' 
 +---+ 
 |   | 
     | 
     | 
     | 
     | 
 z|=========''', '''
   +---+ 
   |   | 
   O   | 
       | 
       | 
       | 
 =========''', ''' 
  
   +---+ 
   |   | 
   O   | 
   |   | 
       | 
       | 
 =========''', ''' 
  
   +---+ 
   |   | 
   O   | 
  /|   | 
       | 
       | 
 =========''', ''' 
  
   +---+ 
   |   | 
   O   | 
  /|\  | 
       | 
       | 
 =========''', ''' 
  
   +---+ 
   |   | 
   O   | 
  /|\  | 
  /    | 
       | 
 =========''', ''' 
  
   +---+ 
   |   | 
   O   | 
  /|\  | 
  / \  | 
       | 
 =========''']

palabras = '''hormiga babuino tejon murcielago oso castor camello gato 
almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana
cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria 
buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca 
tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo 
tortuga comadreja ballena lobo wombat cebra'''.split()

def obtener_palabra(lista_de_palabras):
    indice_palabras = random.randint(0, len(lista_de_palabras))
    return lista_de_palabras[indice_palabras]

def mostrar_tablero(IMAGENES_AHORCADO, letras_incorrectas, letras_correctas, palabra_secreta):
    print(IMAGENES_AHORCADO[len(letras_incorrectas)])
    print()

    print(letras_incorrectas, end="")
    for letra in letras_incorrectas:
        print(letra, end="")
        print()

        espacios_vacios = "_" * len(palabra_secreta)

        for i in range(len(palabra_secreta)): #Completa los espacios vacios con las letras adivinadas
            print(letra, end="")
            print()

def obtener_intento(letras_probadas): #Devuelve la letra ingresada por el jugador. Verifica que el jugador halla ingresado solo una letra y no otra cosa.
    while True:
        print("Adivina una letra")
        intento = input()
        intento = intento.lower()
        abecedario = "a b c d e f g h i j k l m n ñ o p q r s t u v w x y z".split()

        if len(intento) != 1:
            print("Por favor introduce solo una letra")
        elif intento in letras_probadas:
            print("Ya probaste con esa letra, elige otra")
        elif intento not in abecedario:
            print("Por favor ingresa una letra")
        else:
            return intento

def jugar_de_nuevo(): #Esta funcion devuelve True si el jugador quiere volver a jugar, caso contrario devuelve false. 
    print("Quieres jugar de nuevo (si o no)")
    return input().lower.startswitch("s")


if __name__ == "__main__":

    print("Bienvenido al juego del AHORCADO")
    
    letras_incorrectas = ""
    letras_correctas = ""
    palabra_secreta = obtener_palabra(palabras)
    jugar_terminado = False

    while True:
        mostrar_tablero(IMAGENES_AHORCADO, letras_incorrectas, letras_correctas, palabra_secreta)

        #Permite al jugador escribir una letra
        intento = obtener_intento(letras_incorrectas + letras_correctas)

        if intento in palabra_secreta:
            letras_correctas = letras_correctas + intento

            #Verifica si el jugador ha ganado

            encontrado_todas_las_letras = True
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] not in letras_correctas:
                    encontrado_todas_las_letras = False
                    break
                if encontrado_todas_las_letras:
                    print("Si!! La palabra secreta es" + palabra_secreta + "Has Ganado!!")
                    jugar_terminado = True
                else:
                    letras_incorrectas = letras_incorrectas + intento

            #Comprobar si el jugador ha agotado sus intentos y ha perdido
            if len(letras_incorrectas) == len(IMAGENES_AHORCADO) - 1:
                mostrar_tablero(IMAGENES_AHORCADO, letras_incorrectas, letras_correctas, palabra_secreta)
                print("Te has quedado sin intentos\n despues de " + str(len(letras_incorrectas)) + "intentos fallidos y " + str(len(letras_correctas)) + "aciertos, la palabra era " + palabra_secreta )
                jugar_terminado = True

            #Preguntar al jugador si quiere volver a jugar (pero solo si el juego ha terminado).

            if jugar_terminado:
                if jugar_de_nuevo():
                    letras_incorrectas = ""
                    letras_correctas = ""
                    jugar_terminado = False
                    palabra_secreta = obtener_palabra(palabras)
                else:
                    break



            
        






        

