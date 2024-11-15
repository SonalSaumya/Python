a = int(input("Enter forst number : "))
b = int(input("Enter second number : "))

try:
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Can not divide by zero")
finally:
    print("inally executed")
