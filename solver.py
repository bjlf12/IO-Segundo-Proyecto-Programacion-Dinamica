import sys
from datetime import datetime

from alignment import Alignment
from container import Container


# Función para imprimir errores
def error(message):
    exit(message)


# Función para imprimir ayuda al usuario
def helpMessage():
    print("Manual de ayuda")
    print("Si desea resolver un problema de mochila utilizando alguno de los siguiente:")
    print("python3 solver.py 1 1 archivo")
    print("python3 solver.py 1 2 archivo")
    print("El primero para utilizar fuerza bruta y el segundo programación dinamica")
    print("Donde el archivo posee un formato de:")
    print("Archivo de entrada: mochila1.txt\nlinea 1: Peso máximo soportado por el contenedor\nlinea 2: elemento i "
          "(peso, beneficio, cantidad)\nlinea n+1: elemento n (peso, beneficio, cantidad)")
    print("Si desea resolver un problema de alineamiento de secuencias utilizando alguno de los siguiente:")
    print("python3 solver.py 2 1 archivo")
    print("python3 solver.py 2 2 archivo")
    print("El primero para utilizar fuerza bruta y el segundo programación dinamica")
    print("Con un formato de archivo:")
    print("valoriguales,valordistintos,valorgap\nhilera1\nhilera2")


# Funcion utilizada para elegir que tipo de resolución se desea utilizar
# method: 1 corresponde a fuerza bruta y 2 corresponde a programación dinámica
# fileName archivo que contiene la información de
def solveContainer(method, fileName):
    container = Container(fileName) # Se inicializa el objeto
    container.readFile() # Se lee el contenido del archivo
    if method == '1': # Se resuelve con fuerza bruta
        # start = datetime.now()
        bag = container.bruteForceSolving() # Se resulve
        container.printResults(bag) # Se imprime los resultados
        # print(datetime.now() - start)

    elif method == '2': # Se resuelva con programación dinamica
        # start = datetime.now()
        bag = container.dynamicSolving() # Se resuelve
        container.printResults(bag) # Se imprime el resultado
        # print(datetime.now() - start)
    else:
        error("Error, revise que utilice los parametros correctos. \n Utilize [-h] para ayuda.")


# Funcion utilizada para elegir que tipo de resolución se desea utilizar para alineamiento de secuencias
# method: 1 corresponde a fuerza bruta y 2 corresponde a programación dinámica
# fileName archivo que contiene la información de
def solveAlignment(method, fileName):
    alignment = Alignment(fileName) # Se crea el archivo
    alignment.readFile() # Se lee el archivo con la información
    if method == '1': # Se elige fuerza bruta
        # start = datetime.now()
        result, result1, result2 = alignment.bruteForceSolving() # Se resuelve
        alignment.printBruteForce(result, result1, result2) # Se imprime los resultados
        # print(datetime.now() - start)
    elif method == '2':
        start = datetime.now()
        matrix, moves, result, result1, result2 = alignment.dynamicSolving() # Se resuelve
        alignment.printDynamic(matrix, moves, result, result1, result2) # Se imprime los resultados
        # print(datetime.now() - start)
    else:
        error("Error, revise que utilice los parametros correctos. \n Utilize [-h] para ayuda.")


# Función principal del programa
# args argumentos obtenidos desde la terminal
def main(args):
    if args[1] == "[-h]": # Se muestra información relevante para utilizar el programa
        helpMessage()
        exit(1)
    elif args[1] == '1': # Se resuelve un problema de mochila
        solveContainer(args[2], args[3])
    elif args[1] == '2': # Se resuelve un problema de alineamiento de secuencias
        solveAlignment(args[2], args[3])
    else: # Muentra un mensaje de error
        error("Error, revise que utilice los parametros correctos. \n Utilize [-h] para ayuda.")


if __name__ == '__main__':
    main(sys.argv)
