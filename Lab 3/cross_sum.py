
def cross_sum(x):
    tverrsum_list = []

    s = str(x)
    
    count = 0
    tverrsum = 0
    for letter in s:
        tverrsum_list.append(letter)
    for _ in tverrsum_list:
        tverrsum = tverrsum + int(tverrsum_list[count])
        count +=1
        
    return(tverrsum)
        

def nth_cross_sum(n, x):
    tverrsum_nth = {}
    count = 0
    ny_x = 0
    
    while count < n:
        
        ny_x += 1

        if cross_sum(ny_x)== x:
            
            tverrsum_nth[n] = ny_x
            count +=1

        if ny_x >2000:
            break
    return(ny_x)



def test_nth_cross_sum():
    print('Tester nth_cross_sum... ', end='')
    assert nth_cross_sum(3, 7) == 25
    assert nth_cross_sum(1, 10) == 19
    assert nth_cross_sum(2, 10) == 28
    assert nth_cross_sum(10, 2) == 2000
    print('OK')
test_nth_cross_sum()