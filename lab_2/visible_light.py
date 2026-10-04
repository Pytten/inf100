

enhet = {"nm",
         "THz"}
print("Angi enhet (nm eller THz):")

min_enhet = input()

if not min_enhet in enhet:
    print(f"Enheten må være i nm eller THz, det kan ikke være {min_enhet}.")

if min_enhet == "THz":
    print("Angi verdi i THz:")
    frekvens = int(input())
    bølgelengde = int(((3*10**8)/(frekvens*10**12))*10**9)

    if bølgelengde > 380 and bølgelengde <= 450:
        print("Violet")
    elif bølgelengde > 450 and bølgelengde <= 485:
        print("Blue")
    elif bølgelengde > 485 and bølgelengde <= 500:
        print("Cyan")
    elif bølgelengde > 500 and bølgelengde <= 565:
        print("Green")
    elif bølgelengde > 565 and bølgelengde <= 590:
        print("Yellow")
    elif bølgelengde  > 590 and bølgelengde <= 625:
        print("Orange")
    elif bølgelengde > 625 and bølgelengde <= 750:
        print("Red")
    else:
        print(f"{frekvens} Thz er utenfor det synlige spekteret.")


if min_enhet == "nm":
    print("Angi verdi i nm:")
    bølgelengde = int(input())
    if bølgelengde > 380 and bølgelengde <= 450:
        print("Violet")
    elif bølgelengde > 450 and bølgelengde <= 485:
        print("Blue")
    elif bølgelengde > 485 and bølgelengde <= 500:
        print("Cyan")
    elif bølgelengde > 500 and bølgelengde <= 565:
        print("Green")
    elif bølgelengde > 565 and bølgelengde <= 590:
        print("Yellow")
    elif bølgelengde  > 590 and bølgelengde <= 625:
        print("Orange")
    elif bølgelengde > 625 and bølgelengde <= 750:
        print("Red")
    else:
        print(f"{bølgelengde} nm er utenfor det synlige spekteret.")


