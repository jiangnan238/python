#创建字典
man = {'name':'jiangnan','age':23,'height':170,'weight':98}

#修改键-值
man['height'] = 175
print(man)

#删除键值对
del man['weight']
print(man)

#遍历键值对
for key,value in man.items():
    print('key:'+str(key))
    print('value:'+str(value))

#遍历所有键
for keys in man.keys():
    print("%-8s"%keys,end='\t')
print(end='\n')

#遍历所有值
for values in man.values():
    print("%-8s"%values,end='\t')
print(end='\n')

#排序遍历键
for keys in sorted(man.keys()):
    print("%-8s"%keys,end='\t')
print(end='\n')
print(man)#字典并不会改变顺序
