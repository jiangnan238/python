# 让使用者在名为 table 的 dict 中，输入五组的 key-value pair，key 是字符串、 value 是数字，最后把这个 dict 印出来。
# (提示: dict 没有 append，直接用增 加或更新(InsertOrUpdate)的方式)
# table = {}
# for i in range(0,3):
#     k = input('please input string:')
#     v = int(input('please input number:'))
#     table[k] = v
#     print(end='\n')
# print('table=',table)

match={'tom':88,'jack':90,'john':55,'peter':99,'mary':78}
print(match)
for checktimes in range(0,3):
    name = input('please input player name:')
    if name in match.keys():
        print('his grade is ',match[name],end='\n')
    else:
        print('no this player!')
    #print(match.get(name,'no this people!'))