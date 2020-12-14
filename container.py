import random
from itertools import combinations


# Función utilizada para resolver el problema de la matriz de forma dinámica
def dynamicBag(elements, weight, elementsLen):
    memoized = [[0 for w in range(weight + 1)] for j in range(elementsLen + 1)] # Se crea un matriz de tamaño W * N de 0
    result = [] # Lista con los elementos seleccionados
    for k in range(1, elementsLen + 1): # Se itera entre la lista de elementos
        element, elementWeight, value = elements[k - 1]
        for w in range(1, weight + 1): # Se compara con los valores obtenidos agregando otros elementos
            if elementWeight > w: # Mientras aun se pueda incluir elementos en la mochila
                memoized[k][w] = memoized[k - 1][w] # Se actualiza el valor en el memoized
            else:
                memoized[k][w] = max(memoized[k - 1][w], memoized[k - 1][w - elementWeight] + value) # Se elige el mayor de aregar o no el elemento
    w = weight
    for j in range(elementsLen, 0, -1): # Se calcula los elementos que se agregan
        if memoized[j][w] != memoized[j - 1][w]:
            element, elementWeight, value = elements[j - 1]
            result.append(elements[j - 1]) # Se añade el elmento a la mochila
            w -= elementWeight # Se le resta al tamaño de la mochila
    return result


# Solución del problema de la mochina con fuerza bruta
def bruteForceBag(elements, weight, elementsLen):
    resultBenefice = 0
    result = list() # Lista con los elementos elegidos
    for k in range(elementsLen): # Se itera entre todos los elementos
        for combination in combinations(elements, k + 1): # y se calculan todas las combinaciones posible de agregar o no un elemento
            combinationWeight = sum([element[1] for element in combination]) # Se suma el precio de la combinación
            if combinationWeight <= weight: # Si es menor al valor actual
                combinationBenefice = sum([element[2] for element in combination]) # Se calcula las combinaciones
                if combinationBenefice > resultBenefice: # Si el valor obtenido es mayor se actualiza
                    resultBenefice = combinationBenefice
                    result = combination
    return [resultBenefice, result]


#Clase utilizada para los datos necesarios para la solución de la mochila
class Container:
    # Constructor de la clase
    def __init__(self, fileName, weight=0, elements=None):
        if elements is None:
            elements = list() # Asigna la lista de items
        self.fileName = fileName # Asigna el nombre del archivo
        self.weight = weight # Establece el tamaño de la matriz
        self.elements = elements
        self.v = list()

    # Función utilizada para obtener el objeto en string
    def __str__(self):
        return f"{type(self)}\nWeight: {self.weight}.\nElements: {self.elements}"

    # Función utilizada para leer los datos desde el archivo
    def readFile(self):
        file = open(self.fileName)
        self.weight = int(file.readline())
        count = 0
        for line in file:
            element = list(map(int, line.split(',')))
            self.elements.append([count] + element)
            count += 1
        file.close()

    # Método para obtener la solución mediante fuerza bruta
    def bruteForceSolving(self):
        listElements = list()
        for i in self.elements: # Agrega a la lista de elementos la cantidad de veces indicada de cada item
            for n in range(i[3]):
                listElements.append(i[:-1])
        bag = bruteForceBag(listElements, self.weight, len(listElements)) # Calcula el resultado optimo
        items = list()
        for i in range(len(self.elements)): # Ahora cuenta cuantas veces se va agregar el mismo articulo
            count = bag[1].count(self.elements[i][:-1])
            if count:
                items.append((i + 1, count))
        return [bag[0], items]

    # Función utilizada para resolver la mochila mediante programación lineal
    def dynamicSolving(self):
        listElements = list()
        for i in self.elements: # Agrega la cantida de elementos disponibles por item
            for n in range(i[3]):
                listElements.append(i[:-1])
        bag = dynamicBag(listElements, self.weight, len(listElements)) # Calcula la mejor mochila
        maxBenefit = sum(element[2] for element in bag) # Obtiene el beneficio de la mochila
        items = list()
        for i in range(len(self.elements)): # Se cuenta la cantidad de veces que esta un mismo item en la mochila
            count = bag.count(self.elements[i][:-1]) # Cuenta la cantidad de veces que se encuntra un item en la mochila
            if count:
                items.append((i + 1, count))
        return [maxBenefit, items]

    # Función utilizada para crear elementos entre los rangos establecidos
    def generateElements(self, quantity, minWeight, maxWeight, minBenefice, maxBenefice, minQuantity, maxQuantity):
        for i in range(quantity): # Se crean los n elementos indicados
            element = [i, random.randint(minWeight, maxWeight), random.randint(minBenefice, maxBenefice),
                       random.randint(minQuantity, maxQuantity)] # Se eligen valores en los rangos establecidos
            self.elements.append(element)

    # Función para elegir que algoritmo de solución se va utilizar
    def solver(self, method):
        if method == '2': # Dinamica
            return self.dynamicSolving()
        elif method == '1': # Fuerza bruta
            return self.bruteForceSolving()
        else:
            exit("Error, revise que utilice los parametros correctos. \n Utilize [-h] para ayuda.")

    # Función que imprime lso resultados obtenidos
    def printResults(self, bag):
        print(bag[0]) # Imprime el valor
        for i in bag[1]: # Imrpime los items inluidos
            print(f"{i[0]},{i[1]} #Articulo {i[0]}, {i[1]} unidades")

    # Función utilizada para escribir en un archivo los datos de los items creados en el generador
    def writeResults(self):
        file = open(self.fileName, 'w')
        file.write(str(self.weight)) # Escribe el tamaño de la mochila
        file.write("\n")
        print("Resultado:")
        for i in range(len(self.elements)):
            print(*self.elements[i][1:])
            file.write("{},{},{}".format(*self.elements[i][1:])) # Agrega los datos correspondiente a cada item creado
            file.write("\n")
        file.close()
