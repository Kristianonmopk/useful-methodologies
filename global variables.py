#As we already know, different variables have different scopes depending on where they are defined. 
#For example, if we define a variable inside a function, it is only available inside that function and these types of variables are known as local variables
#However, if we define a variable outside o a function, it is available globally and these types of variables are known as global variables
#However, if we wish to sue a global variable inside of a function, we can only do so by putting the keyword 'global' before the variable name inside the function 

#For example, in the example below we defined the global variable 'enemies' and we then try to access that same variable inside of the function 'increase_enemies' by adding 1 to it.
#However, as we did not define the global variable 'enemies' inside of the function, the function 'increase enemies' believes that we are trying to access a variable that does not exist and therefore it throws an error.

enemies = 1
def increase_enemies():
  enemies += 1
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies inside function: {enemies}")

#Alternatively, if we tried to to re-define the variable 'enemies' inside of the function , the function 'enemies' would believe that we are trying to create a new variable inside the function and therefore it would create a new variable with the name 'enemies' and assign it a value of 2.1.

enemies = 1
def increase_enemies():
  enemies = 3
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside the function: {enemies}")
#Summartively however, if we wished to use the global variable 'enemies' inside of the function, we can do so by adding the keyword 'global' before the variable name inside the function like below

enemies = 1
def increase_enemies():
  global enemies
  enemies += 1 
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies inside function: {enemies}")
