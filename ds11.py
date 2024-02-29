def sqmatrix(no):
    for i in range(1, no+1, 1):
        first = "0"
        second = "1"
        
        if i % 2 == 0:
            print(first + second)
        if i == 1:
            print(second)
        else:
            print(second + first)
        


number = int(input("Whats the value of N:  "))
sqmatrix(number)