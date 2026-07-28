#Declaração de variáveis
anoNascimento:int = 0
anoAtual:int = 0
idade: int = 0
futuraIdade: int = 0
#Início
anoNascimento = int(input("Digite o seu ano de nascimento: "))
anoAtual = int(input("Digite o ano atual: "))

idade = anoAtual - anoNascimento
futuraIdade = idade + 17

print("Você tem", idade, "anos e depois de 17 anos terá", futuraIdade, "anos")
#Fim