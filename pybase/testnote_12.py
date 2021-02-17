file_path = 'C:/Users/江南/Desktop/python/text_files/pi.txt'
#直接输出文件内容
with open(file_path) as file_object:
    contests = file_object.read()
    print(contests)

#文件内容逐行读取
with open(file_path) as file_object:
    file_lines = file_object.readlines()
    print(file_lines)#每行作为列表的一个元素
    message = ''   
    for line in file_lines:
        message = message + line.rstrip()
    print(message)
    message = message.replace('420','Dog')
    print(message) 
    #file_line = file_object.readline()
    #print(file_line)#读取首行，可限制显示字符数量