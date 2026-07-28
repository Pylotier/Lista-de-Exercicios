# 40.	Receba 2 números inteiros. Verifique e mostre todos os números primos existentes entre eles.

#Declarar as váriaveis
n1: int = 0
n2: int = 0
res: int = 0
nDivisores: int = 0
#Inicio
n1 = int(input("Digite o 1° número: "))
n2 = int(input("Digite o 2° número: "))

if (n1 > n2):
    print("Entre",n1,"e",n2,"os número primos são:")
    for i in range(n2+1, n1, 1):
        for j in range (1, i+1):
            if (i%j == 0):
                nDivisores += 1
        # print(i,"%",j,"=", i%j)
        # print ("------------ Divisores:", nDivisores)
        
        # print("nDivisores reiniciou") 
                
elif (n1 < n2):
    print("Entre",n1,"e",n2,"os número primos são:")
    for i in range(n1+1, n2, 1):
        for j in range (1, i+1):
            if (i%j == 0):
                nDivisores += 1
        if (nDivisores == 2):
            print(i,"é primo")
        nDivisores = 0    
else:
    print("Número iguais")
#Fim