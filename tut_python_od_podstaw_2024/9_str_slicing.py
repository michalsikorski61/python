text = 'Programuj od podstaw'
print(text[0]) # P - strings start from 0 index
print(text[1]) # r
print(text[2]) # o
print(text[3]) # g

print(text[-1]) # w - last character
print(text[0:3]) # Pro - slicing, start from 0 index, end at 3 index (not included)
print(text[0:9:2]) # Po - slicing, start from 0 index, end at 9 index (not included), step 2
print(text[:9]) # Programuj - slicing, start from beginning, end at 9 index (not included)
print(text[9:]) # od podstaw - slicing, start from 9 index, end at the end
print(text[::2]) # Pormj dpdta - slicing, start from beginning, end at the end, step 2
print(text[::-1]) # watsdop do jumorP - slicing, start from the end, end at the beginning, step -1
print(text[::-2]) # wsdpo jmo - slicing, start from the end, end at the beginning, step -2
print(text[3:0:-1]) # gor - slicing, start from 3 index, end at 0 index (not included), step -1

#length of string
print(len(text)) # 20 - length of string

