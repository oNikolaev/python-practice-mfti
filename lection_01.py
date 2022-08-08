# Дзен Python
# name = input("Введите имя: ")
# print(f"Привет {name}!")
#
# x = 10
# while True:
#     if (x < 0):
#         break
#     print(x)
#     x -=1

# for x in 5,3,7:
#     print(x ** 2)

# x = int(input("x: "))
# y = int(input("y: "))
#
# if y > 0:
#     if x > 0:
#         print(1)
#     else:
#         print(2)
# else:
#     if x < 0:
#         print(3)
#     else:
#         print(4)

# import turtle
# turtle.shape('turtle')
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
#
# turtle.color('green')
# for step in range(6):
#     turtle.forward(100)
#     turtle.left(60)
#
# turtle.color('blue')
# for step in range(20):
#     turtle.forward(25)
#     turtle.left(18)
#
# turtle.color('red')
# for step in range(40):
#     turtle.forward(35)
#     turtle.left(9)
#
# turtle.color('yellow')
# for step in range(360):
#     turtle.forward(1)
#     turtle.left(1)

import turtle

def david():
    turtle.speed(10)
    turtle.color('green', 'yellow')

    for step in range(6):
        turtle.begin_fill()
        for i in range(3):
            turtle.forward(50)
            turtle.left(360 / 3)
        turtle.end_fill()

        turtle.forward(50)
        turtle.right(60)

for i in range(4):
    david()
    turtle.backward(200)