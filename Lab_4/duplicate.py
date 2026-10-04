
def duplicate(numbers):
    numbers == []
    i = 0
    n = len(numbers)
    for i in range(n):
        numbers[i] = numbers[i]*2
        i += 1
    


def duplicated(numbers):
    numbers == []
    numbers_2 = []
    i = 0
    n = len(numbers)
    for i in range(n):
        numbers_2.append(numbers[i]*2)
        i += 1
    return numbers_2

def test_duplicated():
    print('Testing duplicated...', end=' ', flush=True)

    # Test 1
    arg = [2, 3, 10, 3, 4]
    return_val = duplicated(arg)
    expected = [4, 6, 20, 6, 8]
    assert return_val == expected
    assert arg == [2, 3, 10, 3, 4]

    # Test 2
    arg = [3, 2]
    return_val = duplicated(duplicated(arg))
    expected = [12, 8]
    assert return_val == expected
    assert arg == [3, 2]

    print('OK')
test_duplicated()