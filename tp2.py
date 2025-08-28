#1

number = int(input("Guess the number : "))
sn = int()


while number !=sn :
        if number < sn :
            print("Number is too low ")
        else:
            print("Number is too high " ) 
        number = int(input("Guess the number again : "))

print("Congratulations you have guessed the number ")   

#2

math = ["charlie", "kevin","alise", "bob", "leo"]
physics = ["jack", "paolo", "alex", "bob", "charlie"]

math.append(input("Add a new student to the math list : "))
physics.insert(2,input("Enter the new student to the physics list : "))
math.sort()
physics.sort()

print("The math list is : ",math)
print("The physics list is : ",physics)

student  = input("Add a new student to the physics list : ")
physics.append(student)


student  = input("Select a student name to delete from the physics list ")
if student in physics :
    physics.remove(student)
    print(student ,"has been deleted from the list ")
else :
    print("This student doesn't exist within the list of physics")   

print("The final math list is : ",math)
print("The final physics list is : ",physics)

#3

import turtle

yanis = turtle.Turtle()

yanis.pensize(10)
yanis.shape("turtle")
yanis.speed(1)
turtle.bgcolor("white")

colors = ["red", "blue", "green", "yellow", "purple", "orange"]
size = int(input("Enter the size of each side of the hexagon : "))

for i in colors:
    yanis.pencolor(i)
    yanis.forward(size)
    yanis.left(60)

#4

scores = {
 "Alice": 88,
 "Bob": 95,
 "Charlie": 90
}
i = 0
name = ""
for key , value in scores.items():
    if i < value: 
        i = value
        name = key 

print("The highest score is :",i,"by",name)         
