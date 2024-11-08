

while input("do you want to continue : ") == "yes":
    value = float(input("Enter value : "))
    unit = input("Enter unit : ")
    convert = input("Enter unit for conversion : ")

    if convert == "feet":
        ans = value * 0.0833333
        break

    elif convert == "meters":
        ans = value * 0.0254
        break

    elif convert == "centimeters":
        ans = value * 2.54
        break

print("after conversion ")
print(ans , convert)



