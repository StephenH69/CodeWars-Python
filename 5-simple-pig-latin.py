# Move the first letter of each word to the end of it, 
# then add "ay" to the end of the word. 
# Leave punctuation marks untouched.
import string

def pig_it(text):
    solution = ""
    split_text = text.split()
    for x in split_text:
        if x in string.punctuation:
            solution += x + " "
        else:        
            y = list(x)
            z = y[0] 
            del y[0]
            y.append(z)
            y.append("ay ")
            for i in y:
                solution += str(i) 
    return solution.strip()

print(pig_it('Pig latin is cool')) # igPay atinlay siay oolcay
print(pig_it('Hello world !'))     # elloHay orldway !

input_string = str(input("Please enter the phrase you want to convert:"))
print(pig_it(input_string))


def pig_it2(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

word = "Stephen"
print([word[1:] + word[:1]])