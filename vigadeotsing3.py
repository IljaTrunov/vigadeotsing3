from random import *
s=nol=pos=neg=[]
def arvud_loendis():
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>=maxi:
        mini,maxi=vahetus(mini,maxi)
    generaator(n,s,mini,maxi)
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort()
    print("Отсортированный список",s)
    jagamine(s,pos,neg,nol)
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",nol)
    kesk=keskmine(pos)
    lisamine(s,kesk)
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg)
    lisamine(s,kesk)
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")
    s.sort()
    print(s)

def vahetus(a:int,b:int):
    """kui a>b siis vehatame neid
    :param int a: arv mis on suurem kui b
    :param int b: arv mis on väiksem kui a
    :rtype:int,int
    """
    abi=a

def generaator(n:int,loend,a:int,b:int):
    """ 
    :param int n: кол-во цифр
    :param list loend: список в котором цифры
    :param int a: минимальное
    :param int b: максимальное
    """
    for i in range (n):
        loend.append(randint(a,b))
    

def jagamine(loend,p,n,nol):
    """
    :param list loend: список со значениями
    :param list p: позитивные
    :param list n: негативные
    :param list nol: нули
    """
    for el in loend:
        if el>0:
            p.append(el)
        elif el<0:
            n.append(el)
        else:
            nol.append(el)

def keskmine(loend):
    """
    :param list loend: среднее число
    rtype: float
    """
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2)
    return kesk

def lisamine(loend,el:float):
    """
    :param list loend: добавляется значение
    :param float el: элемент который добавится в список
    """
    loend.append(el)
    loend.sort()
