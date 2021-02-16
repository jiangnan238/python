file_path1 = 'C:/Users/江南/Desktop/python/text_files/guest_name.txt'
file_path2 = 'C:/Users/江南/Desktop/python/text_files/guest_book.txt'
file_path3 = 'C:/Users/江南/Desktop/python/text_files/guest_answer.txt'

#编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写入到文件 guest.txt 中
with open(file_path1,'w+') as file_name:
    guest_name = ''
    while guest_name != 'q':
        guest_name = input("please input your name(input 'q' to end): ")
        file_name.write(guest_name+'\n')

#编写一个 while 循环，提示用户输入其名字，在屏幕上打印一句问候语，并将一条访问记录添加到文件 guest_book.txt
with open(file_path2,'w+') as file_book:
    guest_name = input("please input your name(input 'q' to end): ")
    while guest_name != 'q':
        welcome = 'hello,'+guest_name + ' !'
        print(welcome)
        file_book.write(welcome+'\n')
        guest_name = input("please input your name(input 'q' to end): ")

#编写一个 while 循环，询问用户为何喜欢编程。每当用户输 入一个原因后，都将其添加到一个存储所有原因的文件中
with open(file_path1,'r+') as file_read:
    for name in file_read.readlines():
        name = name.rstrip()#删除空白部分
        while name != 'q':
            with open(file_path3,'a+') as file_answer:
                guest_answer = input(name+",why you like python? ")
                file_answer.write(guest_answer+'\n')
                break