
#dev
try:


    while True:
        num1 = int(input("Enter number: "))

        if num1 == 7:
            print("Good bye!")
            break


        elif num1 > 0:
            print("Number is positive")
        elif num1 < 0:
            print("Number is negative")
        elif num1 == 0:
            print("Number is equal to zero")


except Exception as ex:
    print(ex)