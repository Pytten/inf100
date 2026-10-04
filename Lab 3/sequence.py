
def sequence_for(n):

 numbers = ''
 

 for num in range(n + 1):
        numbers+=str(num)
        numbers+=(' ')
 return(numbers)
 
def sequence_while(n):

 numbers = ''
 i = 0
 while i <= n:
    numbers+=str(i)
    numbers+=' '
    i= i + 1
 return(numbers)




def test_sequence_for():
    print("Tester sequence_for... ", end="")
    assert "0 1 2 3 4 5 " == sequence_for(5)
    assert "0 1 2 3 4 5 6 7 8 9 10 " == sequence_for(10)
    assert "0 " == sequence_for(0)
    print("OK")

test_sequence_for()

def test_sequence_while():
    print("Tester sequence_while... ", end="")
    assert "0 1 2 3 4 5 " == sequence_while(5)
    assert "0 1 2 3 4 5 6 7 8 9 10 " == sequence_while(10)
    assert "0 " == sequence_while(0)
    print("OK")

test_sequence_while()