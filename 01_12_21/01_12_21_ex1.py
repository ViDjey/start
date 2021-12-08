def func1():
    """Converts a list of strings to a byte representation for 'list'"""
    for i in range(len(list)):
        list[i] = list[i].encode('utf-8')
def func2():
    """Converts a list of byte representations of strings to a list of strings for 'list'"""
    for i in range(len(list)):
        list[i] = list[i].decode('utf-8')       
def func3():
    """Converts a list of strings to byte codes for a 'list'"""
    list2 = []
    for elem in list:
        list3 = []
        for i in range(len(elem)):
            list3.append(ord(elem[i]))
        list2.append(list3)
    return list2
def func4():
    """Converts a list of byte-code strings to a list of strings for the 'list'"""
    list2 = []
    for elem in list:
        strs = ""
        for i in range(len(elem)):
            strs += chr(elem[i])
        list2.append(strs)
    return list2


tmp = True
while tmp:
    try:
        N = int(input("Введите количество строк: "))
    except ValueError:
        print("Количество должно быть натуральным числом")
    else:
        tmp = False
        if N <= 0:
            print("Количество должно быть положительное")
            tmp = True
list = []
for i in range(N):
    s = input('Введите строки: ')
    list.append(s)
func1()
print(f"Преобразованный список строк в байты: {list}")
func2()
print(f"Преобразованный список из байт в строки: {list}")
list = func3()
print(f"Преобразованный список строк в байт-коды: {list}")
list = func4()
print(f"Преобразованный список из байт-кодов в строки: {list}")
