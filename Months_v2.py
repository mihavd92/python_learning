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


        



    

