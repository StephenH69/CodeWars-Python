# Given two integers a and b, which can be positive or negative,
# find the sum of all the numbers between including them too and
# return it. If the two numbers are equal return a or b.

# Note: a and b are not ordered!

def get_sum(a,b):
    no1 = 0
    no2 = 0
    total = 0
    if a < b:
        no1 = a
        no2 = b
    else:
        no1 = b
        no2 = a

    while no1 < no2 + 1:
        total += no1
        no1 += 1

    return total

def get_sum2(a,b):
    return sum(range(min(a,b), max(a,b)+1))

print(get_sum(-1,-3))
print(get_sum2(-1,-3))