departamentosColombia=[]

for i in range(int(input("Digite el numero de departamentos: "))):
    
    departamentos = (input("escriba el departamento: "))
    departamentosColombia.append(departamentos)
    
print("los ultimos 2 departamentos ingresados fueron: ",{departamentosColombia[-2]},{departamentosColombia[-1]})

departamentosColombia.sort(reverse=True)
print(departamentosColombia)

#punto7

print("la longitud de la lista es de: ", len(departamentosColombia))
