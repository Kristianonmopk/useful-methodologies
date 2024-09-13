#List comprehension is essentially a way of iterating through a list's value and applying a function to each value.
#This works essentially the same as a for loop when iterating through a list to use or alter its values however, it allows us to do this in a single line of code.
#The syntax for list comprehension is: new_list = [expression FOR item IN list IF condition]
#An example of this would be: based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
#Below is an example of doing this with a for loop:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#However, if we did this with list comprehension, it would look like this:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
#Below is another example of list comprehension if we wanted to double the numbers in a list and assign those doubled numbers to another list:
numbers = [1, 2, 3, 4, 5]
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers)

input()

#Let's use if...else with list comprehension to find even and odd numbers:

numbers = [1, 2, 3, 4, 5, 6]
# find even and odd numbers
even_odd_list = ["Even" if i % 2 == 0 else "Odd" for i in numbers]
print(even_odd_list)

input()

#Let's use nested if with list comprehension to find even numbers that are divisible by 5:
# find even numbers that are divisible by 5
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)
#Here, list comprehension checks two conditions:
#if y is divisible by 2 or not.
#if yes, is y divisible by 5 or not.
#If y satisfies both conditions, the number appends to num_list.

input()

#Below is list comprehension that is used to find the square of all even numbers from 1 to 50
# List Comprehension
l = [i ** 0.5 for i in range(1, 50) if i % 2 == 0]
print(l)
#i -> Variable
#i  ** 0.5 -> Input Sequence (Optional)
#range(1, 50) -> Output Expression
#if i % 2 == 0 -> Conditional Statement (Optional)

input()

#Below is an example of nested list comprehension that is used to find the cube of all even numbers from 1 to 50
nested_list = [[1,2,3], [4,5,6], [7,8,9]]
flat_list = [num for num in nested_list for num in num]
print(flat_list)

input()

#Any and All methods are useful in checking if every element in the list if they All or Any of the elements in the list satisfy the conditions.

#Any method returns True if any element in the list satisfies the condition.
#All method returns True if all elements in the list satisfy the condition.
#Below is an example of using the any method to check if any element in the list is greater than 10:
numbers = [1, 2, 3, 4, 5, 6]
any_greater_than_10 = any(num > 10 for num in numbers)
print(any_greater_than_10)
#Below is an example of using the all method to check if all elements in the list are greater than 10:
numbers = [1, 2, 3, 4, 5, 6]
all_greater_than_10 = all(num > 10 for num in numbers)
print(all_greater_than_10)

#Below is an example of using the any method to create a function that checks that if an entered email contains any invalid letters.
def has_invalid_characters(string):
  valid = "abcdefghijklmnopqrstuvwxyz0123456789."
  return any(i not in valid for i in string)

#Importantly to add, whilst the map() function can be used alternatively to list comprehension, the syntax for list comprehension is mostly much better and more readable/simplified. However, it is up to preference.
