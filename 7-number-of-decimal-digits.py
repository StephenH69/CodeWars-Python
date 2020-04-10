# Determine the total number of digits in the integer (n>=0) given as input 
# to the function. For example, 9 is a single digit, 66 has 2 digits and 
# 128685 has 6 digits. Be careful to avoid overflows/underflows.

# All inputs will be valid.

def digits(n):
    return(len(str(n)))

print(digits(5))
print(digits(12345))
print(digits(9876543210))

# digits(5),1)
# digits(12345),5)
# digits(9876543210),10)