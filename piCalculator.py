reset="y"
while reset in ("y","Y"):
    pi=float(0)
    b=int(1)
    n=0
    counter=int(1)
    check="y"
    print("Welcome to the LB Pi Iterator! \n\n Firstly you can define the NUMBER of iterations you wish, \n\nif you define the value as 0 the calculation will run indefinitly!")
    it=int(input())
    if it > 0:
        print("do you want to see the iteration progress? (type \"y\" or \"Y\" for yes)")
        mode=str(input())
        if mode in ("y", "Y"):
            print("ITERATION         PI VALUE")
            while counter<=it:
                pi=float(pi+(1/b))
                print(n, " ", '%.50f' % (pi*4))
                n+=1
                b=b+2
                counter+=1
                pi=float(pi-(1/b))
                print(n, " ", '%.50f' % (pi*4))
                n+=1
                b=b+2
                counter+=1
            print("Do you want to try again?(type \"y\" or \"Y\" to restart or anything else to close!)")
            reset=str(input())
            if reset in ("y","Y"):
                continue
            else:
                print("The program is closing...")
            break
        
        else:
            while counter<=it:
                pi=float(pi+(1/b))
                b=b+2
                n+=1
                counter+=1
                pi=float(pi-(1/b))
                b=b+2
                n+=1
                counter+=1
            print("pi value is ", '%.50f' % (pi*4), " after ", n, " iterations")
            print("Do you want to try again?(type \"y\" or \"Y\" to restart or anything else to close!)")
            reset=str(input())
            if reset in ("y","Y"):
                continue
            else:
                print("The program is closing...")
                break


    elif it == 0:
        print("Do you want the program to PAUSE in a given range of iterations? \n\n(type \"y\" or \"Y\" for yes or anything else for no!)")
        pause=str(input())
        if pause in ("y","Y"):
            print("Please define the range NUMBER of iterarions that you wish to pause:")
            itrange=int(input())
            while itrange<=0:
                print("the range should be above 0, please input a positive interger:")
                itrange=int(input())
                
            print("ITERATION         PI VALUE")
            while pause in ("y", "Y"):
                while counter<=itrange:
                    pi=float(pi+(1/b))
                    print(n, " ", '%.50f' % (pi*4))
                    n+=1
                    b=b+2
                    counter+=1
                    pi=float(pi-(1/b))
                    print(n, " ", '%.50f' % (pi*4))
                    n+=1
                    b=b+2
                    counter+=1
                print("Do you want to CONTINUE the iteration? \n\n(type \"y\" or \"Y\" for yes or anything else for no!")
                pause=str(input())
                counter=1
            print("You stopped the iteration")                

        else:
            print("This will cause the program to run indefintly, are you sure you want to proceed? \n\n(type \"y\" or \"Y\" for yes or anything else for no!")
            check=str(input())
            if check not in ("y", "Y"):
                print("The program is restarting...")
                continue
            print("ITERATION         PI VALUE")
            while counter>it:
                pi=float(pi+(1/b))
                print(n, " ", '%.50f' % (pi*4))
                b=b+2
                n+=1
                pi=float(pi-(1/b))
                print(n, " ", '%.50f' % (pi*4))
                b=b+2
                n+=1
    else:
        print("the value must be numerical or above 0")
        print("Do you want to try again?(type \"y\" or \"Y\" to restart or anything else to close!)")
        reset=str(input())
        if reset in ("y","Y"):
            continue
        else:
            print("The program is closing...")
            break
        
