#Mariam Vaid
#1477614
#8.10

if __name__ == '__main__':
    user_input = input()
    normal = ""
    reverse = ""
    for tx in user_input.lower():
        if tx != ' ':
            normal += tx
            reverse = tx + reverse
    if normal == reverse:
        print(user_input + " is a palindrome")
    else:
        print(user_input + " is not a palindrome")
