# fizzbuzz challenge
def fizzBuzz(val):
	if (val % 5 == 0) and (val % 3 == 0):
		return("FizzBuzz")
	elif (val % 5 == 0):
		return("Buzz")
	elif (val % 3 == 0):
		return("Fizz")
	else:
		return val

for i in range(1,101):
	print(fizzBuzz(i))

