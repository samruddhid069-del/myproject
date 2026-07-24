name="Ram"
print(name)
print(id(name))
print(name[0])
print(name[1])
name="Samruddhi"
print(name)
print(id(name))



#given string--->fetch one by one

for ch in name:
    print(ch)

#find length of string
x="Maharashtra"
print(len(x))


#reverse of string
for ch in range(len(x)-1,-1,-1):
    print(x[ch] ,end="")



#count of a particular character in string
x="india"
count=0
for ch in x:
    count+=1
print(count)



#methods in string
x="India"
print(x.upper())
print(x.lower())
x="hello how are you ?"
print(x.title())
print(x.capitalize())
x="India"
print(x.swapcase())
print(x.replace("dia","x"))
print(x.replace('i','z'))


x="apple banana grapes"
print(x.count("p"))
print(x.count("e)"))
print(x.find('v'))#if present then return index else -1
print(x.split(','))

#checking methods(true or false)
x="hello"
print(x.isupper())
print(x.islower())
#check-->all alphabet or not
print(x.isalpha())

x="1234"
print(x.isdigit())

#alpha+num
x="abc123"
print(x.isalnum())

print(x.startswith("abc"))
print(x.endswith("123"))

#white spaces ---->remove
x="  hello"
print(len(x))
x=x.strip()
print(len(x))

#pgm to count number of characters in a string without using len() function
str=input("enter a string:")
print(str)
count=0
ch=input("enter a character to count:")
for c in str:
    if c==ch:
        count+=1
print(count)




