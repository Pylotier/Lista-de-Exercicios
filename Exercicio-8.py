#Declaração de variáveis
deposito: float = 0.0
meses: int = 0
montante: float = 0.0

#Início
deposito = float(input("Digite quanto vai depósitar em poupança:"))
meses = int(input("Quandos meses você guardar o dinheito depósitado:"))

montante = deposito*(1+0.013)**meses

print("Resultado de", meses, "meses guardado é:", montante, "R$")
#Fim