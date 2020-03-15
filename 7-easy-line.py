# In the drawing below we have a part of the Pascal's triangle, 
# lines are numbered from zero (top).

# We want to calculate the sum of the squares of the binomial coefficients 
# on a given line with a function called easyline (or easyLine or easy-line).

# Can you write a program which calculate easyline(n) where n is the line number?

# The function will take n (with: n>= 0) as parameter and will return the sum 
# of the squares of the binomial coefficients on line n.

# ##Examples:

# easyline(0) => 1
# easyline(1) => 2
# easyline(4) => 70
# easyline(50) => 100891344545564193334812497256

def easyline(n):
    for i in range(n+1):
        if i == 0: lineList = [1]
        elif i == 1: lineList = [[1],[1,1]]
        else:
            newList = []
            newList.append(1)
            j = 0
            while j < (len(lineList[i-1]))-1:
                newList.append(lineList[i-1][j] + lineList[i-1][j+1])
                j += 1       
            newList.append(1)
            lineList.append(newList)
    returnTotal = 0
    for k in lineList[n]: returnTotal += (k * k)
    return returnTotal



print(easyline(7))
print(easyline(13))
print(easyline(17))
print(easyline(19))





# testing(easyline(7), 3432)
# testing(easyline(13), 10400600)
# testing(easyline(17), 2333606220)
# testing(easyline(19), 35345263800)