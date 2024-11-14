kurum = "BTK AKADEMİ".split()  # str to list
print(type(kurum))
print(kurum[0])
print(kurum[1])

sayilar = [1,2,3,4,5]
isimler = ["ali","ahmet","ayşe"]

print(type(sayilar))
print(type(sayilar[0]))

print(type(isimler))
print(type(isimler[0]))

ogrenci = ["Çınar","Turan",60,50,70]

print(ogrenci[0] + " " +ogrenci[1])
ortalama = (ogrenci[2] + ogrenci[3] + ogrenci[4]) / 3
print(ortalama)

ogrenciler = [["Çınar","Turan",60,50,70], ["Ali","Turan",80,50,70]]

print(ogrenciler[0][0])
print(ogrenciler[1][0])

# Liste tanımlama

programlama_diller = ["Python","C#","Java","Javascript"]

sonuc = programlama_diller
sonuc = type(programlama_diller)
sonuc = programlama_diller[0:2]
sonuc = programlama_diller[:2]
sonuc = programlama_diller[:]
sonuc = programlama_diller[-3:-1]
sonuc = programlama_diller[-3:]

# güncelleme
programlama_diller[-1] = "Php"

sonuc = programlama_diller
sonuc = len(programlama_diller)
sonuc = programlama_diller + ["Go","Delphi"]

sonuc = "Python" in programlama_diller
sonuc = "React" in programlama_diller       # koşul ifadeleri

del programlama_diller[0]

for dil in programlama_diller:
    print(dil)


# print(sonuc)