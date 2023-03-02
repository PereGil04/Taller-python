lista = [23, 45, 25, 53, 4, 8, 100]

print(lista[4])

lista.sort()
print("Numeros de forma ascendente: ", lista)

menor = None
mayor = None
for numero in lista:
    if menor==None and mayor==None:
        menor=numero
        mayor=numero
    else:
        if numero<menor:
            menor=numero
        if numero>mayor:
            mayor=numero

print(f'El numero mayor es {mayor}')
print(f'El numero menor es {menor}')