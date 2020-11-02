user={'name':'jiangnan','age':'23','sex':'man','like':'LOL','test':'empty'}#创建一个字典
#del user['test']#删除字典中的项目
#print(user)
#-------------------------------------------------------
#for Key,Value in user.items():#声明两个变量，这两个变量可使用任何名称
#    print("key: "+Key+"\tvalue: "+Value)#将键与值分别存储在变量中
#    print(user[Key])#通过当前键输出当前值
#-------------------------------------------------------
#for item in user.items():#键与值全部存储在一个变量中
    #print(item)
#-------------------------------------------------------
#for key in user.keys():#只输出键而不需要值
    #print(key)
#-------------------------------------------------------
#for Value in user.values():#输出字典中的值
#    print(Value)
#-------------------------------------------------------
favorite_languages = {"jen":"python",    "sarah":"c",    "hjh":"ruby",    "phil":"java"}
staff_lists=['jen','jack','tom','jerry','john']
for staff_list in staff_lists:
    if staff_list in favorite_languages.keys():
        print(staff_list+",thank you for your participation!")
    else:
        print(staff_list+",do you want join us?")
