nome= str(input("Digite seu nome(mais de 3 caracteres): "))
while (len(nome)<4):
    print("Nome inválido")
    nome= str(input("Digite seu nome: "))
idade= int(input("Digite sua idade: "))
while (idade<0 or idade>122):
    print("Idade inválida")
    idade= int(input("Digite sua idade: "))
salario= float(input("Digite seu salário: "))
while (salario<0):
    print("Salário inválido")
    salario= float(input("Digite seu salário: "))
sexo= str(input("Digite seu sexo (f para feminino e m para masculino): "))
while (sexo!= "f" and sexo!= "m" and sexo!= "F" and sexo!= "M"):
    print("Sexo inválido")
    sexo= str(input("Digite seu sexo (f para feminino e m para masculino): "))
estado_civil= str(input("Digite seu estado civíl (s para solteiro, c para casado, v para viúvo e d para divorciado): "))
while (estado_civil!= "s" and estado_civil!= "c" and estado_civil!= "v" and estado_civil!= "d"):
    print("Estado civíl inválido")
    estado_civil= str(input("Digite seu estado civíl (s para solteiro, c para casado, v para viúvo e d para divorciado): "))