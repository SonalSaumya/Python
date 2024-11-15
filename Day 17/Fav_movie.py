dict = {}

def add_movie():
    key = input("Enter movie : ")
    value = int(input("Enter Vote :"))
    dict[key] = value

def vote_movie():
    name= input("Enyer movie to vote : ")
    dict[name] = dict[name]+1

def remove_movie():
    name = input("Enter name to remove : ")
    del dict[name]

def display():
    print(dict)


def top_movie():
    max = 0
    max_movie = None
    for key in dict:
        if dict[key]>max:
            max=dict[key]
            max_movie=key
    print( max_movie)


print(add_movie())
print(add_movie())
print(add_movie())
print(add_movie())
print(add_movie())
print(display())

print(vote_movie())
print(display())
print(top_movie())

print(remove_movie())
print(display())


print(top_movie())
print(display())

