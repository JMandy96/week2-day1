# Exercise #1
# Cube Number Test... Print out all cubed numbers up to the total
# value 1000. Meaning that if the cubed number is over 1000 break the loop.

#starts off at 0
num = 0

#checks for if the number cubed is over 1000 or not.
while num ** 3 <= 1000:
    #sets a cubed variable to store what the number cubed is.
    cube = num ** 3
    #prints the cube variable.
    print(cube)
    #adds 1 to the count each loop.
    num += 1



# Exercise #2
# Get first prime numbers up to 100

# HINT::
# An else after an if runs if the if didn’t
# An else after a for runs if the for didn’t break

#count up from 1-100
for num in range(1, 101):
    #default the value to true:
    prime = True
    #next for loops to check if it is prime or not:
    for integer in range(2, num):
        #for each number the loop will check use modulo to check if the 
        # remainder is 0, if it is then the number is not prime and will be 
        # changed to false

        #this loop is done for each number in the range of 2 to the 
        # number i am checking -1:

        if num % integer == 0:
            prime = False

    if prime:
        print(num)



# Exercise 3
# Take in a users input for their age, if they are younger than 18 print kids,
# if they're 18 to 65 print adults, else print seniors

try:
    age = int(input("What is your age? "))

    if age < 18:
        print("Kids")
    elif age > 18 and age < 65:
        print("Adults")
    else:
        print("Seniors")
except:
    print("You must use a digit, not the word")
