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
# x, y, z = 78

# Uygulama
''' Aşağıdaki müşterinin bilgilerini ve satın aldığı ürün bilgilerini değişkenler içerisinde saklaynız
    Toplam ödenen ücret nedir?
    Ödeme miktarının kdv oranı nedir?

    Sadık Turan
    05531234567
    info@sadikt@mail.com
    Kocaeli

    Satın alınan ürünler
    Ürün adı:Kablosuz mouse
    Fiyat: 550TL

    Ürün adı:Kablosuz klavye
    Fiyat: 650TL

    Ürün adı:Dizüstü bilgisayar
    Fiyat: 55550TL
'''

musteri = input("Adınızı girin : ")
tel_no = input("Telefon numarasını girin : ")
mail=input("Mail adresini girin : ")
adres = input("Adresinizi girin : ")
kabl_kul = 550+(550*0.18)
kabl_ms = 650+(650*0.18)
diz_bil=55550+(55550*0.18)
urun_toplam=kabl_kul+kabl_ms+diz_bil
print(f"Sayın {musteri}, {adres} konumlu adresinize, satın alınan ürünler gönderilecektir. Lütfen {tel_no} numaranızı kontrol ediniz. Ödenecek toplam miktar {urun_toplam}TL'dir")



