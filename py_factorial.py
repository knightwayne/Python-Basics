def factorial(n):
	if n==1:
		return 1
	else:
		return n*factorial(n-1)

i=int(input())
while i<=7:
	print(factorial(i))
	i+=1

