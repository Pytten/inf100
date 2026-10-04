
def smallest_absolute_difference(a):
    a ==[]
    b =sorted(a)
    n = len(a)
    diffrence = []

    for i in range(n-1):
        diffrence.append(b[i+1]-b[i])

    minste_forskjell = min(diffrence)
    
    return(minste_forskjell)
