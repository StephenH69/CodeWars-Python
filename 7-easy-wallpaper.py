# John wants to decorate a room with wallpaper. He's heard that 
# making sure he has the right amount of wallpaper is more complex 
# than it sounds. He wants a fool-proof method for getting it right.

# John knows that the rectangular room has a length of l meters, a
# width of w meters, a height of h meters. The standard width of 
# the rolls he wants to buy is 52 centimeters. The length of a roll 
# is 10 meters. He bears in mind however, that it’s best to have an 
# extra length of wallpaper handy in case of mistakes or miscalculations 
# so he wants to buy a length 15% greater than the one he needs.

# Last time he did these calculations he got a headache, so could 
# you help John? Your function wallpaper(l, w, h) should return as a 
# plain English word in lower case the number of rolls he must buy.

# Example:
# wallpaper(4.0, 3.5, 3.0) should return "ten"
# wallpaper(0.0, 3.5, 3.0) should return "zero"

# Notes:
# all rolls (even with incomplete width) are put edge to edge
# 0 <= l, w, h (floating numbers), it can happens that w x h x l is zero
# the integer r (number of rolls) will always be less or equal to 20
# FORTH: the number of rolls will be a positive or null integer 
# (not a plain English word; this number can be greater than 20)

import math

num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty'}


def wallpaper(l, w, h):
    #roll_cover = 5.2
    #total_cover = (((l * h)*2) + ((w * h)*2))
    #number_rolls = ((((l * h)*2) + ((w * h)*2))/5.2)*1.15
    if l == int(0) or w == int(0) or h ==(0):
        return "zero"
    else:
        return(num2words.get(math.ceil(((((l * h)*2) + ((w * h)*2))/5.2)*1.15))).lower()

print(num2words.get(15))
print(wallpaper(6.3, 4.5, 3.29))
print(wallpaper(7.8, 2.9, 3.29))
print(wallpaper(6.3, 5.8, 3.13))
print(wallpaper(6.1, 6.7, 2.81))
print(wallpaper(0, 4.5, 3.29))



# testing(wallpaper(6.3, 4.5, 3.29), "sixteen")
# testing(wallpaper(7.8, 2.9, 3.29), "sixteen")
# testing(wallpaper(6.3, 5.8, 3.13), "seventeen")
# testing(wallpaper(6.1, 6.7, 2.81), "sixteen")