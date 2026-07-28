#Declaração de variáveis
quilos: float = 0.0
diasConsumido: int = 0
res: float = 0.0
#Início
quilos = float(input("Digite a quantidade de quilos:"))
diasConsumido = int(input("Quando a pessoa vai comer, sabendo que ela come 50g por dia:"))

res = quilos - (diasConsumido * 0.05)

print("De", quilos, "kg depois de", diasConsumido, "sobrou", res)
#Fim