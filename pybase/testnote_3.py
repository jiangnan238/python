#五次数学段考的成绩分别为 10、30、50、70、90 分，算出平均后，老师发现大 家考太烂、只好将成绩开根号再乘上 10 ，再算出一个新 平均。
math_grades = [10,30,50,70,90]
print('grades:',end=' ')
for grade in math_grades:
    print(grade,end=' ')
print(end='\n')
average = sum(math_grades)/len(math_grades)
print('average:',average,end='\n')
print('new grades:',end=' ')
for grade in range(0,len(math_grades)):
    math_grades[grade]= pow((math_grades[grade]),0.5)*10
    print('%f'%math_grades[grade],end=' ')
print(end='\n')
average = sum(math_grades)/len(math_grades)
print('new average:',average)

#来办场 Party 吧! 输入十个整数、存入一个名为 people 清单中 (表示我们的宴客人数)；
#之后会有五次询问，每次会输入列表开始和结束的位置，再输出从开 始到结束位置的总和。
people=[]
for i in range(0,10):
    i=int(input('please input number:'))
    people.append(i)
print(people,end='\n')
a = int(input('please input head:'))
b = int(input('please input end:'))
print('sum:',sum(people[a:b]))