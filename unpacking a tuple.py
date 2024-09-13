#Create a function that takes a list of tuples containing two items each which are an x and y co-ordinate and if the coordinates that have matching x and y coordinates then they should be printed
def equal_coordinates(l):
  l_2 = []
  for i in l:
#As seen below, due to us knowing that the input of l will be 2 values, we assign one of each of these values to both x and y 
#By doing this we were able to then compare the two individual items of l and compute our logic afterwards depending on the result
    x,y = i
    if x == y:
      l_2.append(i)
  return l_2

