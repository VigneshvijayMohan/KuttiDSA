def sqmatrix(no):
    for i in range(no, 0, -1): 
        for j in range(i, no + 1, 1): 
            print(chr(ord('A') + j - 1), end = " "); 

        print("");





number = int(input("What's the value of N: "))
sqmatrix(number)


#Incomplete