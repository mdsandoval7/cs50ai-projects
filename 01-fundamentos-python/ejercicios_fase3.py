# Manuel Dionicio Sandoval Carranza 
# 1234888581 
# Grupo:213022_28
# Programa: Ingeniería en Inteligencia Artificial y Ciencias de Datos
# problema 9
n = int(input("ingresa el tamaño de la matriz: "))
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        valor = int(input("valor: "))
        fila.append(valor)
        matriz.append(fila)
print(matriz)

# Inicializamos el mayor y el menor con el primer elemento de la matriz
mayor = matriz[0][0]
menor = matriz[0][0]

# Recorremos la matriz nuevamente para buscar el mayor y el menor
for i in range(n):
    for j in range(n):
        # Comparamos si el número actual es mayor
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]
            
        # Comparamos si el número actual es menor
        if matriz[i][j] < menor:
            menor = matriz[i][j]

print("El número mayor es:", mayor)
print("El número menor es:", menor)
suma_total = mayor + menor
print("La suma del mayor y el menor es:", suma_total)
texto = str(suma_total) 
texto[::-1]
if texto == texto[::-1]:
    print("El resultado es un número capicúa.")
else:
    print("El resultado NO es un número capicúa.")

# Inicializamos el acumulador de la suma de números pares en 0
suma_pares = 0

# Recorremos la matriz para identificar y sumar los elementos pares
for i in range(n):
    for j in range(n):

# Evaluamos si el número de la celda es par (residuo de dividir entre 2 es 0)
        if matriz[i][j] % 2 == 0:
            suma_pares += matriz[i][j]
            binario = bin(suma_pares)[2:]  # Convertimos a binario y eliminamos el prefijo '0b'
print("La suma de los números pares es:", suma_pares)
print("Su representación en binario es:", bin(suma_pares))