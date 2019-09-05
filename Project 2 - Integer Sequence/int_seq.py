num = int(input("Enter an integer: "))
the_sum = 0
odd = 0
even = 0
largest = 0

while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

    if num >= largest:
        largest = num

    the_sum += num
    print("Cumulative total:", the_sum)
    num = int(input("Enter an integer: "))

print("Largest number:", largest)
print("Count of even numbers:", even)
print("Count of odd numbers:", odd)