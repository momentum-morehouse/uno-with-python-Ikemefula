# python for absolute beginners #1 - What are variables?
# print("Hello World")
# print('more string')
# print(3)

# i have established a variable. The convention is to have your 
# a = 1
# in order to check what is in tha variable, I want to print it out in the python console. 
# print(a)

# b = 2 
# print(b)

# print(a, b)

# c = "hello there"
# print(a, b, c)

# re-assigning variables 
# a = "People say I drive too fast, move too fast, live too fast"
# b = "Ain't no such thing as too fast for me" 
# c = "People say I drive too fast, move too fast, live too fast"
# d = "Ain't no such thing as too fast for me"

# print(a,b,c,d)

# a = 1 
# c = "Hello World"

# f = a 
# a = 2

# g = c 

# print(a)
# print(c)
# print(f)


# Swapping two variables.
# This is  how i chose to swap my variables. 
# v1 = "first string"
# v2 = "second string"

# v1 = v2

# v2 = "first string"
# print(v1, v2)

# This is the method he used instead. He utilized temp variables. 
# v1 = "first string"
# v2 = "second string"

# temp1 = v1
# temp2 = v2

# v1 = temp2
# v2 = temp1
# print(v1)
# print(v2)

# what if i only wanted to use 1 temp variable to swap  the variable values? 

v1 = "first string"
v2 = "second string"

temp = v1
v1 = v2
v2 = temp
print(v1)
print(v2)

#                                  WHAT DID YOU LEARN?