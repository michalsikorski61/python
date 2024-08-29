name = "Michal" # string created with single quotes
name = 'Michal' # string created with double quotes
name = """Michal""" # string created with triple quotes, this is for multiline strings
channel_name = 'Jak nauczyć się programowania' # string with single quotes
channel_name = "Jak nauczyć się programowania - dłuższy tekst ujmujemy w podwójne cudzysłowie" # string with double quotes
name = 'Michal with \' apostrof' # SyntaxError: invalid syntax if we use single quotes without escape character
name = "Michal with ' apostrof" # string with double quotes and single quotes inside

print(name)

long_text = """To jest          długi tekst
w wielu


liniach"""
print(long_text)

# f-string
name = "Michal"
age = 30
text = f"Hello {name}, you are {age} years old."
print(text)