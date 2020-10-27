#如何使用循环遍历一个列表
games=['LOL','OV','CS','DOTA']#定义一个列表
i=0
for game in games:
    i=i+1
    #print("Game"+str(i)+":\t"+game)#缩进则在循环内部
    #games输出整个列表
#print("my favorite game is: "+games[0])#不缩进在循环外部即循环结束后运行一次。
#--------------------------------------------------------------------------------
#函数range
for value in range(2,10,2):#2~10输出间隔为2
    print(value)#在5停止，不打印5
#使用range函数创建列表
number = list(range(1,4,1))
print(number)
#输出1-10的平方
squares = []
for value in range(1,11,1):
    num=value**2#定义num等于value的平方
    squares.append(num)#列表添加num
print(squares)
#列表解析等同于上面
squares_example=[num2**2 for num2 in range(1,11,1)]#[表达式 给表达式赋值]
print(squares_example)
