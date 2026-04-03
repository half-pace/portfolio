user = int(input("Enter a number: "))
choice = int(input("Enter the pattern number (1-4): "))

match choice:
    case 1:
        # pattern 1 - right triangle
        for i in range(1, user + 1): #rows
            for j in range(0, i): #columns
                if j < i:
                    print("*", end="")
            print() # for new line after each row

    case 2:
        # pattern 2 - inverted right triangle
        for i in range(user, 0, -1):
            for j in range(0, i):
                if j < i:
                    print("*", end="")
            print()

    case 3:
        # pattern 3 - square of n * n stars (n here is user var)
        for i in range(user):
            for j in range(user):
                print("*", end="")
            print()

    case 4:
        # pattern 4 - number pyramid
        for i in range(1, user + 1):
            for j in range(1, i + 1):
                # for k in range(user - i):
                #     print(" ", end="")
                print(j, end="")
            print()


