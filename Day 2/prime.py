n = int(input("Enter number : "))
prime = []

for j in range (2,n+1):
    if j==2 :
        prime.append(2)
    else :
        for i in range(2, j + 1):
            if (j % i == 0):
                break


            else:
                prime.append(j)
                break


print(prime)





##What about 2 ? done
