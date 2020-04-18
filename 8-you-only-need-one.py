# You will be given an array a and a value x. 
# All you need to do is check whether the provided array contains the value.

# Array can contain numbers or strings. X can be either.

# Return true if the array contains the value, false if not.


def check(seq, elem):
    return elem in seq


print(check(["anyone", "want", "to", "hire", "me?"], "me?"))
print(check([78, 117, 110, 99, 104, 117, 107, 115], 8))