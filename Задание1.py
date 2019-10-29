print('-----Задание 1-----')
def visocos_func (a):
    """Функция определения високосного года"""
    if a%4!=0 or (a%100==0 and a%400!=0):
        return('Обычный')
    else:
        return ('Високосный год') 
print(visocos_func(2344))