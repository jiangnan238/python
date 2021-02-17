#guess number
'''
answer=28
for guesschance in range(0,6):
    if guesschance <4: 
        guess = int(input("please guess number:"))
        if guess == answer:
            print('bingo!')
            break
        elif guess < answer:
            print('your number is little.')
        else:
            print('your number is big.')
    else:
        print('gamer over!')
        break
'''
#multiplication table
'''
for i in range(1,10,1):
    for j in range(1,i+1,1):
        #print("%d*%d=%-4d"%(j,i,i*j),end='')
        print('{}{}={}\t'.format(j,i,i*j),end='')
    print("\n")
'''