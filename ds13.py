def sqmatrix(no):
    num = 1
    for i in range(1, no+1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()
        


number = int(input("Whats the value of N:  "))
sqmatrix(number)

