# Програма має запросити у користувача значення з хвилинами 
# і вивести у яку чверть години попадає це число. 
# При вводі невалідного значення програма має вивести повідомлення про помилку.

minutes = int(input('Enter value of minutes'))

if minutes >= 1 and minutes < 15:
    print('I quarter')
elif minutes >= 15 and minutes < 30:
    print('II quarter')
elif minutes >= 30 and minutes < 45:
    print('III quarter')
elif minutes >= 45 and minutes < 60:
    print('IV quarter')
else:
    print('Error!!!')
