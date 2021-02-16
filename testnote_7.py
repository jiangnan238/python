'''
aliens = [] # 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'} 
    aliens.append(new_alien)
# 显示前五个外星人
for alien in aliens[:5]: 
    print(alien)
print("...") 
# 显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))
'''
#字典内嵌字典

#创建一个city字典
citys = {
	'shanghai':{
		'country':'china',
		'population':'9999',
		'fact':'9898'
		},
	'niuyue':{
		'country':'america',
		'population':'8888',
		'fact':'7777'
		},
	'lundun':{
		'country':'england',
		'population':'6666',
		'fact':'5555'
		}
}
#遍历打印

for city,city_info in citys.items():
    print(city_info['population']+' people in '+city+'. In fact , only '+city_info['fact']+' people.')