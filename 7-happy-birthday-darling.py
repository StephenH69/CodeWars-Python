# As you may know, once some people pass their teens, they jokingly only celebrate their 20th 
# or 21st birthday, forever. With some maths skills, that's totally possible - 
# you only need to select the correct number base!

# For example, if they turn 32, that's exactly 20 - in base 16... Already 39? That's just 21, in base 19!

# Your task is to translate the given age to the much desired 20 (or 21) years, and 
# indicate the number base, in the format specified below.

# Note: input will be always > 21

# Examples:
# 32 - -> "32? That's just 20, in base 16!"
# 39 - -> "39? That's just 21, in base 19!"

def womens_age(n):
    x = 11
    completed = False
    while completed == False:
        if (2 * x) == n:
            return f"{n}? That's just 20, in base {x}!"
        elif (2 * x) + 1 == n:
            return f"{n}? That's just 21, in base {x}!"
        else:
            x+=1

print(womens_age(32))
print(womens_age(39))

# Test.assert_equals(womens_age(32), "32? That's just 20, in base 16!")
# Test.assert_equals(womens_age(39), "39? That's just 21, in base 19!")
