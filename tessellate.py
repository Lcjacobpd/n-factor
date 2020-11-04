import argparse


FACTORS = []
PRIMES = [
    1, 2, 3, 5, 7, 11, 13, 17, 19, 23,
    29, 31, 37, 41, 43, 47, 53, 59, 61,
    67, 71, 73, 79, 83, 89, 97
]

def ParseArgs():
    '''
    Process program arguments
    '''
    parser = argparse.ArgumentParser('')
    parser.add_argument('num', type=int,)
    parser.add_argument('--dim', type=int, default=3)

    args = parser.parse_args()
    return args

def Factor(num):
    if num in PRIMES:
        FACTORS.append(num)
        return

    for i in range(2, int(num/2) + 1):
        if num % i != 0:
            continue

        # else
        FACTORS.append(i)
        Factor(int(num/i))
        return

def nRootx(n, x):
    root = x ** (1.0 / n)
    return root

def Condense(num, dim):
    print('Condensing...')
    temp = FACTORS
    length = len(FACTORS)

    while length > dim:  # list is too long    
        if length == (dim + 1):
            a = temp[0] * temp[1]
            temp = temp[2:]
            temp.insert(0, a)
            
            print(F'>> {temp}')
            print('Done!\n')
            return temp

        # check for large
        remainder = num
        large = False
        for f in temp:
            if f >= nRootx(dim, num):
                large = True
        
        if large:  # list contains large number
            remainder = int(remainder/f)
            print(F'Found Large: {f}')
            print(F'Remainder: {remainder}\n')

            b = temp[0] * temp[length-2]
            temp = temp[1:-2]
            temp.append(b)
            temp.append(f)
            print(F'>> {temp}')

            length -= 1
        
        else:  # list is roughly even distribution
            c = temp[0] * temp[length-1]
            temp = temp[1:-1]
            temp.append(c)
            print(F'>> {temp}')

            length -= 1

    # ----- end while
    if length < dim:  # list is too short
            temp = FACTORS
            temp.extend([1, 1])
            temp = temp[0:3]

            print(F'>> {temp}')
            print('Done!\n')
            return temp

    if length == dim:  # list is just right
                print('Done! Nothing to do\n')
                return FACTORS


def main():
    param = ParseArgs()

    Factor(param.num)  # updates FACTORS
    print('Factors:')
    print(F'{FACTORS}\n')

    result = Condense(param.num, param.dim)
    print(F'Final: {result}\n')


if __name__ == '__main__':
    main()