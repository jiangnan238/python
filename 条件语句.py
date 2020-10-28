car=['audi','bmw','subaru','toyota']
if (car[0]=='audi') and (car[1].title()=='Bmw'):#使用and 并联条件
    print("ture")
else:
    print(car[1].title())#if语句区分大小写
#-------------------------------------------------
if 1>2 or 2==3:#or只要一个满足就返回true
    print ("just have one")
else:
    print("no one conform")
#-------------------------------------------------
#检查特定值是否在列表中
if 'audi' in car:
    print("yes")
if 'Tesla' not in car:
    print('tesla no in it.')
#------------------------------------------------
#布尔逻辑运算
print(car[0]=='audi')#返回true
print(car[1]=='audi')#flase
