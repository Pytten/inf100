
def compress(raw_binary):
    raw_binary ==''
    Antall = []
    n = len(raw_binary)
    i = 0



    while i < n:
        antall_zeros = 0
        antall_ones = 0

        while i < n and raw_binary[i] == '0':
            antall_zeros +=1
            i +=1

        if i < n or raw_binary[n-1] == '0':
            Antall.append(antall_zeros)

        while i <n and raw_binary[i] == '1':
            antall_ones +=1
            i +=1

        if i < n or raw_binary[n-1] == '1':
            Antall.append(antall_ones)

    return(Antall)
        

def decompress(compressed_binary):
    compressed_binary == []
    n = len(compressed_binary)
    raw_binary = ''
    i = 0

    while i < n:
        if i < n and i % 2 == 0:
            raw_binary =raw_binary+('0'*compressed_binary[i])
            i +=1
        if i < n and i % 2 != 0:
            raw_binary =raw_binary+('1'*compressed_binary[i])
            i +=1
    return(raw_binary)

def test_decompress():
    print('Tester decompress... ', end='')
    assert('0011100001111' == decompress([2, 3, 4, 4]))
    assert('110111111110' == decompress([0, 2, 1, 8, 1]))
    assert('0000' == decompress([4]))
    print('OK')
test_decompress()
