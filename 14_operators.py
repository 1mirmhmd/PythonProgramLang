# aritmetik operatorler
a = 9
b = 2

sonuc = a + b
sonuc = a - b
sonuc = a * b
sonuc = a / b
sonuc = a % b
sonuc = a ** b
sonuc = a // b

print(sonuc)

# atama operatorleri
a = 10
b = 20
c = 30

a, b, c = 10, 20, (30, 40)
# d = 10,20

a += 5      # a = a + 5
a -= 5      # a = a - 5
a *= 5      # a = a * 5
a /= 5      # a = a / 5
# a %= 5      # a = a % 5
a **= 5      # a = a ** 5
a //= 5      # a = a ** 5

# print(a,b,c)

# Atama operatorleri uygulama
a, b, c = 4, 8, (12, 2)

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile a,b,c toplamının farkı nedir?

# sayi1 = int(input("sayı 1: "))
# sayi2 = int(input("sayı 2: "))

# carpim = sayi1 * sayi2
# toplam = a + b + (c[0] + c[1])

# sonuc = carpim - toplam

# 2- c' nin b' ye kalansız bölümünü hesaplayınız.

sonuc = (c[0] + c[1]) // b

# 3- (a,b,c) toplamının mod 7' si nedir?
sonuc = (a + b + (c[0] + c[1])) % 7

# 4- b' nin a. kuvvetini hesaplayınız.
sonuc = b ** a

# 5- a, *b, c = (2,4,6,8,13) işlemine göre c' nin küpü nedir?

a, *b, c = (2, 4, 6, 8, 13)
print(c ** 3)

# 6- a, b, *c = (2,4,6,8,13) işlemine göre c' nin değerleri toplamı nedir?

a, b, *c = (2, 4, 6, 8, 13)

# print(c[0] + c[1] + c[2])

# Karşılaştırma operatorleri
a, b, c, d = 2, 2, 10, 5

eposta = "info@sadikturan.com"
parola = "135790"

sonuc = (a == c)
sonuc = (a != c)
sonuc = (a != b)

# sonuc = (eposta == input('eposta: '))
# sonuc = (parola == input('parola: '))

sonuc = (c > a)
sonuc = (a >= b)
sonuc = (a <= b)
sonuc = (a < c)
sonuc = (True == 1)
sonuc = (False == 0)
sonuc = int(True)

print(sonuc)

# 1- Girilen 2 sayıdan hangisi büyüktür?
# sayi1 = int(input("sayı 1:"))
# sayi2 = int(input("sayı 2:"))

# sonuc = (sayi1 > sayi2)
# print(f"{sayi1} {sayi2} den büyük {sonuc}")

# 2- Girilen bir sayının tek çift kontrolünü yapınız.

# sayi = int(input("sayı: "))
# sonuc = (sayi % 2 == 0)
# print(f"sayı çift: {sonuc}")


# 3- Bir öğrencinin girilen 3 notuna göre başarı durumunu kontrol ediniz. 50 ve üstünde başarılı.

not1 = int(input("not 1: "))
not2 = int(input("not 2: "))
not3 = int(input("not 3: "))

ortalama = (not1 + not2 + not3) / 3

print(f"öğrencinin not ortalaması: {
      round(ortalama, 2)}, başarı durumu {ortalama >= 50}")


# mantıksal operatorler

# (yas >= 18) => true, false
# (mezuniyet == 'lise') ya da (mezuniyet == 'üniversite') => true, false
# sonuc = (yas >= 18) ve (mezuniyet == 'lise' ve ya mezuniyet == 'üniversite')

x = 11

sonuc = (x > 5) and (x < 10)

# 1- And
#   True, True => True
#   True, False => False
#   False, False => False

# 2- Or
#   True, True => True
#   True, False, False => True
#   False, False => False

sonuc = (x > 0) and (x % 2 == 0)    # x pozitif çift sayı
sonuc = (x > 0) or (x % 2 == 0)    # x pozitif ya da çift sayı

# 3- Not
# False => True
# True => False
sonuc = not (x > 0)

print(sonuc)

# mantıksal operatorler uygulama
# 1- Yaşı 18' den büyük ya da veli izni varsa bir işte çalışabilir durumunu kontrol ediniz.
veli_izni = False

veli_izni = False
yas = 18
sonuc = (veli_izni) or (yas >= 18)

# 2- Ders notu 50-100 arasındaysa geçti değilse kalsın bilgisini yazdırınız.
dersNotu = 55
sonuc = (dersNotu >= 50 and dersNotu <= 100)
print(f"ders geçme durumu: {sonuc}")

# 3- Not ortalaması en az 70 puan ve zayıfı yoksa teşekkür belgesi alabilme durumunu kontrol ediniz.
ortalama = 75
zayifSayisi = 0
sonuc = (ortalama >= 70) and (zayifSayisi == 0)

# 4- İşe girmek için en az önlisans ya da lisans mezunu olma durumunu kontrol ediniz. Sigara kullanmama koşulu.
egitim = "önlisans"
sigara_icme = False

sonuc = (egitim == "önlisans" or egitim == "lisans") and (not(sigara_icme))

# 5- Uygulamaya giriş kontrolünü "username yada email" ve "parola" için yapalım.

email = "info@sadikturan.com"
username = "sadikturan"
password = "12345"

girilen_bilgi = input("email yada username: ")
girilen_parola = input("parola: ")

sonuc = (email == girilen_bilgi or username == girilen_bilgi) and (password == girilen_parola)

print(sonuc)

# identity

x = [2,4,6]
y = [2,4,6]
z = y

print(x == y)
print(x is y)
print(x is not y)

print(z is y)
print(z is not y)

# membership

print(20 in x)
print(20 not in x)