
def factorial(n):
	
	if n == 0:
		return 1
	
	return n * factorial(n-1)


num = int(input("enter number"));
print("Factorial of", num, "is",
factorial(num))
