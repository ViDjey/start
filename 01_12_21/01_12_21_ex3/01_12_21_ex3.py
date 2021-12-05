def func_shifr(texts,keys):
    text=''
    try:
        keys=int(keys)
    except ValueError:
        t=0
        for elem in texts:
            c=ord(elem)^ord(keys[t])
            text=text+chr(c)
            if t+1<len(keys):
                t+=1
            else:
                t=0
    else:
        for elem in texts:
            c=ord(elem)^keys
            text=text+chr(c)
    return text    



key=(input("Введите ключ: "))
text=''
with open("file.txt", 'r') as f:
    text=f.read()
obr_text = func_shifr(text, key) 
print(f"\nEncrypted text: {obr_text}")
with open("file.txt", 'w') as file:
    file.write(f"Initial text: {text}")
    file.write(f"\nEncrypted text: {obr_text}")
    file.write(f"\nDecrypted text: {func_shifr(obr_text, key)}")
