
#dev
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
sum=0
for i in range(num1,num2+1):
    print(f"{sum}+{i} = ", end="")
    sum +=i
    print(f"{sum}")

print(f"{sum} = sum")
print(f"{int(sum/num2)} = ariph")
