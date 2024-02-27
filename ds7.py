def sqmatrix(no):
    for i in range(1, no * 2, 2):
        spaces = " " * ((no * 2 - 1 - i) // 2)
        stars = "*" * i
        print(spaces + stars + spaces)


number = int(input("Whats the value of N:  "))
sqmatrix(number)
