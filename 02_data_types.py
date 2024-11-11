# Veri türleri - Data types
# Numeric -int, float 
# Text - string
# Boolean - bool
isim="Ahmet"
yas=27
kilo=78.9
ogrenciMi=True
print(type(isim))         # str
print(type(yas))          # int
print(type(kilo))         # float
print(type(ogrenciMi))    # bool
print("Ad: "+isim+"  yaşı "+str(yas)+" kilosu "+str(kilo)+" öğrencilik durumu "+str(ogrenciMi))

# Veri tipi dönüşümü
sayi1 = int("10")
sayi2 = 10
toplam=sayi1+sayi2
print(toplam)

x=int("10")
# x=int("10.5") #hata
x=float("10")
x=float(10)
x=str(3.4)
x=str(True)

print(type(x))

# Uygulama
''' 
Uygulama 1 : 
Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız
Alan: π¹
Çevre: 2πr

Uygulama 2 : Klavyeden girilen km bilgisini mil cinsinden hesaplayınız
'''

yari_cap= 15
pi=3.141592653589793
alan=pi*(yari_cap**2)
cevre=2*(pi*yari_cap)
print("Verilen dairenin alanı "+str(alan)+" çevresi ise "+str(cevre))

km= int(input("Hesaplanacak Km'yi giriniz : "))
mil = km/1.609344
mil=round(mil,2)
print("Girilen km değeri mil cinsinden {0}".format(mil)+" olacaktır.")
