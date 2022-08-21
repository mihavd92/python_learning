# Написать функцию которая принимает номер месяца и 
# возвращает время к какому времени года относится этот месяц. 
# Для хранения информации о соответствии месяца к времени года 
# использовать словарь, где ключ это месяц а значение 
# список месяцев которые к нему относятся.


def season_name():  
    months_list = {
        'Winter': (12, 1, 2), 
        'Spring': (3, 4, 5), 
        'Summer': (6, 7, 8), 
        'Autumn': (9, 10, 11)
        }
    month = int(input('Enter month number: '))

    for a in months_list:
        if months_list.get(a).count(month):
            return a
        else:
            return 'Error. This month does not exist'

result = season_name()
print(result)


        



    

