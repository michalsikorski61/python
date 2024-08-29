# method is a function that belongs to an object
# string is an object
# object is an instance of a class
# class is a blueprint for creating objects

# string methods
channel_name = "Jak nauczyć się programowania"
print(channel_name.upper()) # JAK NAUCZYĆ SIĘ PROGRAMOWANIA
print(channel_name.lower()) # jak nauczyć się programowania
print(channel_name.title()) # Jak Nauczyć Się Programowania
print(channel_name.capitalize()) # Jak nauczyć się programowania
print(channel_name.count("a")) # 5
print(channel_name.count(" ")) # 3
print(channel_name.startswith("Jak")) # True
print(channel_name.startswith("jak")) # False
print(channel_name.endswith("programowania")) # True
print(channel_name.endswith("programowani")) # False
print(channel_name.find("nauczyć")) # 4 - index of the first occurrence
print(channel_name.find("nauczyć", 5)) # -1 - index of the first occurrence after index 5
print(channel_name.find("nauczyć", 5, 10)) # -1 - index of the first occurrence between index 5 and 10
print(channel_name.find("nauczyć", 5, 11)) # 4 - index of the first occurrence between index 5 and 11
print(channel_name.rfind("a")) # 29 - index of the last occurrence
print(channel_name.index("nauczyć")) # 4 - index of the first occurrence
# print(channel_name.index("nauczyć", 5)) # ValueError: substring not found - index of the first occurrence after index 5 because it does not exist in the string after index 5 it exists before index 5
print(channel_name.replace('programowania', 'jazdy na nartach')) # Jak nauczyć się jazdy na nartach
print(channel_name.replace(' ', '_')) # Jak_nauczyć_się_programowania
print(channel_name.split()) # ['Jak', 'nauczyć', 'się', 'programowania']
