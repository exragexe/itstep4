
#dev

num1=int(input("Enter first num: "))
print(f"!{num1}=")

sum=1
for i in range(1,num1+1):
    if i == num1:
        print(i, end="")
    else:
        print(f"{i} * ", end="")
    sum*=i
print(f"= {sum}")

