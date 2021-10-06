num=float(input("Ingrese la cantidad de dinero: "))     #O(1)   O(1)
denominacion=[500,200,100,20,10,5,1,float(0.5)]         #O(1)   O(1)

for i in denominacion:          #O(8)       
    if num >= i:                
        x=num//i                #O(1)
        if num >= 100:
            if x == 1:
                print(f'{int(x)} billete de {i}')
            else:
                print(f'{int(x)} billetes de {i}')
        else:
            if num <= 20 or num>=20:
                if x == 1:
                    print(f'{int(x)} moneda de {i}')
                else:
                    print(f'{int(x)} monedas de {i}')
   
     
    num= num % i        #O(n)       #O(n)
    #print(num)
"""
Memoria O(n+5)    Simplificado O(n)
Procesador O(n+1) Simplificado O(n)
"""


"""
Forma 2
num=float(input("Ingrese la cantidad de dinero: "))

if num >= 500:
    x=num//500
    resta=num - (x*500)
    print(f'{int(x)} billetes de 500')
    num=resta
    #print(num)

if num >= 200:
    x=num//200
    resta=num - (x*200)
    print(f'{int(x)} billetes de 200')
    num=resta
    #print(num)

if num >= 100:
    x=num//100
    resta=num - (x*100)
    print(f'{int(x)} billetes de 100')
    num=resta
    #print(num)

if num >= 20:
    x=num//20
    resta=num - (x*20)
    print(f'{int(x)} monedas de 20')
    num=resta
    #print(num)

if num >= 10:
    x=num//10
    resta=num - (x*10)
    print(f'{int(x)} monedas de 10')
    num=resta
    #print(num)

if num >= 5:
    x=num//5
    resta=num - (x*5)
    print(f'{int(x)} monedas de 5')
    num=resta
    #print(num)

if num >= 1:
    x=num//1
    resta=num - (x*1)
    print(f'{int(x)} monedas de 1')
    num=resta
    #print(num)

if num >= 0.5:
    x=num//0.5
    resta=num - (x*0.5)
    print(f'{x} monedas de 0.5')
    num=resta
    #print(num)"""

