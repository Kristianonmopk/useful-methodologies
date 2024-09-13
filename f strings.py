#f strings are strings that are formatted with an 'f' and they allow for variables/items not of the string data type to be placed into a string using curly brackets, without the need to convert them into a string

#Example:
age = 11
name = "Ojdoha"
introduction = f"Hello, my {name} is Josh and I am {age} years old."
print(introduction)

#Example 2:
true_or_false = True
print(f"The answer to the question is {true_or_false}")
