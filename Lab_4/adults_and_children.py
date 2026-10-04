
import copy

def remove_children(people):
    people =={}
    people_2 = copy.copy(people)
    n = len(people)

    for i in range(n):
        if people_2[i]["age"]<18:
            people.remove(people_2[i])

def get_adults(people):
    people == {}
    adults_only = []
    n = len(people)

    for i in range(n):
        if people[i]["age"]>=18:
            adults_only.append(people[i])
    return(adults_only)
