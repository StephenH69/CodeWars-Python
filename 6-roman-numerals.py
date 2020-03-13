# Roman Numerals Encoder
# Create a function taking a positive integer as its parameter and 
# returning a string containing the Roman Numeral representation of that integer.

# Modern Roman numerals are written by expressing each digit separately 
# starting with the left most digit and skipping any digit with a value of zero. 
# In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
# 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in 
# descending order: MDCLXVI.

# Example:
# solution(1000) # should return 'M'
# Help:
# Symbol    Value
# I          1
# IV         4
# V          5
# IX         9
# X          10
# XL         40
# L          50
# XC         90
# C          100
# CD         400
# D          500
# CM         900
# M          1,000
# Remember that there can't be more than 3 identical symbols in a row.

# More about roman numerals - http://en.wikipedia.org/wiki/Roman_numerals
import time

def solution(n):
    # TODO convert int to roman string
    solution = ""
    remainder = n

    while remainder > 0:
        if remainder > 999:
            solution = solution + "M"
            remainder -= 1000
        elif remainder > 899:
            solution = solution + "CM"
            remainder -= 900           
        elif remainder > 499:
            solution = solution + "D"
            remainder -= 500            
        elif remainder > 399:
            solution = solution + "CD"
            remainder -= 400 
        elif remainder > 99:
            solution = solution + "C"
            remainder -= 100 
        elif remainder > 89:
            solution = solution + "XC"
            remainder -= 90    
        elif remainder > 49:
            solution = solution + "L"
            remainder -= 50    
        elif remainder > 39:
            solution = solution + "XL"
            remainder -= 40      
        elif remainder > 9:
            solution = solution + "X"
            remainder -= 10 
        elif remainder > 8:
            solution = solution + "IX"
            remainder -= 9 
        elif remainder > 4:
            solution = solution + "V"
            remainder -= 5
        elif remainder > 3:
            solution = solution + "IV"
            remainder -= 4
        elif remainder > 0:
            solution = solution + "I"
            remainder -= 1 
    return(solution)


start_time = time.time()
print(solution(7))
print(solution(81))
print(solution(249))
print(solution(816))
print(solution(1066))
print(solution(1820))
print(solution(1969))
print(solution(2020))
print(solution(2199))
print(solution(3642))
print("Time taken: ", time.time() - start_time)


def solution2(n):
    roman_numerals = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    roman_string = ''
    for key in sorted(roman_numerals.keys(),reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string




start_time = time.time()
print(solution2(7))
print(solution2(81))
print(solution2(249))
print(solution2(816))
print(solution2(1066))
print(solution2(1820))
print(solution2(1969))
print(solution2(2020))
print(solution2(2199))
print(solution2(3642))
print("Time taken: ", time.time() - start_time)
