def par(x): #Função: def+nome+variável.
    return(x%2==0) #Retorna um valor para fora da função.
def par_ou_impar(x):
    if par(x):
        return("Par")
    else:
        return("Ímpar")
    
print(par_ou_impar(2)) #Mostra o valor da função.
print(par_ou_impar(3)) #Mostra o valor da função.
print(par_ou_impar(4)) #Mostra o valor da função.