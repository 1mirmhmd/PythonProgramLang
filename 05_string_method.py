mesaj = "btk akademi, python kursu        "
# sonuc=mesaj.upper()
# sonuc=mesaj.lower()
# sonuc=mesaj.title()
# sonuc=mesaj.capitalize()

# sonuc="abc".islower()
# sonuc=mesaj.strip() # string verinin önündeki ve sonundaki boşlukları siler
# string veri içerisindeki kelimeleri boşluklardan dizi şeklinde böler
sonuc = mesaj.split()
# string veri içerisindeki kelimeleri dizi şeklinde belirtilen karakterlerden böler
sonuc = mesaj.split(',')

sonuc = mesaj.index("akademi")
sonuc = mesaj.startswith("a")
sonuc = mesaj.endswith("a")

sonuc = mesaj.replace("python", "javascript")
print(sonuc)

kursAdi = " Btk Akademi Python ile Programlama Dersleri "
website = "https://www.btkakademi.gov.tr"
# 1. 'Btk Akademi' karakter dizisinin baş ve sonundaki boşluk karakterlerini siliniz
print(kursAdi.strip())
# 2. kursAdideğişkeninden tüm karakterleri küçük harfe çeviriniz
print(kursAdi.lower())
# 3. website değişkeninde kaç tane '.' karakteri vardır?
print(website.count('.'))
# 4. website değişkeni 'https' ile mi başlıyor?
print(website.startswith('https'))
# 5. website değişkeni 'tr'ile mi bitiyor?
print(website.endswith('tr'))
# 6. kursAdi değişkenindeki tüm karakterler harflerden mi oluşuyor?
print(kursAdi.isalpha())
# 7. kursAdi değişkenindeki tüm boşlukları '_' ile değiştiriniz.
print(kursAdi.replace(" ", "_"))
# 8. kursAdi değişkenindeki Python kelimesini ReactJS ile değiştiriniz
print(kursAdi.replace("Python", "ReactJS"))
# 9. website değişkeni 'www' içeriyor mu?
print(website.index('www'))
# 10. kursAdi değişkenini listeye çeviriniz
print(kursAdi.split())