def func(kol):
    """Algorithm for finding recursively a number from the Fibonacci series, under the number 'kol'
    Keyword argument:
    kol-type int, positive
    """
    if kol==1 or kol==2:
        return 1
    else:
        return func(kol-1) + func(kol-2)


tmp=True
while tmp:
    try:
        N = int(input("Введите нужный номер элемента ряда Фибоначчи: "))
    except ValueError:
        print("Номер должен быть натуральное")
    else:
        tmp = False
        if (N <= 0):
            print("Номен должен быть положительный")
            tmp = True
print(f"Число Фибоначчи под номером {N}: {func(N)}")

