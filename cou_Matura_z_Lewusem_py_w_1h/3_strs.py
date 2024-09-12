name = 'Michał'
print(name[1])

print('-----------------')
for letter in name:
    print(letter,end=' | ')


print('\n-----------------')
if 'm' in name:
    print('letter m is in name')

print('-----------------')
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.swapcase())
print(f'Length of name: {len(name)}')
name = name.upper()
name = name.lower().replace('chał','chałek')
print(name)

print('-----------------')
test_str = 'ala ma kota '
test_str = test_str.replace(' ','_')
print(test_str)
array_test_str = test_str.split('_')
print(array_test_str)
print(test_str.endswith('kota'))
print(test_str.startswith('ala'))

new_str = test_str + 'i psa'
print(new_str)

new_str = new_str.replace('i',' i')
print(new_str)
new_str2 = f'this a new string with var {name}, we\'re using f-string'
print(new_str2)
print(new_str2.find('new')) # returns index of first occurence
print(new_str2.find('old')) # returns -1 if not found
print(new_str2.index('new')) # returns index of first occurence
print(new_str2[-1]) # returns last character
print(new_str2[-2]) # returns second last character
print(new_str2[-3]) # returns third last character
print(new_str2[2:5]) # returns characters from index 2 to 5
print(new_str2[2:]) # returns characters from index 2 to end
print(new_str2[:5]) # returns characters from start to index 5
print(new_str2[:-5]) # returns characters from start to fifth last
print(new_str2[2:5:2]) # returns characters from index 2 to 5 with step 2