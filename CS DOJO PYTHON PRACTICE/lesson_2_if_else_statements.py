# lesson_2 How to use if else statements in python
#                          WHAT DID I LEARN?
# 1. setting up an "if clause"

#                           TO DO LIST
# 1. Learn how to select and replace one word in python. 
# 2. Learn how to clear python console. 




# print("hello 1")
# print("hello 2")


# print("Raindrops, drop tops (drop top)")
# print("Smokin' on cookie in the hotbox (cookie)")
# print("Touchin' on your chick she a thot, thot, thot (Thot)")
# print("Cookin' up dope in the crockpot, (pot)")
# print("We came from nothin' to somethin' ninja (hey)")
# print("I don't trust nobody, grip the trigger (nobody)")
# print("Call up the gang, they come and get you (gang)")
# print("Cry me a river, give you a tissue (hey)")
# print("My chick bad and boujee (bad)")
# print("Cookin' up dope with a Uzi (blaow)")
# print("My ninjas is savage, ruthless (savage)")
# print("We got 30's and 100 rounds too (grrah)")
# print("My chick bad and boujee (bad)")
# print("Cookin' up dope with a Uzi (dope)")
# print("My ninjas is savage, ruthless (hey)")
# print("We got 30's and 100 rounds too (glah)")


#                          SETTING UP AN IF CLAUSE
# I've established the variables of a and b and initialized them with the values of 1 and 2, respectively.
# a = 1 
# b = 2
# what if we want to print a message like " a is less than b" but ONLY IF the value of the variable a is actually less than the value of the variable b? 



# start with the word if then enter your variables
# I want to evaluate if A is LESS THAN B 
# if it is, I want to PRINT "a is less than b"
# if a < b:
# use colon to close your if statement
    # tab over for conventional printing
    # print("a is less than b ")
    # this is the end of the "if clause".
    # we can have multiple print lines within the if statement.
    # print("a is definitley less than b")
# this print statement is outside of the if clause
# print("Not sure if a is less than b ")
#                                      IF ELSE 
# c = 3 
# d = 4 
# if c < d: 
#     print("c is less than d")
# else:
#     print("c is not less than d")
#     print("I don't think c is less than d")
# print("outside of the if block")
#                   ELSE IF / ELIF 
# what if we wanted to dea with 3 cases?
# e = 20
# f = 8 
# if e < f:
#     print("e is less than f")
    # note that there is no colon at the end of the elif statement
    # also notice that the double equal sign == is used to check if one value is equal to another.  
# elif e == f: 
#     print("e is equal to f")
# we can have multiple elif statements to evaluate our first condition. The below equation will evaluate if the value is greater than f by 10. 
# elif e > f + 10: 
#     print("e is greater than f by more thn 10")
# else:
#     print("e is greater than f")


g = 7 
h = 8
if g < h:
    print("g is less than h")
else:
    if g == h: 
        print("g is equal to h")
    else:
        print("g is greater than h")

name = "Ike"
height_m = 2
weight_kg = 90

