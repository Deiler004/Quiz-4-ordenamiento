import random
import time



print("Hola mundo")

######################################################
def BubbleSort(l):
    l_len = len(l)
    for i in range(l_len):
        for j in range(l_len-1-i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l
######################################################
# Definición de la función quicksort
def QuickSort(arreglo, izquierda, derecha):
    if izquierda < derecha:
        indiceParticion = Particion(arreglo, izquierda, derecha)
        QuickSort(arreglo, izquierda, indiceParticion)
        QuickSort(arreglo, indiceParticion + 1, derecha)

# Definición de la función partición
def Particion(arreglo, izquierda, derecha):
    pivote = arreglo[izquierda]  # Elige el pivote como el primer elemento
    while True:
        # Avanza el índice de izquierda hasta que encuentre un valor mayor o igual al pivote
        while arreglo[izquierda] < pivote:
            izquierda += 1

        # Decrementa el índice de derecha hasta que encuentre un valor menor o igual al pivote
        while arreglo[derecha] > pivote:
            derecha -= 1

        # Si los índices se cruzan, devuelve el índice de la derecha
        if izquierda >= derecha:
            return derecha
        else:
            # Si no, intercambia los elementos desordenados
            arreglo[izquierda], arreglo[derecha] = arreglo[derecha], arreglo[izquierda]
            izquierda += 1
            derecha -= 1
######################################################

# mi_lista = [1,4,2,7,5,3]
# QuickSort(mi_lista, 0, len(mi_lista)-1)
# print("mi_lista = ", mi_lista)

######################################################

l_bubble = []
bubble_times = []
current_bubble_time = 0

for k in range(5):
    rango = (k+1)*1000

    for i in range(10):
        l_bubble = []
        for i in range(rango):
            l_bubble.append(random.randint(1, rango))

        start = time.time()
        BubbleSort(l_bubble)
        end = time.time()
        current_bubble_time += end-start
    bubble_times.append(current_bubble_time/10)
    current_bubble_time = 0
    # print("rango = ", rango, "bubble_times = ", bubble_times)
print("rango = ", rango, "bubble_times = ", bubble_times)

######################################################

l_quick = []
quick_times = []
current_quick_time = 0

for k in range(5):
    rango = (k+1)*1000

    for i in range(10):
        l_quick = []
        for i in range(rango):
            l_quick.append(random.randint(1, rango))

        start = time.time()
        QuickSort(l_quick, 0, len(l_quick)-1)
        end = time.time()
        current_quick_time += end-start
    quick_times.append(current_quick_time/10)
    current_quick_time = 0
    # print("rango = ", rango, "quick_times = ", quick_times)
print("rango = ", rango, "quick_times = ", quick_times)

######################################################



