
print("Skriv et ord:")
ord1 = input()
print("Skriv et annet ord:")
ord2 = input()
print("Skriv et siste ord:")
ord3 = input()

LENGDE_ORD = []
len(ord1)
LENGDE_ORD.append(len(ord1))

len(ord2)
LENGDE_ORD.append(len(ord2))

len(ord3)
LENGDE_ORD.append(len(ord3))

lengste = max(LENGDE_ORD)

print("")
if LENGDE_ORD[0] == lengste:
    print(ord1) 
if LENGDE_ORD[1] == lengste:
    print(ord2)
if LENGDE_ORD[2] == lengste:
    print(ord3)