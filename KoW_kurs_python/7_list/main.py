x = 1
y = "Abc"

list1 = [1,2,"c","d","f","e",]
print(list1)
print(list1[-5])
print(list1[0])
list1[-1] = 'None'
for item in list1:
    print(item)

text = "Hello World"
print(text[2])
print("--------------------")
print(list1 + [22,3,5])
print(list1 * 3)
list1.append(["g","h"])
print(list1)
print(list1[5][1])

print("---------------------")
list1.insert(1,"new item on index 1")
print(list1)
print("number of char: ", list1.count('c'))
print("Index of 'f': ",list1.index("f"))
list1.remove("f")
print(list1)
list2 = [1,2,34,25,53,45,-4,]
print(min(list2))
print(max(list2))
list2.sort()
print(list2)
list2.reverse()
print(list2)
list2.clear()
print(list2)