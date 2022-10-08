
#dev
try:
    odd = []
    even = []
    list9 = []
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            even.append(i)
        elif i % 3 == 0:
            odd.append(i)
        elif i % 9 == 0:
            list9.append(i)
    print(f"Кратні 2: {even} \n AVG:{int(sum(even)/len(even))}")
    print(f"Кратні 3: {odd} \n AVG:{int(sum(odd)/len(odd))}")
    print(f"Кратні 9: {list9} \n AVG:{int(sum(list9)/len(list9))}")

except Exception as ex:
    print(ex)

