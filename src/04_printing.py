"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,*************
# y, and z: 
# x is 10, y is 2.25, z is "I like turtles!"

print("my fav number is %s"%(x))
print("my least fav number is %s"%(y))
print("sometimes i think to myself, %s"%(z))

# Use the 'format' string method to print the same thing
print("I think i numbers that work well with, {}!".format(x))
print("The number, {} is of decimal type.".format(y))
print("{}".format(z))

# Finally, print the same thing using an f-string
print(f"{x}, how are ya?")
print(f"{y}")
print(f"{z}")
