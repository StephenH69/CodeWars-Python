# You are given a function that should insert an asterisk(*) between every 
# pair of even digits in the given input, and return it as a string. 
# If the input is a sequence, concat the elements first as a string.
# Input
# The input can be an integer, a string of digits or a sequence containing integers only.
# Output
# Return a string.
# Examples
# 5312708 - -> "531270*8"
# "0000" - -> "0*0*0*0"
# [1, 4, 64] - -> "14*6*4"

def asterisc_it(n):
    ret = ''
    if isinstance(n, list):
        xlist = ''
        for i in range(len(n)):
            xlist += str(n[i])
    else:
        xlist = list(str(n))
    for i in range(len(xlist)):
        if i == len(xlist)-1:
            ret += xlist[i]
        elif (int(xlist[i]) % 2 == 0) and (int(xlist[i+1]) % 2 == 0):
            ret += xlist[i] + "*"
        else:
            ret += xlist[i]
    return ret

print(asterisc_it(5312708))
print(asterisc_it(9682135))
print(asterisc_it([1, 4, 64, 68, 67, 23, 1]))

# test.assert_equals(asterisc_it(5312708), '531270*8')
# test.assert_equals(asterisc_it(9682135), '96*8*2135')
# test.assert_equals(asterisc_it(2222), '2*2*2*2')
# test.assert_equals(asterisc_it(1111), '1111')
# test.assert_equals(asterisc_it(9999), '9999')
# test.assert_equals(asterisc_it('0000'), '0*0*0*0')
# test.assert_equals(asterisc_it([1, 4, 64, 68, 67, 23, 1]), '14*6*4*6*8*67231')