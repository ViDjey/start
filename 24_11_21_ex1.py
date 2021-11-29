N=int(input("Ведите размер массива для сортировки: "))
while N<=0:
    print("Введен неверный размер для массива")
    N=int(input("Ведите размер массива для сортировки: "))
a = []
for i in range(N):
    print(f"Введите элемент массива {i+1}: ")
    a.append(int(input()))
for i in range(1,len(a)):
    for j in range(len(a)-1,i-1,-1):
        if a[j]<a[j-1]:
            a[j],a[j-1]=a[j-1],a[j]
print("Отсортированный масив")
for i in range(len(a)):
    print(a[i])
