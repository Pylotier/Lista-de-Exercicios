# 44.	Receba o número da base e do expoente. Calcule e mostre o valor da potência.

#Declarar as váriaveis
base:int = 0
expoente:int = 0
cont: int = 0
res:int = 0
#Inicio
res = 1

base = int(input("Digite o valor da base:"))
expoente = int(input("Digite o valor do expoente:"))

while (expoente != cont):
    # print(base)
    cont += 1
    res *= base
print("Resultado a exponenciação de", expoente,"com base",base,"é:",res)

#Fim