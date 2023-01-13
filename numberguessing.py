import random

a = random.randint(1,50)

#print('your number is',a)

def divisibleBy(n):
    
    if n%3 == 0:
        return print('number is divisible by 3')
    elif n % 4 == 0:
        return print('number is divisible by 4')
    elif n % 5 == 0:
        return print('number is divisible by 5')
    elif n % 6 == 0:
        return print('number is divisible by 6')
    elif n % 7 == 0:
        return print('number is divisible by 7')
    elif n % 8 == 0:
        return print('number is divisible by 8')
    elif n % 9 == 0:
        return print('number is divisible by 9')
    elif n % 10 == 0:
        return print('number is divisible by 10')
    elif n % 11 == 0:
        return print('number is divisible by 11')
    else:
        return print('number is not divisible from number upto 11')
    
def evenOrOdd(n):
    if n % 2 == 0:
        return print('number is an even number.')
    else:
        return print('number is an odd number.')

def lessThan(n):
    if n < 10:
        return print('number is less than 10')
    elif n < 20:
        return print('number is less than 20')
    elif n < 30:
        return print('number is less than 30')
    elif n < 40:
        return print('number is less than 40')
    else:
        return print('number is less than 50')

def greaterThan(n):
    if n > 40:
        return print('number is greater than 40')
    elif n > 30:
        return print('number is greater than 30')
    elif n > 20:
        return print('number is greater than 20')
    elif n > 10:
        return print('number is greater than 10')
    else:
        return print('number is greater than 0')

def primeNumber(n):
    c = 1
    for i in range(2,n-1):
        if n % i == 0:
            return print('number is a composite number.')
            c = 0
    if c == 1:
        return print('number is a prime number.')
            
        
wrongCount = 5
funcList = [divisibleBy,evenOrOdd,lessThan,greaterThan,primeNumber]
inputGuess = int(input('Guess a number : '))
while inputGuess != a and wrongCount >0:
    print('you guess a wrong number.')
    print('New Hint : ')
    function = random.choice(funcList)
    function(a)
    inputGuess = int(input('Guess a number : '))
    wrongCount -= 1
    print('remaining guesses',wrongCount)
if wrongCount == 0:
    print('you lose.','The number was',a)
else:
    print('You have guessed the right number.', 'the number was',a)