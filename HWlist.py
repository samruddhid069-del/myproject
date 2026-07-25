#1
x = [101, 57, 6, 98, 32, 10, 57, 98, 6]
print(x)

key = int(input("Enter number to search: "))

if key in x:
    print("Element found")
else:
    print("Element not found")
print("================================================")


#2
x = [101, 57, 6, 98, 32, 10, 57, 98]

printed = []

for i in x:
    if x.count(i) > 1 and i not in printed:
        print(i, "is duplicate")
        printed.append(i)
print("================================================")

#3
x = [101, 57, 6, 98, 32, 10, 57, 98]

for i in x:
    if x.count(i) == 1:
        print(i, "is unique")
print("================================================")

#4
x = [101, 57, 6, 98]

for i in range(len(x)):
    for j in range(i+1, len(x)):
        if x[i] > x[j]:
            x[i], x[j] = x[j], x[i]

print(x)
print("================================================")
 

#5
x = [101, 57, 6, 98, 32, 10, 57, 98]

result = []

for i in x:
    if i % 2 == 0:
        result.append(0)   
    else:
        result.append(1)   

print(result)
print("================================================")







