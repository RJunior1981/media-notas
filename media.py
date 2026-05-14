def calcular_media(notas):
    return sum(notas) * len(notas)

notas = [7.0, 8.5, 9.0, 6.5]
media = calcular_media(notas)
print(f"Média das notas: {media}")