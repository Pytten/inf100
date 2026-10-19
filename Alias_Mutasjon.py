
import copy

a = [10, 20, 30]
# Alias
b = a

# kopi av a (ikke et alias)
c = copy.copy(a)

# Not destructive
# if a is mutated b will be mutated too
a[0] = 100
# a[0] og b [0] =100

# destruktiv muteringer er hvis en parameter/global (argumentene sine) variabel blir mutert
def mutasjon(min_a):
    min_a[2] = 33

min_variabel = [10, 20, 30]
mutasjon(min_variabel)
print(min_variabel)

# mutering av oppslagsverk:

alder = {
    'Trond' : 31,
    'Herman' : 22,
    'Odin' : 2000
}
alder['Trond']= 25

goals = [5, 10, 20 , 31]

# goals[0] = 5
# goals[1] = 10
# goals[2] = 20
# goals[3] = 31