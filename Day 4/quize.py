
'''
#siddhi
dict = {'abc':'efg', 'hij':'klm', 'nop':'qrs', 'tuv':'wxy'}
attempt = 0

while True:
    play = input("Do you want to play :")
    if play == "yes":
        for i in dict:
            print("country : ", i)
            guess = input("Enter capital :")
            if guess == dict[i]:
                print("Won")
            else:
                print("Wrong answer !")
                attempt = attempt+1
                print("Attempts : ",attempt)

    if play =="no":
        break

'''

dict = {'a':'b', 'c':'d', 'e':'f'}
attempt= 0
while True:

    game = input("Do you want to play the game: ")
    if game == "yes":

        for i in dict:
            print("Country: ", i)
            guess = input("Enter Capital: ")
            if guess==dict[i]:
                print("You Won!!!")
            else:
                print("Try Again!: ")
                attempt =attempt+1
    print("No of attempts: ",attempt)
