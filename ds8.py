def sqmatrix(no):
    for i in range(no * 2 - 1, 0, -2):
        spaces = " " * ((no * 2 - 1 - i) // 2)
        stars = "*" * i
        print(spaces + stars + spaces)


number = int(input("Whats the value of N:  "))
sqmatrix(number)
