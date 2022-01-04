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
























































using System;

namespace EPICBATTLE
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] heroes = { "Mario", "Chinese woman", "Donkey", "Shrek", "Bomj", "Patrick", "Deadpool", "Garry Snail", "150kg Pudge" };
            string[] villian = { "Kim Jong-Un", "Putin", "Hitler", "Stalin", "Jew", "Hitman", "Street cleaner", "Lenin", "Trevor from gta 5", "your mother" };
            string[] weapon = { "gaming mouse", "wooden chain", "some random motherfucker", "super mega powers", "atom bomb", "universe explosion", "fingers", "fist", "fly","gravity control","your mothers phone","No u", "Uno reverse card" };

            string randomHero = GetRandomcharacter(heroes);
            string randomVillian = GetRandomcharacter(villian);
            string Heroweapon = GetWeapon(weapon);
            string Villianweapon = GetRandomcharacter(weapon);
            Console.WriteLine($"Your random Hero is {randomHero}");
            Console.WriteLine($"Your random Hero weapon is {Heroweapon}");
            Console.WriteLine($"Your random Villian is {randomVillian}");
            Console.WriteLine($"Your random Villian weapon is {Villianweapon}");
        }

        public static string GetRandomcharacter(string[] someArray)
        {
            Random rnd = new Random();
            int randomIndex = rnd.Next(0, someArray.Length);

            return someArray[randomIndex];

        }
         public static string GetWeapon(string[] someArray)
        {
            Random rnd = new Random();
            int randomIndexOne = rnd.Next(0, someArray.Length);

            return someArray[randomIndexOne];

        }


     
    }
}
    a=b
    b=abi
    return a,b

def generaator(n:int,loend:list,a:int,b:int):
    """ генерирует числа от а до b в значении n
    :param int n: количество чисел
    :param int a: минимальное
    :param int b: максимальное
    :param list loend: список сгенерируемых чисел
    """
    for i in range (n):
        loend.append(randint(a,b))
    

def jagamine(loend:list,p:list,n:int,nol:list):
    """сортирует положительные и отрицательные числа
    :param list loend: список всех чисел
    :param list p: положительные
    :param list n: отрицательные
    :param list nol: нули
    """
    for el in loend:
        if el>0:
            p.append(el)
        elif el<0:
            n.append(el)
        else:
            nol.append(el)

def keskmine(loend:list):
    """ищет среднее число
    :param list loend:
    """
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2) #округление до целового числа 
    return kesk

def lisamine(loend:list,el:float):
    """ добавляет число в список
    :param list loend:
    :param el float:
    """
    loend.append(el)
    loend.sort()

arvud_loendis()

