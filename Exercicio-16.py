#Declaração de variáveis
horasFeitas: int = 0
dinheiroPorHora: float = 0.0
desconto: int = 0.0
numDescendentes: int = 0
salatioBruto: float = 0.0
salarioLiquido: float = 0
#Início
horasFeitas = int(input("Digite quantas horas foram feitas:"))
dinheiroPorHora = int(input("Quanto cada hora vale:"))
desconto = int(input("Disconto:"))
numDescendentes = int(input("Número de descendentes:"))

salatioBruto = horasFeitas*dinheiroPorHora
salarioLiquido = salatioBruto - (salatioBruto*desconto/100) + numDescendentes*100

print("Salário final:", salarioLiquido)

#Fim