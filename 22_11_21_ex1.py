x = 0
y = 0
print('Нужно ввести слово (вверх, вправо, влево, вниз)')
s = (input('Движение в какую сторону: '))
if s == "вверх":
    y += 1
elif s == "вправо":
    x += 1
elif s == "влево":
    x -= 1
elif s == "вниз":
    y -= 1
else:
    print("Ошибка ввода")   
print(f"Конечная позиция: ({x}, {y})")
