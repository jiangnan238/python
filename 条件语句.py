#    car=['audi','bmw','subaru','toyota']
#    if (car[0]=='audi') and (car[1].title()=='Bmw'):#使用and 并联条件
#        print("ture")
#    else:
#        print(car[1].title())#if语句区分大小写
#    #-----------------------------------------------------
#    if 1>2 or 2==3:#or只要一个满足就返回true
#        print ("just have one")
#    else:
#        print("no one conform")
#----------------------------------------------------------
#检查特定值是否在列表中
#    if 'audi' in car:
#        print("yes")
#    if 'Tesla' not in car:
#        print('tesla no in it.')
#---------------------------------------------------------
#布尔逻辑运算
#    print(car[0]=='audi')#返回true
#   print(car[1]=='audi')#flase
#---------------------------------------------------------
#    favotite_fruits=['apple','banana','pear','orange']
#    for favotite_fruit  in favotite_fruits:
#        if favotite_fruit =='banana':
#            print("my favorite fruit is "+favotite_fruit+'.')
#       elif favotite_fruit!='banana':
#           print("i don't like "+favotite_fruit+'.')
#------------------------------------------------
#如果列表为空返回false
empty=[]
if empty:
    print("true")
else:
    print("false")
#--------------------------------------------------------
numbers=['1','2','3','4','5','6','7','8','9']
for number in numbers:
    if number =='1':
        print(number+"st")
    elif number =='2':
        print(number+'nd')
    elif number =='3':
        print(number+'rd')
    else:
        print(number+'th')
#---------------------------------------------------------