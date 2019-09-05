#Algorithm
# The first number will be the maximum, because it's the only number
# We check if the second number is the same size or bigger, if so, that number becomes the biggest
# we continue like this until the user inputs a negative number

num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
max_int = 0

while num_int >= 0:
    if num_int >= max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))

print("The maximum is", max_int)    # Do not change this line