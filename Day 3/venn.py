f = input("Enter fruits : ")
v = input("Enter vegetables : ")
g = input("Enter grains : ")

fruit = set(x for x in f.split(","))
veg = set(x for x in v.split(","))
grains = set(x for x in g.split(","))

print(fruit)
print(veg)
print(grains)

common = (fruit.intersection(veg)).intersection(grains)
print("common : ",common)

sym = (fruit.symmetric_difference(veg)).symmetric_difference(grains)
print("Symmetric difference : ",sym)

unique = (fruit.difference(veg)).difference(grains)
print("Unique : ",unique)