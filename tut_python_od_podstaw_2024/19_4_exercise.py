# two names list with duplicates
names = ['John', 'Paul', 'George', 'Ringo', 'Eric', 'Paul']
names1 = ['John', 'Agi', 'George', 'Rachel', 'Eric', 'Mike']

for name in names:
    if name in names1:
        print(name)

