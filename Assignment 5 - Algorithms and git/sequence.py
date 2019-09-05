#Algorithm
# the sequence takes the last 3 numbers and adds them together to make a new integer
# 1, 2 and 3 don't fit the rule, so we assume they are the beginning of the sequence

n = int(input("Enter the length of the sequence: ")) # Do not change this line

counter = 1

total = 0
first = 0
second = 0
third = 1

while counter <= n:
    total = first + second + third
    print(total)

    first = second
    second = third
    third = total

    if first == 1 and second == 1:
        first = 0

    counter += 1