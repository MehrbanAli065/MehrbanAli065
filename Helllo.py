import random
#print("hello world")

#LAB ACTIVITY ONE
"""
for i in range(20):
    if i%3==0:
        print (i)
    if i%5==0:
        print ("BINGO!")
    print("----------------------------------------------")
"""

# lab activity 2
"""
n=input("Enter a number: ")
if int(n)%2==0:
    print("Given number is even ")
else:
    print("Given number is odd")
"""


# lab activity 3
"""
sum=0
s=int(input("Enter an integer value..."))
while s!=0:
    sum=sum+s
    s = int(input("Enter an integer value..."))
print("sum of given value is",sum) 
"""

# lab activity 4
"""
isprime=True
i=2
n=int(input("Enter a number..."))
while i<n:
    remainder=n%i
    if remainder==0:
        isprime=False
        break
    else:
        i=i+1
if isprime:
    print("Number is prime")
else:
    print("Number is not prime")
"""


# lab activity 5
"""
sum=0
i=0
while i<4:
    s=int(input("Enter number...."))
    sum=sum+s
    i = i + 1
print("sum is",sum)
"""

# lab activity 6
"""
summation=0
i=1
while i<=10:
    summation=summation+i
    i = i + 1
print("Summation is: ",summation)
"""



# lab activity 7
min=1
max=9
num=random.randint(min,max)
guess=None
Another=None
Try=0
Running=True
print("Alrigyht")

while Running:
    guess=input("What is ur lucky number")
    if int(guess)<num:
        print("Wrong too low")
    elif int(guess)>num:
        print("Wrong too high")
    elif guess.lower()=="Exit":
        print("Better luck next time.")
    elif int(guess)==num:
        print("yes thats the one", str(num))
        if Try<2:
            print("impressive only %s tries"% str(num))
        elif Try>2 and Try<10:
            print("Pretty good",Try)
        else:
            print("Bad",Try)
        running=False
    Try+=1



# Task 1

"""
num=int(input("Enter a number that have to revers"))
rev_num=0
while num!=0:
    digit=num%10
    rev_num=rev_num*10+digit
    num //=10
print("reversed number: "+str(rev_num))

#method 2 with string slicing
num=123456
print(str(num)[::-1])
"""


# Task2s
"""
odd=0
even=0
count_even=0
count_odd=0
inp=int(input("Enter integer....."))
for i in range(inp+1):
    if i%2==0:
        print("Number",i ,"is even")
        even=even+i
        count_even=count_even+1
    else:
        if i % 2 != 0:
            print("Number",i ,"is odd")
            odd = odd + i
            count_odd = count_odd + 1
print("sum of even numer is: ",even,"total even number is",count_even)
print("sum of odd numer is: ",odd,"total odd number is",count_odd)
"""
