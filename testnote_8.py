#用户输入填充字典
vocations  = {}

end = 1
while end:
    name = input(" what's your name? ")
    place = input("If you could visit one place in the world, where would you go? ")
    vocations[name] = place
    answer = input("Would you like to let another person respond? (yes/ no)  ")
    if answer == 'no':
        end = 0
    
print("\n----results----")
for name,place in vocations.items():
    print(name+" want go to "+place+" . ")
print(vocations)