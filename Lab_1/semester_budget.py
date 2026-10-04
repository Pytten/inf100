
print("Hva er budsjettet ditt?")
budsjett = int(input())

print("Hvor mye bruker du på bolig?")
bolig = int(input())

print("Hvor mye bruker du på mat?")
mat = int(input())

kaffe_budsjett = budsjett - bolig -mat
kaffe_pris = 500//11
kopper_kaffe = kaffe_budsjett//kaffe_pris

print(f"Det er {kaffe_budsjett} NOK igjen, det er nok til {kopper_kaffe} kopper kaffe!")