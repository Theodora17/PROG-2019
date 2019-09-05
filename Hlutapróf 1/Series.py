first = int(input("First: "))
step = int(input("Step: "))

the_sum = 0

while the_sum < 100:
    print(first, end = " ")
    the_sum += first
    first += step

print()
print("Sum of series:", the_sum)