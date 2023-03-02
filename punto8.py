numeros = []

for i in range(int(input("Digite numero a ingresar"))):
    num = int(input("digite numero: "))
    numeros.append(num)
    numeros.sort()
    print(numeros)
    
for i in numeros:
    numeros.sort(reverse=True)
print(numeros) 

    