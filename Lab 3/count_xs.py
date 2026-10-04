def count_xs(s):

    Antall_xs = 0


    for streng in s:
        if 'x' in streng:
            Antall_xs =+s.count('x')

    return(Antall_xs)

# count_xs(s = input())



# Din kode her
    # initialiser en variabel x_count til 0
    # for hvert tegn i strengen:
        # hvis tegnet er en x:
            # øk x_count med 1
    # returner x_count


def test_count_xs():
    print('Tester count_xs... ', end='')
    assert 0 == count_xs('foo bar hei')
    assert 1 == count_xs('x')
    assert 4 == count_xs('xxCoolDragonSlayer99xx')
    print('OK')

test_count_xs()