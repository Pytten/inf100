# Spør brukeren om første raden i en haiku. Lagre resultatet i en ny variabel.
# Spør brukeren om andre raden i en haiku. Lagre resultatet i en ny variabel.
# Spør brukeren om tredje raden i en haiku. Lagre resultatet i en ny variabel. Nå burde du ha tre variabeler.

# Finn lengden av hver linje (bruk len())
# Finn lengden av den lengste linjen (bruk max())

# Skriv ut en tom linje
# Skriv ut toppen av haiku-rammen. Lengden av den er basert på lengden av den lengste linjen, som vi fant i trinn 5, men pluss fire til. Vi trenger fire til fordi rammen skal gå på utsiden på begge sider (se eksempelkjøring nedenfor).
# Skriv ut hver av de tre linjene. Hver linje skal begynne med @ + et passende antall mellomrom. Deretterer følger selve teksten, og til slutt et nytt mellomrom og en ny alfakrøll. (Hvor mange mellomrom er passende for hver linje? )
# Skriv ut bunnen av rammen.
haiku = []
print('Første raden:')
haiku1 = input()
haiku.append(haiku1)

print('Andre raden:')
haiku2 = input()
haiku.append(haiku2)

print('Tredje raden:')
haiku3 = input()
haiku.append(haiku3)


lengste = (len(haiku[0]), len(haiku[1]), len(haiku[2]))
lengde = max(lengste)

print("")
print('@'*lengde + '@'*4)
print('@' +' ' + ' '*(lengde-len(haiku[0])) + haiku[0] + ' ' + '@')
print('@' +' ' + ' '*(lengde-len(haiku[1])) + haiku[1] + ' ' + '@')
print('@' +' ' + ' '*(lengde-len(haiku[2])) + haiku[2] + ' ' + '@')
print('@'*lengde + '@'*4)