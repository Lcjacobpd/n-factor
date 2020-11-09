'''
Tessallate.py
    written by Jacob Dickens, Nov 2020

    Basic principle:
        Given some integer N, find a, b, c such that
        N = a * b * c where a, b and c are as close
        in value as is possible.
'''

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
    parser.add_argument(
        'num',
        type=int,
        help='Original number'
    )
    parser.add_argument(
        '--dim',
        type=int,
        default=3,
        help='Dimensions'
    )

    args = parser.parse_args()
    if args.num < 1 or args.dim < 1:
        raise argparse.ArgumentTypeError(F"{args.num} isn't a positive int")

    return args


def Factor(num):
    '''
    Calculate factor tree leaves
    '''
    if num in PRIMES:
        FACTORS.append(num)
        return

    for i in range(2, int(num/2) + 1):
        if num % i != 0:
            continue

        # else, i cleanly divides num
        FACTORS.append(i)
        Factor(int(num/i))
        return


def CatchPrime(num):
    '''
    Include potential missing prime in FACTORS
    '''
    product = 1
    for item in FACTORS:
        product *= item

    if num != product:  # append missing prime
        FACTORS.append(num/product)


def nRootx(n, x):
    '''
    Determine the n root of x
    '''
    root = x ** (1.0 / n)
    return root


def Condense(num, dim):
    '''
    Condense the factor list to desired length
    '''
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
    '''
    Main program
    '''
    param = ParseArgs()

    Factor(param.num)  # updates FACTORS
    CatchPrime(param.num)
    print(F'Factors:\n{FACTORS}\n')

    result = Condense(param.num, param.dim)
    print(F'Final: {result}\n')


if __name__ == '__main__':
    main()
