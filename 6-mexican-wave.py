# In this simple Kata your task is to create a function that turns 
# a string into a Mexican Wave. You will be passed a string and you 
# must return that string in an array where an uppercase letter is a 
# person standing up.

# 1.  The input string will always be lower case but maybe empty.
# 2.  If the character in the string is whitespace then pass over it 
# as if it was an empty seat.

# wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

def wave(str):
    StrLen = len(str)
    x = 0
    MexWave = []
    while x < StrLen:
        str = str.lower()
        StrList = list(str)
        if StrList[x] != " ":
            StrList[x] = StrList[x].upper()
            MexWave.append("".join(StrList))
        x += 1
    return MexWave

print(wave("codewars"))
print(wave("two words"))