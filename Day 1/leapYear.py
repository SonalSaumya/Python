year  = int(input("Enter year"))

if year%4 == 0 :
    print("Leap year")
else:
    if year %400 == 0 :
        if year % 100:
            print("Leap year")
    else :
        print("Not leap year")

