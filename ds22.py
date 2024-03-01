def sqmatrix(no):
    print(f"{no}" * ((2 * no) - 1))
    for i in range((2 * no) - 1):
        print(f"{no}" + f"{no-1}" * ((2 * no) - 3) + f"{no}")
    print(f"{no}" * ((2 * no) - 1))


number = int(input("Whats the value of N:  "))
sqmatrix(number)
