# this would be a example test app to try out how to do nlp for basic stuff  like interpreting numbers from text and then using a little if else statement tree to make a simple AI calculator.

# firstly the thing I have to do is 
# [*] writing text forms of numbers for 0 to 9 
# [*] then interpreting these numbers into their number form 
# and priting them out.
# [] work with the prefix evalute method so that you could include arthematic with brackets.


from prefix import *
from constants import *

request = input("Enter a word for a single digit number : ").lower()

tokenList = request.split()

exp = []

temp = 0;

for token in tokenList :
    

    if token in singleDigits:
        singleint = singleDigits[token]
        print("Found the digit : " + str(singleint))
        # if temp and singleint:
        temp = temp + singleint
        exp.append(str(temp))
        temp = 0

    if token in operators : 
        print("Found the digit : " + str(operators[token]))
        exp.append(str(operators[token]))

    if token in multipliers :
        print("Found the digit : " + str(multipliers[token]))
        temp = multipliers[token]


print(exp)
if len(exp) > 0:
    print(evalute(exp))

'''
what we want => 1+2) * 7
what we can already do *7+12
what we get with our current implementation => +12*7
but this will calculate to errors

+12)*7


'''