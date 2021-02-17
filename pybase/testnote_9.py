#函数

'''
def favorite_book(title='jiangnan'):
    #默认设置为jiangnan
    print("One of my favorite books is "+title+'.')

favorite_book('longzu')
favorite_book()#不指定输出默认值

#定义音乐专辑
def make_album(singer_name,album_name,album_number = 0):
    album = {}
    album[singer_name] = album_name
    album['number'] = album_number
    return album

#调用
while True:
    name = input("singer name： ")
    song = input("ablum name： ")
    answer = input("enter no to end the program（yes or no）? ")
    print(make_album(name,song))
    if answer == 'no':
        break

#函数传递列表

#函数中修改列表是永久性的
def change_name(list):
    list[0] = 'jack'

name_list = ['tom','jack','john','mary']
#调用副本不修改列表(切片表示创建副本)
change_name(name_list[:])
print(name_list)

#直接调用
change_name(name_list)
print(name_list)
'''
def make_car(vendor,model,**info):
    car_info = {}
    car_info['vendor'] = vendor
    car_info['model'] = model
    for key,value in info.items():
        car_info[key] = value
    return car_info

car = make_car('Tesla','Y',color='blue',tow_package=True)
print(car)