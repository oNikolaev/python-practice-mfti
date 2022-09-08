# Кортежи и списки
import turtle

A = range(1, 6)
print(*A)

for x in A:
    print(x)

A = [(1, 10), (2, 20), (3, 30)]
for i in range(len(A)):
    angle, length = A[i]
    turtle.forward(length)

for T in A:
    angle, length = T
    turtle.forward(length)

for angle, length in A:
    turtle.forward(length)

A = [(10), (20), (30)]
for i, x in enumerate(A):
    print(i, x)

A = [(1, 10), (2, 20), (3, 30)]
for i, (angle, length) in enumerate(A):
    print(i, angle, length)
