#try...except block


def divideFunction(n):
    try:
        print(str(42/n));
    except:
        print('Hawww!!! You just tried to divide by zero!');

print('Enter the divisor.');
divideFunction(int(input()));
