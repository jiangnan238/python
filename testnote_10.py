#创建类
class restaurant():
    #定义初始化方法
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_eat = 666
    
    #定义方法
    def describe_restaurant(self):
        print("The restaurant name is "+self.restaurant_name +".")
        print("The restaurant cuisine type is "+self.cuisine_type +".")

    def open_restaurant(self):
        print(self.restaurant_name+" is opening.")
    
    def number_served(self):
        print(self.number_eat," people eat in "+self.restaurant_name+'.')
    
    def set_number_served(self,numbers):
        if numbers >= self.number_eat:
            self.number_eat =str(numbers)
        else:
            print("you can't decrement numbers.")

'''
#调用类
KFC = restaurant('KFC','hamburg')

#调用方法
KFC.open_restaurant()
KFC.describe_restaurant()
KFC.number_served()
KFC.set_number_served(0)
KFC.set_number_served(888)
KFC.number_served()
'''
#继承
class fast_reataurant(restaurant):
    #初始化父类
    def __init__(self,restaurant_name,cuisine_type):
        #初始化子类
        super().__init__(restaurant_name,cuisine_type)
        self.cook_time = 5
    #定义自己独有方法
    def fast_cook_time(self):
        print('we cook just '+str(self.cook_time)+' min.')

KFC = fast_reataurant('KFC','cook')
KFC.fast_cook_time()