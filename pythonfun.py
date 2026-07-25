def print1to10():
    i=1
    while i<=10:
        print(i)
        i+=1

def table():
    num=int(input("Enter a number: "))
    for i in range(1,11):
        print(num,"x",i,"=",num*i)

def prime():
        
    num=int(input("Enter a number: "))
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                print(num,"is not a prime number")
                break
        else:
            print(num,"is a prime number")
    else:
        print(num,"is not a prime number")


def reverse():
    num=int(input("Enter a number: "))
    rev=0
    while num>0:
        dig=num%10
        rev=rev*10+dig
        num=num//10
    print("Reversed number is: ",rev)


def fibonacci():
    n=int(input("Enter the number of terms: "))
    a,b=0,1
    count=0
    if n<=0:
        print("Please enter a positive integer")
    elif n==1:
        print("Fibonacci sequence upto",n,":")
        print(a)
    else:
        print("Fibonacci sequence:")
        while count<n:
            print(a)
            a,b=b,a+b
            count+=1


def palindrome():
    num=int(input("Enter a number: "))
    temp=num
    rev=0
    while temp>0:
        dig=temp%10
        rev=rev*10+dig
        temp=temp//10
    if num==rev:
        print(num,"is a palindrome number")
    else:
        print(num,"is not a palindrome number")


while(1) :
    print("1 - 1to10\n2 - Table\n3 - Prime\n4 - Reverse\n5 - Fibonacci\n6 - Palindrome\n")
    ch=int(input("Enter your choice: "))
    if ch==1:
        print1to10()
    elif ch==2:
        table()
    elif ch==3:
        prime()
    elif ch==4:
        reverse()
    elif ch==5:
        fibonacci()
    elif ch==6:
        palindrome()
    else:
        print("Invalid choice")

    c=int(input("Do you want to continue? (1 for yes, 0 for no): "))
    if c!=1:
        break
    
    print("----------------Thank you----------------")
