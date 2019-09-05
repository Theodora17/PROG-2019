num = 10

while num <= 99:
    AB = num
    squared = (AB)** 2
    s_AB = squared % 100
    if s_AB == AB and squared < 1000:
        print(AB)

    num += 1