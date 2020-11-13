# Factor.py


## 1. Basic Outline

The purpose of this program is to essentially determine the dimensions of a
given volume. This sounds quite simple at first, the caviot is that the value
of each axis dimension needs to be as close to an even distribution as
possible. This esentially means that when we visualise it as a three
dimensional shape. We're doing our best to find the vectors that most closely
make a cube.

At first glance this would seem to be quite simple as the cube root of any
given number would provide the optimal length of each edge. However, given
the context of process allocation, it quickly becomes more complicated;
a fraction of a process can not be allocated to a CPU. This intruduces the
final criteria of this program; all the dimensions must be clean integers.

As I am not much of a mathematician myself, I took a more logical approach
to the problem. First, the tail factors of the original number are calculated
and collectedin a list. This list is pre-sorted from least to greatest which
will be helpful in the next phase when we try to intellegently recombine items
until only 2-3 remain (Or however many are specified in the dimension
parameter).

<br/>

## 2. Prime Factorization Method

```Python
def get_prime(self, number):
    if number in self.prime_list:
        self.factor_list.append(number)
        return  # Is prime; done.

    for value in range(2, int(number/2) + 1):
        if number % value != 0:
            continue  # Not clean division; try next.

        # else, value cleanly divides number
        # append prime factor, repeat with remainder
        self.factor_list.append(value)
        self.get_prime(int(number/value))
        break
```

The product of the list of factors is then compared to the initial volume.
This catches any large prime numbers not found on the existing list of primes
needed to reach the correct value. Once the list is validated, it's time for it
to be recombined until the desired number dimensions is reached
(In our example so far we've been using three dimensions).

<br/>

## 3. Factor Recombination Method

In an attempt to immitate the logic of an actual person recombining the
condensing the list of prime factors, I arrived at the following psuedocode
implimentation. In which the smallest and largest items in the list are
combined until an overflow point is reached. This overflow point is the actual
cube root of the initial number.

> NOTE:
> In examples where the number of desired dimensions is more or less than
> three, the algorithm will adapt to fill the specification; setting the
> overflow to be the nth root. The same holds true for any other areas
> dependent on the number of dimensions.

Once the overflow is reached, the smallest and second largest numbers are 
combined. This is done until there are only four elements in the list
remaining. At which point the two smallest entries are combined and the
final distribution is achieved and sorted. Should the list of prime factors
be shorter than the desired number of dimensions, 1's are appended to the list
until it is long enough. And lastly, if the list of factors is already the
desired length, no action is performed before it is sorted.

```Python
def condense_list(self):
    while length > self.dimensions:
        if length == (self.dimensions + 1):
            # Case 1: List is 1 item too long
            # Combine the first 2 items
            # Done

        # Check for large values

        if contains_large:
            # Case 2: List contains a large value
            # Combine first and second largest
            length -= 1

        else:
            # Case 3: List is mostly even distribution
            # Combine first and last items
            length -= 1

    # End of while
    # Factor list is <= desired dimension
    if length < self.dimensions:
        # Extend to dimension length

    # Done
```

<br/>

## 4. Flowchart Representation:
<br/>
<img src="docs/img/flow.png"/>
<br/><br/>


## 5. Experiments

In the local directory experiments, there is an test script for trying
factor.py with a range of numbers. There are two parameters for the
experiment, the ceiling for the range of RGN and the optional count of those
generated numbers. For example, the following will Will perform 50 tests with
a range of numbers between 10-20.

```Shell
python test.py 20 --count 50
```

The following is a sample of the terminal output generated by the test script.
Each iteration detail is broken into three parts; the iteration, the original
number, and the collected factors. This information is recorded in a csv file
called data.csv. Returning to the volume representation of our problem, the
first column is the initial volume and all subsequent columns are the derived
dimensions.

```Shell
36. Original: 15 Final: [5, 3, 1]
37. Original: 16 Final: [4, 2, 2]
38. Original: 10 Final: [5, 2, 1]
39. Original: 12 Final: [3, 2, 2]
```

<br/>

-------------------------------------------------------------------------------
Last Updated - 11/13/2020
