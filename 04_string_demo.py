title = "Python ile Programlama Dersleri"
# 1. 'title' değişkeni içerisindeki karakter sayısı nedir?
# 2. 'title' içerisindeki 'python' kelimesini alın
# 3. 'title' değikeninin ilk 5 ve son 5 karakterini alın
# 4. 'title' değişkenini tersten yazıdırın
# 5. Klavyeden girilen öğrenci bilgisine göre örnek verilen cümleyi yazdırın.
# Örnek: Çınar Turan isimli öğrencinin 1. notu 60, 2. notu 60 ve not ortalaması 60 olarak hesaplanmıştır.

print(len(title))
print(title[:6])
print(title[:5], title[-5:])
print(title[::-1])

isim = input("Öğrenci adını giriniz : ")
soyisim = input("Öğrenci soyadını giriniz :")
not1 = int(input("Öğrencinin 1. notunu giriniz : "))
not2 = int(input("Öğrencinin 2. notunu giriniz : "))


def hesapla(not1,not2):
    return (not1*0.4)+(not2*0.6)
print(f"{isim} {soyisim} isimli öğrencinin 1. notu {not1}, 2. notu {not2} ve not ortalaması {hesapla(not1,not2)} olarak hesaplanmıştır.")
