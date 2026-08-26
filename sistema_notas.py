cor = {
    "limpa": "\033[m",
    "azul": "\033[34m",
    "amarelo": "\033[33m",
    "pretoebranco": "\033[30m",
    "verde": "\033[32m",
    "vermelho": "\033[31m",
}

while True:

    va2 = input(f"{cor['pretoebranco']}Digite seu nome: {cor['limpa']}")

    va1 = int(input(f"{cor['pretoebranco']}Digite sua idade: {cor['limpa']}"))

    print(
        f"{cor['amarelo']}Olá {va2}! "
        f"Para saber se você passou de ano, preencha abaixo suas notas."
        f"{cor['limpa']}"
    )

    nota1 = float(
        input(f"{cor['azul']}{va2}, qual foi sua nota na AV1? {cor['limpa']}")
    )

    nota2 = float(input(f"{cor['azul']}E qual foi sua nota na AV2? {cor['limpa']}"))

    media = (nota1 + nota2) / 2

    print(f"Média: {media:.2f}")

    if media >= 7:
        print(f"parabens voce foi aprovado {media:.2f}")
    else:
        print("Você não atingiu a nota mínima...")

    nota3 = float(input(f"{cor['azul']}Qual foi sua nota na AV3? {cor['limpa']}"))

    if nota1 >= nota2:
        media = (nota1 + nota3) / 2
    else:
        media = (nota2 + nota3) / 2

    print(f"Média final: {media:.2f}")

    if media >= 7:
        print(f"Parabéns {va2}, você foi " f"{cor['verde']}APROVADO!{cor['limpa']}")
    else:
        print(
            f"Infelizmente você foi "
            f"{cor['vermelho']}REPROVADO{cor['limpa']}, {va2}!"
        )

    continua = input("Deseja calcular outra nota? (S/N): ").upper()

    if continua == "N":
        break

