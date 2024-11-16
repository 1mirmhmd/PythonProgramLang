# Bir aracın yakıt tipine göre (benzin,dizel,lpg) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulamayı yapınız.
# benzin    : 39.35
# dizel     : 41.71
# lpg       : 20.28
'''
benzin, lpg, dizel = 39.35, 20.28, 41.71
toplamYakitUcreti = 0
aracinGidecegiMesafe = float(input("Aracın gideceği mesafeyi giriniz : "))
andtalamaYakitTuketimi = float(
    input("100 km'de andtalama tüketilen yakıt miktarı : "))
yakitTipi = input("Yakıt tipini yazınız : ")
toplamTuketilenMiktar = aracinGidecegiMesafe*(andtalamaYakitTuketimi/100)
if (yakitTipi == "benzin"):
    toplamYakitUcreti = benzin*toplamTuketilenMiktar
elif (yakitTipi == "lpg"):
    toplamYakitUcreti = lpg*toplamTuketilenMiktar
elif (yakitTipi == "dizel"):
    toplamYakitUcreti = dizel*toplamTuketilenMiktar
else:
    print("Yanlış yakıt tipi")
if (toplamYakitUcreti != 0):
    print(round(toplamYakitUcreti, 2))'''

# Bir öğrencinin 2 yazılı bir sözlü notunu alarak andtalama hesaplayınız ve hesaplanan andtalamaya göre not aralığına karşılık gelen değerlendirmeyi yazdırınız.

#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

yaziliNot1 = float(input("Yazılı 1 sınavda alınan not : "))
yaziliNot2 = float(input("Yazılı 2  sınavda alınan not : "))
proje = float(input("proje sınavda alınan not : "))

notandtalama = (yaziliNot1+yaziliNot2+proje)/3
if (notandtalama >= 0 and notandtalama <= 24):
    print("Aldığınız puan 0'dır!")
elif (notandtalama >= 25 and notandtalama <= 40):
    print("Aldığınız puan 1'dir!")
elif (notandtalama >= 45 and notandtalama <= 54):
    print("Aldığınız puan 2'dir!")
elif (notandtalama >= 55 and notandtalama <= 69):
    print("Aldığınız puan 3'tur!")
elif (notandtalama >= 70 and notandtalama <= 84):
    print("Aldığınız puan 4'tür!")
elif (notandtalama >= 85 and notandtalama <= 100):
    print("Aldığınız puan 5'tir!")
else:
    print("Yanlış not bilgisi")
