'''
print("Give me two numbers, and I'll divide them.") 
print("Enter 'q' to quit.")
while True: 
    first_number = input("\nFirst number: ") 
    if first_number == 'q': 
        break
    second_number = input("Second number: ") 
    try: 
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError: 
        print("You can't divide by 0!")
    else: print(answer)
'''
file_path1 = 'C:/Users/江南/Desktop/python/text_files/dog.txt'
file_path2 = 'C:/Users/江南/Desktop/python/text_files/cat.txt'
def Read_name(filename):
    try:
        with open(filename,'r+') as readname:
            name_lines = readname.readlines()      
    except FileNotFoundError:
        #print("There is no animal！")
        pass
    else:
        for animal in name_lines:
                print(animal,end='')
        print(end='\n')

Read_name(file_path1)
Read_name(file_path2)