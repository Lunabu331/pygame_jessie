# 公式解
a = 1
b = 2
c = -63
x1 = ((-1 * b) + (b**2 - 4 * a * c)**(0.5))/(2*a)
x2 = ((-1 * b) - (b**2 - 4 * a * c)**(0.5))/(2*a)
print (x1, x2)


# 座標
d = input()
e = input()

if int(d) > 0:
    if int(e) > 0:
        print("I")
    else:
        print("IV")
else:
    if int(e) >0:
        print("II")
    else:
        print("III")


# 猜數字遊戲
import random
f = random.randint(1,100)
h = 0
while h == 0:
    g = int(input())
    if g > f:
        print("Too big")
        continue
    elif g < f:
        print("Too small")
        continue
    else:
        print("Correct")
        h = 1



# 星星三角形
i = 1
j = 1
while i <= 5:
    while j <= (6-i):
        print("*", end = "")
        j += 1
    j = 1
    print("")
    i = i + 1
    


# MxM
def f(m):
    i = 1
    j = 1
    while i <= m:
        while j <= m:
            l = i * j
            print(i, "*", j , "=", l, end = "  ")
            j += 1
        j = 1
        print("")
        i += 1
k = int(input())
f(k)

# 交換
def f(a,b):
    i = a
    a = b
    b = i
    return a,b
m = f(3,5)
print(m)

# Judge_big_lower
def f(a,b):
    if a > b:
        i = "a>b"
    elif a < b:
        i = "a<b"
    else:
        i = "a=b"
    return i

m = f(1,2)
print(m)


# N^X
def maker(n):
    def inside(m):
        i = n**m
        return i
    return inside

f= maker(9)
print(f(5))

# Fibonacci
def Fibonacci(m):
    i = 1
    a = 0
    b = 1
    while i <= (m-1):
        c = a + b
        if i == (m-1):
            print(c)
        else:
            a = b
            b = c
        i += 1
Fibonacci(int(input()))


# 日期
import datetime
a = datetime.date(2019,7,13)
print(a)


# map
class Map:
    def set_map(self,n):
        global e
        d = []
        for i in range (1, n+2):
            d.append("*")
        e = []
        for j in range (1, n+2):
            e.append(d)
        
    def set_pattern(self, m):
        global e
        if m == 1:
            e[int((len(e[0]) + 1)/2)][int(((len(e[0]) + 1)/2)-1)] = 0
            e[int(((len(e[0]) + 1)/2)-1)][int(((len(e[0]) + 1)/2))] = 1
            e[int(((len(e[0]) + 1)/2)-1)][int(((len(e[0]) + 1)/2)-1)] = 2
            e[int(((len(e[0]) + 1)/2)-1)][int(((len(e[0]) + 1)/2)+1)] = 3
            e[int(((len(e[0]) + 1)/2)+1)][int(((len(e[0]) + 1)/2))] = 4
    
    def display(self):
        for i in range (1, len(e[0])):
            for k in range (1, len(e[0])):
                print (e[i][k], end= "")
            print("")
    
map = Map()
map.set_map(5)
map.display()
map.set_pattern(1)
map.display()


# car
class car(a):
    color = a
    speed = 0
    def boost(self):
        speed += 1
    def step_break(self):
        speed -= 1
car1 = car("pink")
car2 = car("red")

# animal/dog
class animal:
    shout = "Hi"
    feet_number = 4
class dog(animal):
    pass
print(dog.shout)
