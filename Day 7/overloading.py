class Calc:

    def sum(self,*args):
        return sum(args)


c1 = Calc()

print(c1.sum(1,2))
print(c1.sum(1,2,3))