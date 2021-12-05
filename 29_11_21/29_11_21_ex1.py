def func(str):
     fl1=0
     for i in range (len(str)):
         if str[i].isdigit()==1:
             fl1=1
     if len(str)>6 and fl1==1 and str.isdigit()==0 and str.lower().find("password")==-1:
         return True
     else:
         return False

                 
s=input('Введите строку: ')
if func(s):
    print ("Строка похожа на пароль")
else:
    print ("Строка не похожа на пароль")