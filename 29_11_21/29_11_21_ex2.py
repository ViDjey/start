def f(*args):
    """Returns summation of arguments
    Keyword arguments:
    Presumably the arguments should be of type int
    Will process other types as well
    """
    S = 0
    for i in range(len(args)):
        try: 
            S += args[i]
        except TypeError:
            print(f"Тип аргумента= {args[i]} не подходит для суммирования")
    return S



print (f'Cумма элементов= {f("djfhj", 35, -45, 0.347, ["kei", "rtiu", 234, "kh]"], {34, 46, 13}, 0)}')
print (f'Cумма элементов= {f()}')
print (f'Cумма элементов= {f(5, -38, 64, 89.11)}')
