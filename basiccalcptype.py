import numpy as np
from random import randint
from random import seed
from numpy import pi
from functools import reduce

def sum():
    try:
        a = float(input("1st Number : "))
        b = float(input("2nd Number : "))
        return (a+b)
    except ValueError:
        return("Hatalı Girdiniz, Tekrar Deneyin")

def extr():
    try:
        a = float(input("1st Number : "))
        b = float(input("2nd Number : "))
        return(a-b)
    except ValueError:
        return("Hatalı Girdiniz, Tekrar Deneyin")
def mult():
    try:
        a = float(input("1st Number : "))
        b = float(input("2nd Number : "))
        return(a*b)
    except ValueError:
        return("Hatalı Girdiniz, Tekrar Deneyin")
def divd():
    try:
        a = float(input("1st Number : "))
        b = float(input("2nd Number : "))
        return(a/b)
    except ValueError:
        return("Hatalı Girdiniz, Tekrar Deneyin")
    except ZeroDivisionError:
        return("Tanımsız")
def perc():
    try:
        a = float(input("Sayı giriniz : "))
        b = float(input("Yüzde giriniz : "))
        sonuc = ((a*b)/100)
        return sonuc
    except ValueError:
        return("Hatalı Girdiniz, Tekrar Deneyin")
def sn():
    try:
        x = float((input("Kaç derece : ")))
            
        sonuc = np.around(np.sin(np.radians(x)),decimals = 5)
        return sonuc
    except:
        return("Hatalı veri, tekrar deneyin")
def cn():
    try:
        x = float((input("Kaç derece : ")))
            
        sonuc = np.around(np.cos(np.radians(x)),decimals = 5)
        return sonuc
    except:
        return("Hatalı veri, tekrar deneyin")
def tx():
    try:
        x = float(input("Sayı giriniz :"))
        
        if x not in (90,270,-90):
            sonuc = np.round(np.tan(np.radians(x)),1)
            return(sonuc)
        else:
            return("Tanımsız")
    except:
        return("Hatalı işlem, tekrar deneyin")
def cx():
    try:
        x = float(input("Sayı giriniz :"))
        
        if x not in (180,360,-180):
            sonuc = np.round(1/np.tan(np.radians(x)),1)
            return(sonuc)
        else:
            return("Tanımsız")   
    except:
        return("Hatalı işlem, tekrar deneyin")    
def fc():
    try:
        a = int(input("Sayı giriniz : "))
        list1 = []
        for x in range(1,a+1):
            list1.append(x)
        y = reduce(lambda m,n: m*n,list1)
        return y
    except:
        return("Hatalı işlem,tekrar deneyin")
    
    


dict1 = {
    "+" : sum,
    "-" : extr,
    "*" : mult,
    "/" : divd,
    "yüzde" : perc,
    "sinüs" : sn,
    "cosinüs":cn,
    "tanjant" : tx,
    "cotanjant" : cx,
    "faktöriyel":fc
    
    
    
}
def calculator():
    print(" + \n - \n * \n / \n Sinüs \n Cosinüs \n Tanjant \n Cotanjant \n Yüzde \n Faktöriyel")
    user_input = input("İşlem seçiniz : ")


    print(dict1[user_input.lower()]())


while True:
    calculator()
    check = input("Yeniden hesaplamak ister misiniz? Evet ise Y, Hayır ise N'ye tıklayın." + "\n")
    if check.upper() =="Y":
        continue
    print("Hoşçakalın")
    break