import sys

from alignment import Alignment
from container import Container
from solver import error


# Función utilizada para generar problemas de tipo mochila
# fileName nombre del archivo que se va a crear
# parameters rango que se utilizara para elegir los valores del problema generado
def generateContainer(fileName, parameters):
    container = Container(fileName, int(parameters[0])) # Se crea un objeto de tipo container
    container.generateElements(int(parameters[1]), int(parameters[2]), int(parameters[3]), int(parameters[4]),
                               int(parameters[5]), int(parameters[6]), int(parameters[7])) # Se crean los datos del problema
    container.writeResults() # Se escribe los datos generados en el archivo


# Método utilizado para crear problemas de tipo alineamiento de secuencias
# fileName nombre del archivo que se va a crear
# parameters tamaño de las hileras que se van a crear
def generateAlignment(fileName, parameters):
    alignment = Alignment(fileName)
    alignment.generate(int(parameters[0]), int(parameters[1]))
    alignment.writeResults()


# Función para mostrar ayuda al usuario
def helpMessage():
    print("Manual de ayuda")
    print("Si desea resolver un problema de mochila utilizando alguno de los siguiente:")
    print("python3 solver.py 1 archivo W N minPeso maxPeso minBeneficio maxBeneficio minCantidad maxCantidad")
    print("Lo cual genera un archivo con el nombre que fue indicado por parametros, con el contenido del problema "
          "solucionado")
    print("python3 solver.py 2 archivo largoH1 largoH2")
    print("El cual genera un archivo con un formato de correspondiente al problema de alineamiento de secuencias")


# Función principal del programa
def main(argv):
    if argv[1] == "[-h]": # Muestra ayuda al usuario
        helpMessage()
        exit(1)
    if argv[1] == '1': # Se creara un problema de tipo mochila
        generateContainer(argv[2], argv[3:])
    elif argv[1] == '2': # Se crea un problema de tipo alineamiento de secuencias
        generateAlignment(argv[2], argv[3:])
    else: # Se muestra un error
        error("Error, revise que utilice los parametros correctos. \n Utilize [-h] para ayuda.")


if __name__ == '__main__':
    main(sys.argv)
