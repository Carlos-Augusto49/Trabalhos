lista=[]
lista_par=[]
lista_impar=[]
for i in range(10):
    i+= 1
    n= int(input("Digite o %d° número inteiro: "%i))
    lista.append(n)
    if (n %2==0):
        lista_par.append(n)
    else:
        lista_impar.append(n)
print(lista)
print(lista_par)
print(lista_impar)