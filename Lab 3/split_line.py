
def get_endpoints(i, n, x_lo, x_hi):
    L_tot = x_hi - x_lo
    L_bit = L_tot/n
    x_ilo = x_lo + i* L_bit 
    x_ihi = x_ilo + L_bit
    print(x_ilo, x_ihi)
    return(x_ilo, x_ihi)


def main():

    if __name__ == '__main__':
       
        print('x_lo =')
        x_lo = float(input())

        print('x_hi =') 
        x_hi = float(input())

        print('n = ')
        n = int(input())

        for i in range(n):
            get_endpoints(i, n, x_lo, x_hi)
            

main()