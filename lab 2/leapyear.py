
def is_leap_year(year):
 
 year % 4 == 0
 while True:
    if year % 100 == 0 and year % 400 == 0:
        return(True)
        break
    elif  year % 100 == 0 and year % 400 !=0:
        return(False)
        break
    if year % 4 == 0:
        return(True)
        break
    else: 
        year % 4 != 0
        return(False)
        break
    
is_leap_year(year=int(input()))

def test_is_leap_year():
    print('Tester is_leap_year... ', end='')
    assert is_leap_year(2022) is False # Ikke delelig med 4
    assert is_leap_year(1996) is True  # Normalt skuddår
    assert is_leap_year(1900) is False # Delbart med 100
    assert is_leap_year(2000) is True  # Delbart med 400
    print('OK')

test_is_leap_year()

