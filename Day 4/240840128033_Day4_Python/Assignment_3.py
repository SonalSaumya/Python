nums = []

for i in range(1,21):
    nums.append(i)

#print(nums)

#new_nums = ["fizz" if i%3==0 else "Buzz" if i%5==0 else "FizzBuzz" if (i%3==0 and i%5==0) else i for i in nums]
new_nums = ["FizzBuzz" if (i%3==0 and i%5==0) else "Fizz" if i%3==0 else "Buzz" if i%5==0 else i for i in nums]
print(new_nums)