
from pathlib import Path
import json

def load_emission_data(filename):
    content = Path(filename).read_text(encoding="utf-8")
    
    data = json.loads(content)
    return(data)




def get_deviations(data):
    deviations = []

    for _ in data["data"]:
        forecast = _["intensity"]["forecast"]
        actual = _["intensity"]["actual"]
        if forecast is not None and actual is not None:
            deviaton = abs(forecast - actual)
            deviations.append(deviaton)
    return(deviations)

get_deviations(data=load_emission_data(input()))




def count_values_larger_than(values, threshold):

    bigger = 0
    for larger in values:
        if larger > threshold:
            bigger +=1
    return(bigger)

def main():
    filename = input()
    threshold = 10
    data = load_emission_data(filename)
    deviations = get_deviations(data)
    antall_deviations = count_values_larger_than(deviations, threshold)
    print(f'Antall avvik større enn {threshold}: {antall_deviations}')



if __name__ == "__main__":
    main()
