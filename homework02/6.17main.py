#6.17
#Mariam Vaid
#1477614

passsword=input()
passsword = list(passsword)
for i in range(0,len(passsword)):
    if(passsword[i]=='i'):
        passsword[i]='!'
    elif(passsword[i]=='a'):
        passsword[i]='@'
    elif(passsword[i]=='m'):
        passsword[i]='M'
    elif(passsword[i]=='B'):
        passsword[i]='8'
    elif(passsword[i]=='o'):
        passsword[i]='.'

strong_pass=""
strong_pass=strong_pass.join(passsword)
strong_pass=strong_pass + "q*s"

print(strong_pass)
