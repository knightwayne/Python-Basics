#functions


#function definition
def greeting():
    print('Please enter your name.');
    name=input();
    print('Hi ' + name + '! Nice to meet you!!!');

#function  call
greeting();


#Iterative Sum Programme
def sum(n):
    i=1;
    sum=0;
    for i in range(n+1):
        sum+=i;
    print('Sum is: ' + str(sum));


print('Enter a number');
#n=int(input());
#sum(n);
sum(int(input()));


#Recursive Factorial Programme
def factorial(n):
    if n<=1:
        return 1;
    else:
        return n*factorial(n-1);

print("Enter a number whose factorial is to be found.")
print("Factorial is " + str(factorial(int(input()))) );


