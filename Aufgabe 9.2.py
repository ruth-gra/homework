number = int(2)

for number in range(1,100):
    if number % 3 == 0:
        print("fizz")
    if number % 5 == 0:
        print("buzz")
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    else:
        print(number)