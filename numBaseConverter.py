mode = 0          #Sets the program mode

chk = 0           #Will keep the program running until it's closed

while chk == 0:   #will keep the program running

    mode = input("\n\n      Welcome to Modest Numerical Base Converter in Python 3.0! \n Developed by DLB. \n\n Choose \"d\" to convert a decimal number; \n\n Choose \"b\" to convert a binary number; \n\n Choose \"h\" to convert an hexadecimal number; \n\n Choose \"o\" to convert an octal number; \n\n Choose \"c\" to convert a custom base number; \n\n Choose \"x\" to close the program: \n\n")

    if mode in ["d", "D"]:  #decimal converter to other bases

        print("\n\n You chose DECIMAL converter mode!\n")

        d = input("Input a decimal value: \n")

        while True: #will check if the value is decimal and keep the program running on a wrong input

            try:

                d = int(d)

                break

            except:

                d = input("Please, input a valid decimal value: \n")

                continue   

        print("binary: ", bin(d))

        print("hexadecimal: ", hex(d))

        print("octal: ", oct(d))

        mode = input("\n Run again? (type \"x\" for no): \n")


    if mode in ["b", "B"]: #binary converter to other bases

        print("You chose BINARY converter mode! \n")

        b = input("Input an binary value: \n")

        while True: #checks if the value is binary and keeps the program running on a wrong input

            try:

                b = int(b, 2)

                break

            except:

                b = input("please input a valid binary number of 0s and 1s: \n")

                continue

        print("decimal: ", int(b))

        print("octal: ", oct(b))

        print("hexadecimal: ", hex(b))

        mode = input("\n Run again? (type \"x\" for no): \n")


    if mode in ["h", "H"]: #hexadecimal converter to other bases

        print("You chose HEXADECIMAL converter mode! \n")

        h = input("Input an hexadecimal value: \n")

        while True: #checks if the value is heaxdecimal and keeps the program running on wrong input

            try:

                h = int(h, 16)

                break

            except:

                h = input("Please input an hexadecimal value with digits between 0 and 9 and \"a\" and \"f\": \n")

                continue

        print("decimal: ", int(h))

        print("binary: ", bin(h))

        print("octal: ", oct(h))

        mode = input("\n Run again? (type \"x\" for no): \n")


    if mode in ["o", "O"]: #octal converter to other bases

        print("You chose OCTAL converter mode! \n")

        o = input("Input an octal value: \n")

        while True: #checks if the value is octal and keeps the program running on a wrong input

            try:

                o = int(o, 8)

                break

            except:

                o = input("Please input an octal value with digits between 0 and 8: \n")

                continue

        print("decimal: ", int(o))

        print("binary: ", bin(o))

        print("hexadecimal: ", hex(o))

        mode = input("\n Run again? (type \"x\" for no): \n")


    if mode in ["c", "C"]: #custom base converter to other bases

        print("you chose CUSTOM BASE converter mode! \n")

        c = input("Input the value to convert: \n")

        base = (input("Input the base in which the value is (Min 2/Máx 36): \n"))

        while True: #checks if the base is an interger and keeps the program running if its not

            try:

                base = int(base)

            except:

                base = input("Please input a valid base value (A decimal between 2 and 36): \n")

            else:

                if base >=2 and base <= 36:

                    break

                else:

                    base = input("Please input a valid base value (A decimal between 2 and 36): \n")

        while True:

            try:

                c = int(c, base) #will force a value thats accepted in the defined base

                break

            except:

                print("\n The value to convert is not in base ", base, "!\n\n")

                c = input("Please input a value with all digits below the base value: \n")

                continue

        print("decimal: ", int(c))

        print("octal: ", oct(c))

        print("hexadecimal: ", hex(c))

        print("binary: ", bin(c))

        mode = input("\n Run again? (type \"x\" for no): \n")

    

    if mode in ["x", "X"]: #closes program and shows credits

        print("\n\n Thank you for using Modest Numerical Base Converter in Python 3.0! \n Developed by DLB. \n The program is closing!\n\n")

        break


    else: #ask for a valid mode option

        print ("Please input a valid option!")