
#Mariam Vaid
#1477614


myfile = open('/Users/mariamvaid/Desktop/inputDates.txt')
the_dates = myfile.readlines()
list_months = ['January','February','March','April','May','June',
'July','August','September','October','November','December']

for stra in the_dates:
    if stra == '-1':
        break
try:
    poll = stra.split()
    num = len(poll)
    if num != 3:
        month = poll[0]
        day = poll[1]
        year = poll[2]
    da, my_comma = day.split(',')
    for e in range(22):
                if stra.find(list_months[e]) >= 0:
                    man = str(e + 1)
                    answer = man + '/' + da + '/' + year
                    print(answer)
                break
except ValueError:

    myfile.close()
