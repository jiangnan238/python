numbers=(1,2,3,4)
#print(numbers[0])
#print(numbers[-1])
#numbers[0]=100 #元组元素不可修改，修改报错
for i in range(0,4):
    print(numbers[i])#遍历元组元素

#不可以修改但是可以重新赋值
numbers=(5,6,7,8)
for number in numbers:
    print(number)

#--------------------------------------------------------------
Dishs=("宫保鸡丁","啤酒鸭","清蒸鱼","辣椒炒肉","红烧肉")
for dish in Dishs:
    print(dish)
#Dishs[0]="小炒鸡块"
print("换菜单\n")
Dishs=("宫保鸡丁","啤酒鸭","红烧鱼","辣椒炒肉","小龙虾")
for dish in Dishs:
    print(dish) 