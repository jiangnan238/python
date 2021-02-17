#网站用户
users = ['admin','jack','john','tom','mary']
for user in users:
	print('welcome ,',user,'!',end='\n')
#增加用户
new_user = input('please input you name:\n')
if new_user.lower() in users:
	print('this name is used')
if new_user.lower() not in users:
	users.append(new_user)
print(users)
#删除所有用户
del users[0:len(users)]
print(users)