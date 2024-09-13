#Here by using the break method, it makes it so that while the loop is less than 10 it will add on 1 to the number however if the number is ever to reach 6, then the loop will break
i = 0
while i < 10:
  print(i)
  if i == 6:
    break
  i += 1

print()
#Here this loop does the same as the previous one however by using the break method after i += 1, it makes it so that once 5 is printed and 1 is added to it, it will then reach the break statement before reaching the print statement, only allowing for 5 and below to be printed onto the screen and not 6.
i = 0
while i < 10:
  print(i)
  i += 1
  if i == 6:
     break

print()

#Here this loop it makes it so that while the number is less than 10 it will add on 1 to it and the if statement makes it so that if a number is even the number as well as text will be printed however the continue method makes it so that if a number is even it will skip the process that comes after it in the loop which is printing it onto the screen so the even numbers are not printed twice
i = 0
while i < 10:
  i += 1
  if i % 2 == 0:
    print(str(i) + ".", "This is an even number")
    continue
  print(i)

print()
i = 0
while i < 10:
  i += 1
  if i % 2 == 0:
    continue
  print(i)
  print('hello')
