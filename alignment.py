import copy
import itertools
import random
import sys


# Función utilizada para verificar si dos chars son iguales
# return 1 si son iguales y -1 si son diferentes
def f(char1, char2):
    if char1 == char2:
        return 1
    return -1


# Función utilizada para comparar dos hileras
# return Scoring obtenido de la comparación
def compare(str1, str2):
    result = 0
    for i in range(len(str1)): # Se itera entre las hileras para comparar
        if str1[i] == "_" and str2[i] == "_": # Si son Gaps se ignora
            result += 0
        elif str1[i] == str2[i]: # Si ambos son iguales
            result += 1
        elif str1[i] == "_": # Si es un caracter y un gap
            result -= 2
        elif str2[i] == "_": # Si es un caracter y un gap
            result -= 2
        elif str1[i] != str2[i]: # Si los caracteres son distintos
            result -= 1
        else:
            result += 0
    return result # Scoring obtenido


# Clase utilizada para representar los datos acorde al problema de alineamiento de secuencias
class Alignment:
    match = 1
    disMatch = -1
    gap = -2

    # Constructor de la clase
    def __init__(self, fileName, firstLine=str(), secondLine=str()):
        self.fileName = fileName # Asigna el nombre del archivo
        self.firstLine = firstLine # Asigna el valor de la 1era hilera
        self.secondLine = secondLine # Asigna el valor de la 2da hilera

    # Función para obtener el string del objeto
    def __str__(self):
        return f"{type(self)}\nFirst row: {self.firstLine}\nSecond row: {self.secondLine}"

    # Lee la información utilizada durante el problema
    def readFile(self):
        file = open(self.fileName)
        self.match, self.disMatch, self.gap = map(int, file.readline().split(",")) # Lee el valor de igualdad, desigualdad, gap
        string1 = file.readline()
        self.firstLine = string1.rstrip('\n') # Lee la primer hilera
        string2 = file.readline()
        self.secondLine = string2.rstrip('\n') # Lee la segunda hilera
        file.close()

    # Función utilizada para crear las matrices asociadas a la solución dinámica
    # return matrices con la solución y con los movimientos
    def generateMatrix(self):
        string1 = self.firstLine
        string2 = self.secondLine
        result = [[0 for i in range(len(string1) + 1)] for j in range(len(string2) + 1)] # Crea una matriz de n * m de 0
        moves = copy.deepcopy(result) # Copia la matriz de ceros
        for i in range(len(string1) + 1): # Ingresa los valores de la primer fila
            result[0][i] = -2*i
            moves[0][i] = 2
        for i in range(len(string2) + 1): # Ingresa los valores de la primer columna
            result[i][0] = -2*i
            moves[i][0] = 1
        return result, moves

    # Función utilizada para resolver para resolver el problema mediante programación dinamica
    # return
    def dynamicAlignment(self, matrix, moves):
        string1 = self.secondLine
        string2 = self.firstLine
        for i in range(1, len(string1) + 1): # Llena la matriz con la información acorde a las comparaciones
            for j in range(1, len(string2) + 1):
                results = [matrix[i - 1][j - 1] + f(string1[i - 1], string2[j - 1]), matrix[i - 1][j] + self.gap,
                           matrix[i][j - 1] + self.gap] # Lista con las comparaciones
                indexMax = results.index(max(results)) # Mayor de los elementos de la lista
                moves[i][j] = indexMax # 0 va en diagonal, 1 va para arriba, 2 va a la izquierda
                matrix[i][j] = results[indexMax] # Guarda el valor en la posición mayor
        return matrix

    # Función utilizada para escribir los datos en un archivo del problemas generados
    def writeResults(self):
        result1 = self.firstLine
        result2 = self.secondLine
        file = open(self.fileName, "w")
        print(f"{self.match},{self.disMatch},{self.gap}")
        file.write(f"{self.match},{self.disMatch},{self.gap}")
        file.write("\n")
        file.write(result1)
        print(result1)
        file.write("\n")
        file.write(result2)
        print(result2)
        file.close()

    # Imprime los resultados obtenido de la solución por fuerza bruta
    def printBruteForce(self, result, result1, result2):
        print(f"Score final: {result}")
        print(f"Hilera1: {result1}")
        print(f"Hilera2: {result2}")

    # Resuelve el problema mediante fuerza bruta
    def bruteForceSolving(self):
        result = -sys.maxsize # Se asigna el mayor valor negativo que permite python
        result1 = ""
        result2 = ""
        for x in range(len(self.firstLine)): # Se le añade a la primer hilera x cantidad de gaps, hasta que sean igual al largo de la hilera
            string1 = ["{}"] * len(self.firstLine) + ["_"] * x # Se crea una lista con la hilera y  con x gaps
            for y in range(len(self.secondLine)): # Ahora se le añade a la 2da hilera y gaps
                string2 = ["{}"] * len(self.secondLine) + ["_"] * y # Se crea una lista con la hilera y  con y gaps
                for i in itertools.permutations(string1): # Se itera por todas las posibles permutaciones de la primer hilera
                    for j in itertools.permutations(string2): # Con las de la segunda
                        if len(i) == len(j): # Si las listas tienen el mismo largo
                            str1 = "".join(i)
                            str2 = "".join(j)
                            temp = compare(str1.format(*self.firstLine), str2.format(*self.secondLine)) # Se calcula el scoring
                            if temp > result: # Si es mayor al actual, se actualiza el valor del igual
                                result = temp
                                result1 = str1.format(*self.firstLine) # y el valor de las hileras resultado
                                result2 = str2.format(*self.secondLine)
        return result, result1, result2

    # Función utilizada para generar las hileras de tamaño n y m correspondientemente
    def generate(self, n, m):
        characters = ["A", "T", "C", "G"] # Lista de donde se eligiran los valores
        str1 = ""
        str2 = ""
        for i in range(n): # Se crea la 1er hilera
            str1 = str1 + random.choice(characters) # Se elige un caracter random de la lista
        for i in range(m): # Se crea la 2da hilera
            str2 = str2 + random.choice(characters) # Se elige un caracter random de la lista
        self.firstLine = str1
        self.secondLine = str2

    # Imprime en consola el resultado de la solución dinamica
    def printDynamic(self, matrix, moves, result, result1, result2):
        string2 = self.firstLine
        string1 = self.secondLine
        print("Tabla resultados:")
        for i in " " + string2: # Primero imprime la primer hilera que corresponde a los caracteres de la hilera 1
            print(f"{i:<10}", end="|")
        print()
        string1 = " " + string1
        for i in range(len(matrix)): # Ahora se imprime el contenido de la matriz resultado
            for j in range(len(matrix[0])):
                if not j:
                    print(f"{string1[i]:<10}", end="") # La primer columna corresponde a los valores de la hilera 2
                else:
                    if not moves[i][j]: # Se imprime con una flecha en diagonal
                        print(f"🡬{matrix[i][j]:<10}", end="")
                    elif moves[i][j] == 1: # Se imprime con una flecha hacia arriba
                        print(f"🡡{matrix[i][j]:<10}", end="")
                    elif moves[i][j] == 2: # # Se imprime con una flecha hacia la izquierda
                        print(f"←{matrix[i][j]:<10}", end="")
            print()
        print()
        print(f"Score final: {result}")
        print(f"Hilera1: {result1}")
        print(f"Hilera2: {result2}")

    # Función para realizar la segunda parte de la solución dinámica completar los strings
    # se recorre la matriz resultado desde N,M hasta 0,0
    def dynamicSolving(self):
        matrix, moves = self.generateMatrix()
        matrix = self.dynamicAlignment(matrix, moves)
        lenStr1 = rows = len(self.secondLine)
        lenStr2 = columns = len(self.firstLine)
        string2 = self.firstLine
        string1 = self.secondLine
        result = matrix[rows][columns]
        result1 = ""
        result2 = ""
        while rows or columns: # Mientras no se este en 0,0
            if moves[rows][columns] == 0: # Se asignan ambos valores en las hileras resultado
                lenStr1 -= 1
                lenStr2 -= 1
                result1 = string1[lenStr1] + result1
                result2 = string2[lenStr2] + result2
                rows -= 1 # Se mueve en diagonal
                columns -= 1
            elif moves[rows][columns] == 1: # Se agrega un gap en la primer hilera
                lenStr2 -= 1
                result1 = "_" + result1
                result2 = string2[lenStr2] + result2
                rows -= 1 # Se mueve hacia arriba
            elif moves[rows][columns] == 2: # Se agrega un gap en la 2da hilera
                lenStr1 -= 1
                result1 = string1[lenStr1] + result1
                result2 = "_" + result2
                columns -= 1 # Se mueve hacia la izquierda
        return matrix, moves, result, result1, result2
