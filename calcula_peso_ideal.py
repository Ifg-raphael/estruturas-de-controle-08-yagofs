altura = (float(input("Digite a altura: ")))
sexo = input("Digite o sexo (M/F): ")
if sexo.upper() == "M":
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.7
print(f"O peso ideal é: {peso_ideal:.2f} kg")#