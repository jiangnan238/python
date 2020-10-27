#1~100求和
a=[]
for i in range(1,101):
    a.append(i)
#print(a)#打印1-100
#最小值函数min()
#print(min(a))#输出最小值
#最大值函数max()
#print(max(a))#输出最大值
#求和函数sum()
#print(sum(a))#求和
#----------------------------------------------------------------------------------
#函数解析 100以内可以被3整除的数的立方
cube=[j**3 for j in range(3,101,3)]
#print(cube)
#----------------------------------------------------------------------------------
example_1=["the","first","three","items","in","the","list","are"]
#print(example_1[0:3])#打印前三个
#print(example_1[3:6])#打印中间三个
#print(example_1[-3:])#打印末尾三个
example_2=example_1[:]
example_1.append("ONE")#末尾添加ONE
example_2.append("TWO")#末尾添加TWO
print("the examle one:")
print(example_1)
print("the examle two:")
print(example_2)