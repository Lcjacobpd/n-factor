'''
test.py
    written by Jacob Dickens Nov, 2020

    Generate a custom range of numbers between 10 and
    specified cap to pass to the factor.py for testing.
'''

import argparse
import random
import subprocess
import csv


def parse_args():
    '''
    Process program arguments
    '''
    parser = argparse.ArgumentParser('')
    parser.add_argument(
        'cap',
        type=int,
        help='RNG value ceiling'
    )
    parser.add_argument(
        '--count',
        type=int,
        default=1000,
        help='Number array length'
    )

    args = parser.parse_args()
    if args.cap < 10:
        raise argparse.ArgumentTypeError(F"{args.cap} must be larger than 10!")
    if args.count < 1:
        raise argparse.ArgumentTypeError(F"{args.count} isn't a positive int!")

    return args


class Experiment:
    def __init__(self, ceiling: int, count: int):
        self.ceiling = ceiling
        self.count = count
        self.data = []

    def generate(self) -> None:
        '''
        Generate numbers within range
        '''
        for _ in range(0, self.count):
            value = random.randint(10, self.ceiling)
            self.data.append(value)

    def run_tests(self) -> None:
        '''
        Call factor.py with data list
        '''
        with open('data.csv', 'wt') as data_file:
            # Setup csv writer and add row header
            csv_writer = csv.writer(data_file)
            header = ['Original', 'Factors']
            csv_writer.writerow(header)

            # Run subprocess experiments
            # Recording output for csv data file
            for tally, value in enumerate(self.data):
                process_info = subprocess.run(
                    F'python ../factor.py {value}',
                    shell=True,
                    capture_output=True
                )

                # Fetch final output from factor.py
                # Format to string for csv
                result = process_info.stdout.decode('utf-8').split('\n')[-2]
                print(F'%2d. Original: {value} {result}' % (tally + 1))

                row = [value]
                for factor in result[8:-1].split(', '):
                    row.append(int(factor))
                csv_writer.writerow(row)


def main():
    '''
    Main program
    '''
    params = parse_args()
    exp = Experiment(params.cap, params.count)
    exp.generate()
    exp.run_tests()


if __name__ == '__main__':
    main()