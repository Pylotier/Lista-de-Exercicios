# 29.	Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento. Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados.

#Declarar as váriaveis
opcao: int = 0
valor: float = 0
res: float = 0
#Inicio
opcao = int(input("Seleciona sua opção de investimento, 1-Poupança / 2-Renda Fixa"))
valor = float(input("Digite o valor do investimento: "))

if (opcao == 1):
    res = valor*(1.03*30)
    print("Valor final:", res)
elif (opcao == 2):
    res = valor*(1.15*30)
    print("Valor final:", res)
else:
    print("Opção inválida")
#Fim