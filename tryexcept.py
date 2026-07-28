#1st pgm
print("start")
try:
    ip=int(input("Enter the number"))
    print(ip)
except ValueError as e:
    print(e)
print("progream ended  ")


#2nd pgm
print("srart")
try:
    x=[10,20]
    print(x[9])
except IndexError :
    print("please enter valid index")
print("program ended ")


#3rd pgm
print("start")
try:
  x=[10,20]
  print(x[1])
  print(10/0)
except IndexError as e:
  print(e)
except ZeroDivisionError:
  print("dont divide by zero")
print("program ended ")


# 4th pgm
print("start")
try:
  x=[10,20]
  print(x[1])
  print(10/0)
except Exception as e:
  print(e)
print("Program ended")


# 5th pgm
print("start")
try :
    ip=int(input("Enter the number"))
    print(10/ip)
except (ValueError,ZeroDivisionError):
    print("something went wrong")
finally:
  print("im always execute")
print("Program ended ")

# 6th pgm
class AgeError(Exception):
    pass 
print("start")
age=int(input("enter your age"))
if age>18:
    print("eligible")
else:
    raise AgeError("Age should be greater than 18 ")
print("=======")