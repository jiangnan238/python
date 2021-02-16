#请写一支 Python 程序，能读取两个整数，并把他们的四则运算印出来。(提示: 用 input()印出来的东西是字符串, 记得转型噢!)
a = int (input("please input number1:"))
b = int (input("please input number2:"))
print("example one:  ",a+b,a-b,a*b,a/b)
#第一步让用户输入想要做的符号运算，比如「+, -, *, /」，第二步让使用者输入’整数1’和 ‘整数2’，最后让这两个整数进行运 算。如果输入的运算符号不是「+, -, *, /」，便输出「错误」。
symbol = input("please input symbol(+ - * /):")
num1 = int(input("please input number1:"))
num2 = int(input("please input number2:"))
if symbol == '+':
    print("example two:",num1+num2)
elif symbol == '-':
    print("example two:",num1-num2)
elif symbol == '*':
    print("example two:",num1*num2)
elif symbol == '/':
    print("example two:",num1/num2)
else:
    print("input error!")