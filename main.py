
#dev
try:

    while True:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if num1 == 7 or num2 ==7:
            print("Good bye!")
            break
        elif num1 > num2:
            print(f"{num1} - max, {num2} - min, {num1}+ {num2} = {int(num1+num2)}")
        elif num1 < num2:
            print(f"{num2} - max, {num1} - min, {num2}+ {num1} = {int(num2+num1)}")


except Exception as ex:
    print(ex)