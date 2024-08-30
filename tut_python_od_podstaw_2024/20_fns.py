def hello(name,age,last_name = None): # fn is a piece of code that does a specific task, it's like a verb in a sentence. This piece of code is reusable.
    print ('Cześć ' + name + '! You\'re ' + str(age)  + ' old!') # print text and variable to console, concatenate strings)

    if not None:
        print('Your last name is ' ,last_name)

def strip_and_uppercase(text): # fn with one argument
    return text.strip().upper() # return value from fn

hello('Michał',12) # call fn with  argument
hello('Agi',32) # call fn with argument
hello('John',23) # call fn with argument
hello(age=23,name='Me',last_name='Dump') # call fn with argument, keyword argument (kwarg) and default argument
hello('Me',23,'Dump') # call fn with  positional argument

print(strip_and_uppercase('  Michał  ')) # call fn with argument
print(strip_and_uppercase('  Agi  ')) # call fn with argument
print(strip_and_uppercase('  John  ')) # call fn with argument


print('-----------------')
countries_info ={}
countries_info['Poland'] = ('Warsaw', 38)
countries_info['Germany'] = ('Berlin', 83)
countries_info['France'] = ('Paris', 67)
countries_info['Spain'] = ('Madrid', 47)
countries_info['Italy'] = ('Rome', 60)

# country = 'Poland'
# print(f'Country: {country}')
# print('Capital:', countries_info[country][0])
# print('Population (mln):', countries_info[country][1])

# country = 'France'
# print(f'Country: {country}')
# print('Capital:', countries_info[country][0])
# print('Population :', countries_info[country][1], 'millions')


print('-----------------')
def print_country_info(country):
    print(f"Country: {country}")
    print('Capital:', countries_info[country][0])
    print('Population:', countries_info[country][1], 'millions') 

print_country_info('Poland')
print_country_info('France')
print_country_info('Germany')