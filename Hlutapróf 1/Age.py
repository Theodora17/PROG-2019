age = int(input("Enter your age: "))

if age > 0 and age <= 34:
    print("Young")
elif age >= 35 and age <= 50:
    print("Mature")
elif age >= 51 and age <= 69:
    print("Middle-aged")
elif age >= 70:
    print("Old")
else:
    print("Invalid age")