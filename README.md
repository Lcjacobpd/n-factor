# Factor.py


## 1. Basic Outline

The purpose of this program is to essentially determine the dimensions of a
given volume. This sounds quite simple at first, the caviot is that the value
of each axis dimension needs to be as close to an even distribution as
possible. This esentially means that when we visualise it as a three
dimensional shape.we're doing our best to make a cube.

First, the tail factors of the original number are calculated and collected
in a list. This list is pre-sorted from least to greatest which will be
helpful in the next phase when we try to intellegently recombine items until
only 2-3 remain (Or however many are specified in the dimension parameter).


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
needed to reach the correct value.


## 3. Factor Recombination Method

In an attempt to immitate the logic of an actual person recombining the
condensing the list of prime factors, I arrived at the following psuedocode
implimentation.

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


## Flowchart Representation:
<br/>
<img src="docs/img/flow.png"/>
<br/><br/>

-------------------------------------------------------------------------------
Last Updated - 11/10/2020
