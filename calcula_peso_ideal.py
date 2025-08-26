altura = (float(input("Fornceça a Altura: ")))
sexo = input("Forneça o Sexo (M/F)")
if sexo.upper() == "M":
    peso_ideal = (72.7 * altura) - 58
elif sexo.upper() == "F":
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = None
print(f"{peso_ideal:.2f}")