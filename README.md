# Factor.py

## Basic Outline:

The purpose of this program is to essentially determine the dimensions of a
given volume. This sounds quite simple at first, the caviot is that the value
of each axis dimension needs to be as close to an even distribution as
possible. This esentially means that when we visualise it as a three
dimensional shape.we're doing our best to make a cube.

First, the tail factors of the original number are calculated and collected
in a list. This list is pre-sorted from least to greatest which will be
helpful in the next phase when we try to intellegently recombine items until
only 2-3 remain (Or however many are specified in the dimension parameter).

The solution that I have arrived at looks something like the following
pseudocode. 

```Pseudo
While (factor_List > dimensions):
    # Case 1: List is 1 item too long
    # Combine the first 2 items

    # Case 2: List contains a large value
    # Combine first and second largest

    # Case 3: List is mostly even distribution
    # Combine first and last items

# factor list is <= desired dimension
# Add 1's as needed and crop to size
```
-------------------------------------------------------------------------------

## Flowchart Representation:

<img src="docs/img/flow.png"/>


-------------------------------------------------------------------------------
Last Updated - 11/9/2020
