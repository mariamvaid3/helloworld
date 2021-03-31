#Mariam Vaid
#1477614

allnumbers = input().split()
result = []

for number in allnumbers:
    number = int(number)
    if number >= 0:
        result.append(number)

result.sort()
for number in result:
    print(number, end=' ')
