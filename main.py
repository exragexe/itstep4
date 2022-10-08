
#dev
try:
    num1=int(input("Enter length of lines: "))
    znak = str(input("Znak: "))
    for i in range(1,num1+1):
        print(znak, end="")
except Exception as ex:
    print("not correct num1 or znak")