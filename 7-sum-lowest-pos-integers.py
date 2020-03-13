# Create a function that returns the sum of the two lowest 
# positive numbers given an array of minimum 4 positive integers.
# No floats or non-positive integers will be passed.

# For example, when an array is passed like [19, 5, 42, 2, 77],
# the output should be 7.

# [10, 343445353, 3453445, 3453545353453] should return 3453455.

from heapq import nsmallest

def sum_two_smallest_numbers(numbers):
    return sum(nsmallest(2, numbers))

print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))
print(sum_two_smallest_numbers([7, 15, 12, 18, 22]))
print(sum_two_smallest_numbers([25, 42, 12, 18, 22]))