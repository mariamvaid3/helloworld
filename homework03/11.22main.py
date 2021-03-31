#Mariam Vaid
#1477614

wording = input().split()
for letter in wording:
    count = 0
    for x in wording:
        if x == letter:
            count += 1
    print(letter, count)
