x=[[10,20],[11.2,12.3],"hii",90]
print(x)
print(x[1])
print(x[1][1])
print(x[2])
print("=======================================================")

x=[[10,20],[11.2,12.3],"hii",90]
for i in x:
    print(i)
print("=======================================================")


x=[[10,20],[11.2,12.3],"hii",90]
for i in x:
    if type(i)==list:
     for j in i:
      print(j)
    continue
print(i)

print("=======================================================")


student=[[101,"ram",98],
         [102,"sita",88],
         [103,"ramu",78],
         [104,"gita",99]]
for i in student:
   print(i[1])
print("=======================================================")


student=[[101,"ram",98],
         [102,"sita",88],
         [103,"ramu",78],
         [104,"gita",99]]
for i in student:
   print(f"{i[1]}-->{i[2]}")
print("=======================================================")

student.append([105,"komal",55])
id=int(input("enter id:"))
name=input("enter name:")
marks=int(input("enter marks:"))
student.append([id,name,marks])
print(student)
print("=======================================================")



student=[]

while True:
   print("SMS\n1.add\n2.view\n3.update\n4.delete\n5.Topper\n6.exit\n")
   choice=int(input("enter your choice\n"))

   match choice:

      case 1:
         ip=int(input("how many student data do you want to add\n"))
         for i in range(ip):
            id=int(input("enter your id \n"))
            name=(input("enter your name"))
            marks=int(input("enter marks"))
            student.append([id,name,marks])
            print(f"student{i+1} added")

      case 2:
         if len(student)==0:
            print("no data found")
         else:
            print("ID   NAME   MARKS")
            for i in student:
               print(f"{i[0]}   {i[1]}   {i[2]}")

      case 3:
         sid=int(input("enter your id"))
         for i in student:
            if sid==i[0]:
               print("1.update marks\n2.update name\n3.All details\n4.exit")
               choice=int(input("enter your choice\n"))

               if choice==1:
                  ex_marks=i[2]
                  new_marks=int(input("enter new marks to update !\n"))
                  i[2]=new_marks
                  print(f"{ex_marks} updated to {new_marks} marks !")

               elif choice==2:
                  ex_name=i[1]
                  new_name=input("enter new name\n")
                  i[1]=new_name
                  print(f"{ex_name} updated to {new_name}")

               elif choice==3:
                  id=int(input("enter new id\n"))
                  name=input("enter new name\n")
                  marks=int(input("enter new marks\n"))
                  i[0]=id
                  i[1]=name
                  i[2]=marks
                  print("all details updated")

               elif choice==4:
                  break
         else:
            print("student not found")

      case 4:
         sid=int(input("enter id to delete\n"))
         for i in student:
            if sid==i[0]:
               student.remove(i)
               print("student deleted")
               break
         else:
            print("student not found")

      case 5:
         if len(student)==0:
            print("no data found")
         else:
            top=student[0]
            for i in student:
               if i[2] > top[2]:
                  top=i
            print("Topper details:")
            print(f"{top[0]}   {top[1]}   {top[2]}")

      case 6:
         print("thank you")
         break

      case _:
         print("invalid choice")
         
         