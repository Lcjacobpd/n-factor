'''
test.py
    written by Jacob Dickens Nov, 2020

    Generate a range of numbers between 10 and user cap
    and iteratively call factor.py for testing.
    Save data for postrun analysis.
'''

import argparse
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
        help='Test value ceiling'
    )
    parser.add_argument(
        '--dim',
        type=int,
        help='Final factor count',
        default=3
    )

    args = parser.parse_args()
    if args.cap < 10:
        raise argparse.ArgumentTypeError(F"{args.cap} must be larger than 10!")

    if args.dim < 2:
        raise argparse.ArgumentTypeError(F"{args.dim} must be larger than 1!")

    return args


class Experiment:
    def __init__(self, ceiling: int, dimensions: int):
        self.ceiling = ceiling
        self.dim = dimensions

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
            for value in range(10, self.ceiling + 1):
                process_info = subprocess.run(
                    F'python ../factor.py {value} --dim {self.dim}',
                    shell=True,
                    capture_output=True
                )

                # Fetch final output from factor.py
                # Format to output to string
                output = process_info.stdout.decode('utf-8')
                result = output.split('\n')[-2][8:-1]  # Trim output
                print(F'{value} -> {result}')

                # Create csv data entry
                row = [value]
                for factor in result.split(', '):
                    row.append(int(factor))
                csv_writer.writerow(row)


def main():
    '''
    Main program
    '''
    params = parse_args()
    exp = Experiment(params.cap, params.dim)
    exp.run_tests()


if __name__ == '__main__':
    main()