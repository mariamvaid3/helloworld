#Mariam Vaid
#1477614
#6.22

g = int(input())
h = int(input())
d = int(input())

o = int(input())
p = int(input())
q = int(input())


for x in range(-10, 11):
    for y in range(-10, 11):
        if g * x + h * y == d and o * x + p * y == q:
            print(x, y)
            sol_fou = true

if not sol_fou:
    print("No solution")
