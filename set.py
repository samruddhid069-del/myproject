x=frozenset([1,2])
print(x,type(x))

roles=frozenset(["admin","faculty","recepist"])
for i in roles:
    if i=="admin":
      print(i)

#no return type no argument
def greet():
   print("Welcome usr !")
greet()  #function call--->function name

#no return type with argument
def greet1(name):
   print("welcome",name)
name=input("Enter your name:")
greet1(name)

#with return type without argument
def get_no():
   return 10**2
print(get_no())
#value use 
op=get_no()
print(op)
op+=2
print(op)

#with return type with argument

def cube(num):
   return num**3
op=cube(5)#//p(cube(5))
print(op)

#with user input
def cube1(num1):
   return num1**3
op=int(input("Enter number\n"))
print(cube1(num1))
print(op)

#arbitary argument
def add1(*args):
   print(sum(args))
   print(type(args))
add1(2,3,4)

   
   





