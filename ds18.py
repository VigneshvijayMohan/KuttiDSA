def sqmatrix(no):
    for i in range(no+1, 0, -1):
        for k in range(1, i , 1):
            print(chr(64 + k), end=" ")
        print("")






number = int(input("What's the value of N: "))
sqmatrix(number)


#Incomplete