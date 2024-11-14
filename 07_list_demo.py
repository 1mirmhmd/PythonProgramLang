import math 
# 1- "Toyota, Bmw, Renault, Mercedes" elemanlarına sahip markalar isimli bir liste oluşturunuz.
markalar = ["Toyota", "Bmw", "Renault", "Mercedes"]
# 2- Liste kaç elemanlıdır?
print(len(markalar))
# 3- Listenin ilk ve son elemanı nedir?
print(markalar[0], markalar[-1])
# 4- "Renault" markasını "Togg" ile güncelleyiniz.
sonuc = markalar[2] = "Togg"
print(markalar)
# 5- "Togg" listenin bir elemanı mıdır?
print(markalar.index("Togg"))
sonuc = "Togg" in markalar
sonuc = "Togg" not in markalar
print(sonuc)
# 6- Listenin ilk 2 elemanını alınız.
print(markalar[:2])
# 7- Listenin sonuna "Ford" ve "Citroen" markalarını ekleyiniz.
sonuc = markalar+["Ford", "Citroen"]
print(sonuc)

# 8- Listenin son elemanını siliniz.
del sonuc[-1]
print(sonuc)
# 9- Aşağıdaki verileri liste içerisinde saklayınız.

# öğrenci1: Yiğit Bilgi 2010 [70,80,90]
# öğrenci2: Ada Bilgi   2011 [70,70,80]
# öğrenci3: Çınar Turan 2017 [60,60,90]
ogrenciler = [["Yiğit", "Bilgi", 2010, [70, 80, 90]], [
    "Ada", "Bilgi", 2011, [70, 70, 80]], ["Çınar", "Turan", 2017, [60, 60, 90]]]
# 10- Öğrencilerin yaşlarını hesaplayınız.
yasYigit=2024-ogrenciler[0][2]
yasAda=2024-ogrenciler[1][2]
yasCinar=2024-ogrenciler[2][2]
print(yasYigit,yasAda,yasCinar)

# 11- Öğrencilerin not ortalamalarını hesaplayınız.
notortYigit=(ogrenciler[0][3][0]+ogrenciler[0][3][1]+ogrenciler[0][3][2])/3
notortAda=(ogrenciler[1][3][0]+ogrenciler[1][3][1]+ogrenciler[1][3][2])/3
notortCinar=(ogrenciler[2][3][0]+ogrenciler[2][3][1]+ogrenciler[2][3][2])/3
print(notortYigit, int(notortAda), int(notortCinar))