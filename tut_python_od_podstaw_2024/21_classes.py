#  usr
#  name 
#  mail
#  age

user = ('Kamil', 'kamil@programuj.pl')

class User:# class is a blueprint for creating objects
    def __init__(self, name, mail, age): # constructor is a method that initializes an object
        self.name = name
        self.mail = mail
        self.age = age


    def print_info(self): # method is a function that belongs to an object
        print(self.name)
        print(self.mail)
        print(self.age)


    def is_male(self):
        return self.name.endswith('a') != True # return statement returns a value from a function
        # self.name[-1:] != 'a' # return statement returns a value from a function
# user = User() # object is an instance of a class
# user.name = 'Kamil'
# user.mail = 'kamil@programuj.pl'
# user.age = 30

# user.print_info()

# user1 = User()
# user1.name = 'Michal'
# user1.mail = 'michal@100ppro.net'
# user1.age = 29

# user1.print_info()

user0 = User('Kamil','kamil@example.com', 30)
user0.print_info()
print(user0.is_male())

user1 = User('Michal','michal@example.com', 29)
user1.print_info()
print(user1.is_male())