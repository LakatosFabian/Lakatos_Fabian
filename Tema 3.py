meniu = ["papanasi"] * 10 + ["ceafa"] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

cantitati_comandate = {"guias": 0, "ceafa": 0, "papanasi": 0}

while studenti and comenzi and tavi:
    student = studenti.pop(0)
    comanda = comenzi.pop(0)

    if comanda in meniu:
        istoric_comenzi.append(comanda)
        cantitati_comandate[comanda] += 1
        print(f"{student} a comandat {comanda}.")
        tavi.pop()

print(f"S-au comandat {cantitati_comandate["guias"]} guias, {cantitati_comandate["ceafa"]} ceafa, {cantitati_comandate["papanasi"]} papanasi.")
print(f"Mai sunt {len(tavi)} tavi.")

print(f"Mai este ceafa: {cantitati_comandate["ceafa"] < 3}.")
print(f"Mai sunt papanasi: {cantitati_comandate["papanasi"] < 10}.")
print(f"Mai este guias: {cantitati_comandate["guias"] < 5}.")

total_venit = 0
for produs, pret in preturi:
    total_venit += cantitati_comandate[produs] * pret

print(f"Cantina a incasat: {total_venit} lei.")

produse_acceptabile = [p for p in preturi if p[1] <= 7]
print(f"Produse care costa cel mult 7 lei: {produse_acceptabile}.")