
#dev
dovzh= int(input("Enter length of lines: "))
znak = str(input("Znak: "))
triger = str(input("horizontal - h, vertical - v: "))

for i in range(1,dovzh+1):
    if triger =="v":
      print(znak)
    elif triger =="h":
        print(znak, end="")
    else:
        raise Exception("Incorect choose of triger")
