words = ['apple', 'orange', 'banana', 'pear', 'grape', 'kiwi', 'pineapple']
words_longer_than_5 = []
for word in words:
    if len(word) > 5:
        words_longer_than_5.append(word)

print(words_longer_than_5) # ['orange', 'banana', 'pineapple']