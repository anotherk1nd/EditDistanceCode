#Based on comment soln at https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python

import random
import string

def RSG(N):
    str = [] # only works with empty list for str and and empty string for str1
    str1 = ""
    for _ in range(N): # I don't understand difference between underscore and i but was in soln
        str.append(random.choice(string.ascii_lowercase))
        str1 = ''.join(str) # I think this can be implemented in 1 line
    #print str1
    return str1

#print RSG(5)
#print RSG(5)