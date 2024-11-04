# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
import random

cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []

print("Spanzuratoarea: ghiceste cuvantul!")
print("Progresul tau: " + " ".join(progres))
print(f"Incercari ramase: {incercari_ramase}")

while "_" in progres and incercari_ramase > 0:
    litera = input("Introdu o litera: ").lower()

    if len(litera) != 1 or not litera.isalpha():
        print("Caracter invalid, introdu o litera.")
        continue

    if litera in litere_incercate:
        print("Ai incercat deja aceasta litera. Incearca alta.")
        continue

    litere_incercate.append(litera)

    if litera in cuvant_de_ghicit:
        for i, caracter in enumerate(cuvant_de_ghicit):
            if caracter == litera:
                progres[i] = litera
        print("Corect! Litera se afla in cuvant.")
    else:
        incercari_ramase -= 1
        print(f"Gresit! Litera nu se afla in cuvant. Incercari ramase: {incercari_ramase}")

    print(" ".join(progres))

if "_" not in progres:
    print(f"Felicitari! Ai ghicit cuvantul: {cuvant_de_ghicit}.")
else:
    print(f"Ai pierdut! Cuvantul era: {cuvant_de_ghicit}.")