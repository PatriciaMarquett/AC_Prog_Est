import random

# Operações do aventureiro
def aventureiro_andar(aventureiro, direcao):
    if direcao == "W" and aventureiro["Posição"][1] > 0:
        aventureiro["Posição"][1] -= 1
        return True
    elif direcao == "A" and aventureiro["Posição"][0] > 0:
        aventureiro["Posição"][0] -= 1
        return True
    elif direcao == "S" and aventureiro["Posição"][1] < 9:
        aventureiro["Posição"][1] += 1
        return True
    elif direcao == "D" and aventureiro["Posição"][0] < 9:
        aventureiro["Posição"][0] += 1
        return True
    return False

def aventureiro_atacar(aventureiro):
    return aventureiro["Força"] + random.randint(1, 6)

def aventureiro_defender(aventureiro, dano):
    if dano > 0:
        aventureiro ["Vida"]-= dano
    dano -= aventureiro["Defesa"]
def ver_atributos_aventureiro(aventureiro):
    print("Nome:", aventureiro["Nome"])
    print("Força:", aventureiro["Força"])
    print("Defesa:", aventureiro["Defesa"])
    print("Vida:", aventureiro["Vida"])

def aventureiro_esta_vivo(aventureiro):
    return aventureiro["Vida"] > 0

# Operações do monstro
def novo_monstro():
    print("Um novo monstro apareceu!")
    return {
        "Força": random.randint(5, 25),
        "Vida": random.randint(10, 100)
    }

def monstro_atacar(monstro):
    return monstro["Força"]

def monstro_defender(monstro, dano):
    monstro["Vida"] -= dano

def monstro_esta_vivo(monstro):
    return monstro["Vida"] > 0

# Operações do mapa
def desenhar(aventureiro, tesouro):
    for y in range(10):
        for x in range(10):
            if [x, y] == aventureiro["Posição"]:
                print("@", end=" ")
            elif [x, y] == tesouro["Posição"]:
                print("X", end=" ")
            else:
                print(".", end=" ")
        print()

# Combate
def iniciar_combate(aventureiro, monstro):
    while True:
        # Aventureiro ataca
        dano_aventureiro = aventureiro_atacar(aventureiro)
        monstro_defender(monstro, dano_aventureiro)
        print(f"Você causou {dano_aventureiro} de dano ao monstro. Vida do monstro: {monstro['Vida']}")
        if not monstro_esta_vivo(monstro):
            print("Você derrotou o monstro!")
            return True

        # Monstro ataca
        dano_monstro = monstro_atacar(monstro)
        aventureiro_defender(aventureiro, dano_monstro)
        print(f"O monstro causou {dano_monstro} de dano a você. Sua vida atual: {aventureiro['Vida']}")
        if not aventureiro_esta_vivo(aventureiro):
            print("Você foi derrotado pelo monstro...")
            return False

# Operação principal do jogo
def movimentar(aventureiro, direcao):
    if not aventureiro_andar(aventureiro, direcao):
        return True

    efeito = random.choices(["nada", "monstro"], [0.6, 0.4])[0]
    if efeito == "monstro":
        monstro = novo_monstro()
        return iniciar_combate(aventureiro, monstro)

    return True

def gerar_tesouro():
    while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if [x, y] != [0, 0]:
            return {"Posição": [x, y]}


def main():
    aventureiro = {
        "Força": random.randint(10, 18),
        "Defesa": random.randint(10, 18),
        "Vida": random.randint(100, 120),
        "Posição": [0, 0]
    }

    tesouro = gerar_tesouro()

    aventureiro['Nome'] = input("Deseja buscar um tesouro? Primeiro, informe seu nome: ")
    print(f"Saudações, {aventureiro['Nome']}! Boa sorte!")

    desenhar(aventureiro, tesouro)

    while True:
        op = input("Insira o seu comando: ").upper()
        if op == "Q":
            print("Jogador fugiu. Jogo encerrado")
            return
        elif op == "T":
            ver_atributos_aventureiro(aventureiro)
        elif op in ["W", "A", "S", "D"]:
            if movimentar(aventureiro, op):
                desenhar(aventureiro, tesouro)
            else:
                print("Game Over...")
                break
        else:
            print(f"{aventureiro['Nome']}, não conheço essa opção! Tente novamente!")
        if aventureiro["Posição"][0] == tesouro["Posição"][0] and aventureiro["Posição"][1] == tesouro["Posição"][1]:
            print(f"Parabéns, {aventureiro['Nome']}! Você encontrou o tesouro!")
            break

if __name__ == "__main__":
    main()