# Problem:
# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

import io
import math
text = ""

# Finds the sum of all of the character values (a = 1, b = 2, ...) for a given word
def get_word_value(word):
    sum = 0
    for c in word: # for each character in the word
        if ord(c) >= 65 and ord(c) <= 90: # if the character is a lower case letter
            sum += ord(c) - 64 # add the value of the character (a = 1, b = 2, ...) to the sum
    return sum

# Check if a given integer is of the form ½n(n+1)
def is_triangle(integer):
    value = int(math.sqrt(2*integer + 0.25)) # find the nearest value for n (rounded down)
    return value*value/2 + value/2 == integer # if ½n(n+1) = the input then the input is a triangle number

# Open the file
with io.open('p042_words.txt', 'r') as file:
    text = file.read()

total = 0
words = text.split(',')
# Count the number of triangle words in the file
for word in words:
    if is_triangle(get_word_value(word)):
        total += 1

print(total)