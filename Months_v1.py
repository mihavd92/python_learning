def season_name():    
    month = int(input('Enter month number: '))
    months_list = {
        1: 'Winter',
        2: 'Spring',
        3: 'Summer',
        4: 'Autumn'}
        
    if month == 1 or month == 2 or month == 12:
        return months_list.get(1)
    elif month == 3 or month == 4 or month == 5:
        return months_list.get(2)
    elif month == 6 or month == 7 or month == 8:
        return months_list.get(3)
    elif month == 10 or month == 11 or month == 12:
        return months_list.get(4)
    else: 
        return('Error. This month does not exist')
   
result = season_name()
print(result)



        



    

