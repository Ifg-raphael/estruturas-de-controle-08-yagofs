altura = (float(input()))
sexo = input(" ")
if sexo.upper() == "M":
    peso_ideal = (72.7 * altura) - 58
elif sexo.upper() == "F":
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = 0
print(peso_ideal)