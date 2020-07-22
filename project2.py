user= int(input('ENTER THE NUMBER:'))

if user%11==0 and user%5==0:
    print(user)
    print('The number is divisible by 5 and 11')
else:
    print(user)
    print('The number is not divisible by 5 and 11')