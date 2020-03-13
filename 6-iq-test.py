# IQ Test
# Bob is preparing to pass IQ test.
# The most frequent task in this test is to find out which 
# one of the given numbers differs from the others. 
# Bob observed that one number usually differs from the others in evenness. 
# Help Bob — to check his answers, he needs a program that among 
# the given numbers finds one that is different in evenness, and return a 
# position of this number.

# iq_test("2 4 7 8 10") => 3 // 
# Third number is odd, while the rest of the numbers are even

# iq_test("1 2 1 1") => 2 // 
# Second number is even, while the rest of the numbers are odd

def iq_test(numbers):
    evens = 0
    odds = 0
    new_num = numbers.split(' ')
    for i in new_num:
        if int(i) % 2 == 0:
            evens += 1
        else:
            odds += 1
    if evens == 1:
        for j in new_num:
            if int(j) % 2 == 0:
                return new_num.index(j)+1
    else:
        for j in new_num:
            if int(j) % 2 == 1:
                return new_num.index(j)+1



def iq_test2(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1



print(iq_test("2 4 7 8 10"))
print(iq_test("1 2 1 1"))

print(iq_test2("2 4 7 8 10"))
print(iq_test2("1 2 1 1"))