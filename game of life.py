import time

k = []
l = []

a = int(input("a = "))
b = int(input("b = "))

for i in range(a * b):
    l.append("-")

while True:
    x = input("x = ")
    if x!="f":
        y = int(input("y = "))
        x = int(x)
    else:
        break

    l[x + (y - 1) * a - 1] = "*"

c = 0

for i in range(b):
    print(l[(i * a):(a * (i + 1))])
print('\n')

for i in l:
    k.append(i)

while True:
    time.sleep(1)
    for i in range(b):
        for j in range (a):
            c = 0
            if l[(i - 1) * a + j - 1] == "*":
                c = c + 1
            if l[(i - 1) * a + j] == "*":
                c = c + 1
            if l[(i - 1) * a + j + 1] == "*":
                c = c + 1
            if l[i * a + j - 1] == "*":
                c = c + 1
            if (i * a + j + 1)<(len(l)):
                if l[i * a + j + 1] == "*":
                    c = c + 1
            if ((i + 1) * a + j - 1)<(len(l)):
                if l[(i + 1) * a + j - 1] == "*":
                    c = c + 1
            if ((i + 1) * a + j)<(len(l)):
                if l[(i + 1) * a + j] == "*":
                    c = c + 1
            if ((i + 1) * a + j + 1)<(len(l)):
                if l[(i + 1) * a + j + 1] == "*":
                    c = c + 1

            if l[i * a + j] == "-":
                if c == 3:
                    k[i * a + j] = "*"

            if l[i * a + j] == "*":
                if c == 0 or c == 1 or c == 4 or c == 5 or c == 6 or c == 7 or c == 8:
                    k[i * a + j] = "-"

    for i in range(b):
        print(k[(i * a):(a * (i + 1))])
    print('\n')

    l.clear()
    for i in k:
        l.append(i)

#   0  1  2  3  4 a
#0  0  1  2  3  4
#1  5  6  7  8  9
#2  10 11 12 13 14
#b
#x + y * a