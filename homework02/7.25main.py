#Mariam Vaid
#1477614
#7.25 

def exact_change(user_total):
    num_dollars = user_total // 100
    user_total = user_total % 100
    num_quarters = user_total // 25
    user_total = user_total % 25
    num_dimes = user_total // 10
    user_total = user_total % 10
    num_nickels = user_total // 5
    user_total = user_total % 5
    num_pennies = user_total
    return num_dollars, num_quarters, num_pennies, num_dimes, num_nickels



