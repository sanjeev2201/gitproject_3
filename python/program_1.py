def Prime_Number():
    count = 0
    for i in range(25, 101):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            count += 1
            print(count, "-->", i)


Prime_Number()
