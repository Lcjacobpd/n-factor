# Tessallate.py

```
While (Factor_List is too long):
    Case 1: One too many items
        Merge first two items
        DONE
    
    Case 2: List contains a large item
        Merge first and second largest items
        LOOP

    Case 3: List is roughly even distribution
        Merge first and last item
        LOOP


# else Factor_List is not too long
if (Factor_List is too short):
    append 1's as necessary
    DONE

if (Factor_List length is correct)
    DONE
```
