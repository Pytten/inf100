
from pathlib import Path
import json

content = Path("cryptids.json").read_text(encoding="utf-8")
data = json.loads(content)


length = len(data["kryptider"])
print(data["kryptider"][length-1]["navn"])

print(' ')

antall_navn = 0 
for antall_navn in range(length):
    print(f'{antall_navn + 1}.' ,data["kryptider"][antall_navn]["navn"]+ ':' ,data["kryptider"][antall_navn]["kjennetegn"])
    antall_navn+=1

print(' ')

for antall in data["kryptider"][0]:
    value = data["kryptider"][0][antall]
    print(f'{antall} : {value}', end= "\n")
