# isim = input()
# print("Merhaba "+isim)

# 2000 + 2000 * %18
urunAFiyat = 2000
urunBFiyat = 3000
kdvOrani = 0.20
print(urunAFiyat+(urunAFiyat*kdvOrani))
print(urunBFiyat+(urunBFiyat*kdvOrani))

urunToplami = urunAFiyat+urunBFiyat
print(urunToplami+(urunToplami*kdvOrani))

# Değişken tanımlama kuralları
sayi1 = 10
sayi2 = 20
# 3sayi= 30 => değişken isimleri rakam ile başlayamaz
# sayi@= 40 => değişken tanımlamak için sadece _ kullanılabilir
urunFiyati = 5000  # camelCase
urun_fiyati = 4500  # snake_case
yas = 20
YAS = 30  # case sensetive
# prog. dili keywordları kullanılmamalı => True="Aziz"
x = "10"
y = "20"
print(x+y)
x, y, z = 10, 20, 30
x, y, z = 78
