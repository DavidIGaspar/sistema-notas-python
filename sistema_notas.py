print("=== SISTEMA DE NOTAS ===")

nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print("\n===== RESULTADO =====")
print(f"Aluno: {nome}")
print(f"Média: {media:.2f}")

if media >= 7:
    print("Situação: APROVADO")
elif media >= 5:
    print("Situação: RECUPERAÇÃO")
else:
    print("Situação: REPROVADO")
