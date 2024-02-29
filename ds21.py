def sqmatrix(no):
    print("*" * no)
    for i in range(no-2):
        print("*" + " "*(no-2) + "*")
    print("*" * no)


number = int(input("Whats the value of N:  "))
sqmatrix(number)
