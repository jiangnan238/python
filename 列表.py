list1=['a','b','c','d','e','f',"jiangnan"]

print(list1)#打印整个列表包括括号

print(list1[1])#打印列表元素从0开始

print ("my name is ",list1[-1].upper())#-1表示最后一个，依次-2为倒数第二个

list1[0]="z"#修改列表第一个元素
print(list1)

list1.append('y')#列表最末尾增加元素
print(list1)

list1.insert(0,"who")#第一个位置增加元素
print(list1)

del list1[-2]#删除元素
print(list1)

num1=list1.pop(0)#弹出第一个元素
print(list1)#弹出元素不在列表
print(num1)

list1.remove('e')#删除只知道值但不知道位置的元素
print(list1)

print(sorted(list1))#临时排序，原列表不改变

list1.sort()#永久性按字母排序（冒泡排序法）
print(list1)

list1.sort(reverse=True)#倒序
print(list1)

list1.reverse()#永久性倒序==>再次使用恢复原状
print(list1)

print(len(list1))#len列表长度