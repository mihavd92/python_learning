# Клієнт замовляє каву у кафе. За кожні 6 чашок, 1 чашка дається у якості бонусу.
# Запросити у користувача кількість чашок на покупку та вирахувати кількість бонусних чашок.

prompt = input('Enter the number of cups of coffee')
cups = int(prompt)
bonusCups = int(cups / 6)
print('Client will receive ' + str(cups) + ' cups of coffee and ' + str(bonusCups) + ' bonus coffee.')
