import io
import math
text = ""

def get_word_value(word):
    sum = 0
    for c in word:
        if ord(c) >= 65 and ord(c) <= 90:
            sum += ord(c) - 64
    return sum

def is_triangle(integer):
    value = int(math.sqrt(2*integer + 0.25))
    return value*value/2 + value/2 == integer

with io.open('p042_words.txt', 'r') as file:
    text = file.read()

total = 0
words = text.split(',')
for word in words:
    if is_triangle(get_word_value(word)):
        total += 1

print(total)