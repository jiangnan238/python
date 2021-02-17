#导入随机返回一个整数
from random import randint

#创建骰子游戏
class Die():
    #初始化骰子面数
    def __init__(self,sides=6):
        self.sides = sides
    #投骰子
    def roll_die(self):
        print('The dice turned out: '+str(randint(1,self.sides)))
    #改变骰子面数
    def change_sides(self,change_sides):
        self.sides = change_sides
    #选择玩的次数
    def playgame(self,times):
        for nowtimes in range(1,times+1):
            print('%-2d'%nowtimes,':',end=' ')
            self.roll_die()

game = Die()
game.change_sides(10)
game.playgame(10)
#game.change_sides(20)
#game.playgame(10)