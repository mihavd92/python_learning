# На фермі є кури, корови та свині. 
# Запросити у користувача кількість кур, свиней, корів 
# та вивести на скільки всього ніг у тварин на фермі/

chicken = int(input('Enter your number of Chickens'))
cow = int(input('Enter your number of Cows'))
pig = int(input('Enter your number of Pigs'))
legs = int(chicken * 2 + cow * 4 + pig * 4)
print('Animals of your farm has '  + str(legs) + ' legs')
