text = input("Enter text: ") # get input from user
words = text.split() # split text into words
words_count = {} # empty dictionary
for word in words: # iterate over words
    if word in words_count: # if word is in dictionary
        words_count[word] += 1 # increment word count
    else: # if word is not in dictionary
        words_count[word] = 1 # add word to dictionary
print(words_count) # print dictionary to console

# another way to count words
from collections import Counter

words_count = Counter(words)
print(words_count) # print dictionary to console
# Compare this snippet from GITHUB_POWERED/PYTHON/tut_python_od_podstaw_2024/19_3_exercise.py: