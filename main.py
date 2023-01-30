# FizzBuzz

# Version 1
group = []
number = ""
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        number = "FizzBuzz"
    elif i % 3 == 0:
        number = "Fizz"
    elif i % 5 == 0:
        number = "Buzz"
    else:
        number = str(i)
    group.append(number)
print("Version 1:", group)

# Version 2
print("Version 2:", list(map(lambda i: "Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i), range(1,101))))



