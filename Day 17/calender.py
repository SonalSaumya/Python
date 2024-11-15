'''
#siddhi
days = int(input("Enter days :"))

wd = ['S','M','T','W','T','F','S']

for i in range(len(wd)):
    print(wd[i], end="\t")
print()

k=1
for i in range(days):
    for j in range(0,7):
        if k<=days:
            print(k, end="\t")
            k=k+1
    print()

'''




'''
def print_calendar():
    days_in_month =  int(input("Enter the no. of days in the month: "))
    start_day = int(input("Enter the starting day"))
    week_days = ["S","M","T","W","T","F","S"]
    print("   ".join(week_days))
    print("   "*start_day, end= "")
    for day in range(1, days_in_month +1):
        print(f"{day:>4}", end="")
        if(start_day + day)% 7 == 0:
            print()
    print()

print (print_calendar())
'''

