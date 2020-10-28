text=' python '
print(text.title())#首字母大写

print(text.upper())#全部大写


print(text.lower())#全部小写

print(text+"两端空格\n")#加号直接连接字符串

text=text.lstrip()
print(text+"删除开头空格\n")  #\t代表空格  \n代表换行

text=text.rstrip()
print(text+"删除结尾空格\n")  
