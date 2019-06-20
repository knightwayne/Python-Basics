###conditionals and loops


#if...else
name="batman"
if name=="batman":
    print("Hey Batman!!!");
else:
    print("Hey Thanos!!!");


#if...elif...else
print("Enter your name.");
name = input();
if len(name)==0:
    print("Your name has no characters at all!");
elif (len(name)%2==1):
    print("Your name has odd number of characters!");
else:
    print("Your name has even number of characters!");


#while loop
print("Guess a number!");
count=1;
number=input();
while int(number)!=7:
    print("Oops! Guess again!");
    number=input();
    count+=1;
print("Whooooo!! Correct Guess!!! Took you " + str(count) + " guesses.");


#for loop
i=0;
for i in range(5):
    print(i);
print("for loop 1 exit");

print("Enter 2 numbers, x and y.")
x=int(input());y=int(input());
sum=0;
for i in range(x,y+1):
    print("Current index: " + str(i));
    sum+=i;
print("Sum is: " + str(sum));
print("for loop 2 exit");
