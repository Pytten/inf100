
from pathlib import Path


content_string = Path('people.csv').read_text(encoding='utf-8')

counts = {
    'a' : 0,
    'b' : 0,
    'c' : 0
}

for letter in content_string:
    if letter in counts:
        counts[letter] = counts[letter] +1
    else:
        counts[letter] = 1

for key in counts:
    print(f'{key} : {counts[key]}')