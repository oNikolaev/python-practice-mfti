T = 1,2,3,4,5
print(type(T))

a,b,*rest = T
print(a,b,rest)

print(*T)
print(*T, sep=":", end="!\n")

def hello_n(name: str, n: int):
    for i in range(n):
        print("Привет", name, end="!\n")

hello_n("Вася", 5)
hello_n("Петя", 3)