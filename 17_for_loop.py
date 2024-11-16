
# for => list
# while => koşullu

sayilar = [1,2,3,4,6,8,91,21]
isimler = ["Ali","Canan","Zeynep"]
adsoyad = "Sadık Turan"

# for x in sayilar:
#     print(x)
    
# for x in sayilar:
#     print("Merhaba BTK Akademi")

# for isim in isimler:
#     print(isim)   

# for i in adsoyad:
#     print(i)

my_tuple = [(1,2),(3,4),(5,6)]

# for a,b in my_tuple:
#     print(a,b)

my_dict = {"41":"Kocaeli","53":"Rize","35":"İzmir"}

# for x in my_dict:
#     print(my_dict[x])

for x in my_dict.values():
    print(x)

for x in my_dict.keys():
    print(x)

for x,y in my_dict.items():
    print(x,y)

# uygulama
sayilar = [3,5,7,2,12,32,45]

# 1- "sayilar" listesindeki her bir elemanı yazdırınız.
for sayi in sayilar:
    print(sayi)
# 2- "sayilar" listesinde hangi sayılar 3' ün katıdır?
for sayi in sayilar:
    if(sayi%3==0):
        print(sayi)
# 3- "sayilar" listesinde tüm sayıların toplamı nedir?
toplam=0
for sayi in sayilar:
    toplam+=sayi
print(toplam)

urunler = ["iphone 13","samsung s24","samsung s22","iphone 15","iphone 14"]
# 4- "urunler" listesindeki tüm iphone marka ürünleri listeleyiniz. (find, index)
for urun in urunler:
    if(urun.startswith("iphone")):
        print(urun)
# yada (find, index)
# for urun in urunler:
#     index = urun.find('iphone')
#     if index > -1:
#         print(urun)

# 5- "urunler" listesinde kaç adet samsung ürünü vardır?
sayisi=0
for urun in urunler:
    index = urun.find('samsung')
    if index > -1:
        sayisi+=1
print(sayisi)