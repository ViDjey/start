import random 


size1 = random.randint(1, 10)
size2 = random.randint(1, 10)
mn1 = {random.randint(0, 100)}
mn2 = {random.randint(0, 100)}
for i in range(size1-1):
    mn1.add(random.randint(0, 100))
for i in range(size2-1):
    mn2.add(random.randint(0, 100))
print(f"1 набор случайных чисел от 0 до 100, в случайном количестве от 1 до 10 {mn1}")
print(f"2 набор случайных чисел от 0 до 100, в случайном количестве от 1 до 10 {mn2}")
if mn1.intersection(mn2) == set():
    print("Элементов, которые входят в оба набора нет")
else:
    print(f"Элементы, которые входят в оба набора:{mn1.intersection(mn2)}")
if mn1.difference(mn2) == set():
    print ("Элементов, которые входят только в первое, но не во второе нет")
else:
    print(f"Элементы, которые входят только в первое, но не во второе:{mn1.difference(mn2)}")
if mn2.difference(mn1) == set():
    print ("Элементов, которые входят только во второе, но не в первое нет")
else:
    print(f"Элементы, которые входят только во второе, но не в первое:{mn2.difference(mn1)}")
if mn1.symmetric_difference(mn2) == set():
    print ("Элементов, которые входят только в первое или второе, но не в оба нет")
else:
    print(f"Элементы, которые входят только в первое или второе, но не в оба:{mn1.symmetric_difference(mn2)}")
