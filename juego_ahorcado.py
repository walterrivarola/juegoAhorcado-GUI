from random import *

ahoracado = ['tomate', 'bytemain', 'pasion', 'zapatero', 'espejo']

aleatorio = choice(ahoracado)

#print(aleatorio)
lista = []
incognita = []

for item in aleatorio:
    lista.append(item)

#print(lista)

def iniciarJuego():
    contador = 0
    print("Bienvenido al juego del 'Ahorcado'.\nAdivina la frase antes de quese agoten tus 6 vidas.")

    for item in aleatorio:
        incognita.append('-')
    print(incognita)


def intentoJugador(letra):
    #print(letra)
    vidas = 0
    final = 0
    while vidas < 6:
        intento = input("Ingrese una letra: ").lower()
        indice = 0
        contador = 0
        for item in letra:
            while indice < len(letra):
                if intento == letra[indice]:
                    #print(f"La letra {intento} se encuentra en el espacio {indice}")
                    #print(f"Posicion {letra[indice]}")
                    incognita.pop(indice)
                    incognita.insert(indice,intento)
                    print(incognita)
                    final += 1
                else:
                    contador += 1
                indice += 1
        if contador == len(letra):
            vidas +=1
            print(f"Te equivocaste, sólo te quedan {6-vidas} vidas")
        elif final == len(letra):
            return incognita, lista



def juegoFinalizado(resultado, lista):
    if incognita == lista:
        print("FELICIDADES HAS GANADO")

iniciarJuego()
intentoJugador(lista)
juegoFinalizado(incognita, lista)