import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

#print(round(random.random() * 100))
#print(int(random.random() * 100))

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 1
pontos = 1000

print("Qual nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Digite o nível: "))

if nivel == 1:
    total_de_tentativas = 10
elif nivel == 2:
    total_de_tentativas = 5
elif nivel == 3:
    total_de_tentativas = 2


for rodada in range(1, total_de_tentativas+1, 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if acertou:
        print(f"Parabéns, você acertou o número secreto, {numero_secreto}!")
        print(f"Sua pontuação foi {pontos}")
        break
    else:
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
        if maior:
            print("Você errou! Chute para cima.")
            if (rodada == total_de_tentativas):
                print("O número secreto era {}. Você fez {}".format(
                    numero_secreto, pontos))
        elif menor:
            print("Você errou! Chute para baixo.")
            if (rodada == total_de_tentativas):
                print("O número secreto era {}. Você fez {}".format(
                    numero_secreto, pontos))
        else:
            print("????")


print("Fim de jogo")