print('-----Задание 2-----')
a=[1, 2, 3, 4, 5, 6, 7]
def func_mass (a):
    """Функция, которая перемножает все элементы входного массива, подающегося на вход в качестве аргумента"""
    b=1
    for i in range(1, len(a), 1):
        
        b = b*a[i]
        return b
tap=func_mass(a)
print(tap)
