sayilar=[1,3,5,6,7,3,2,34,567,9]
isimler=["aziz",'burhan',"cafer","deniz","ezgi"]
print(min(sayilar))
print(min(isimler))
print(max(isimler))
sonuc = max(isimler)
sonuc = max(sayilar)

# ekleme
# sayilar.append(12)
# isimler.append('çınar')

# sayilar.insert(0, 100)
# sayilar.insert(-1, 100)
# sayilar.insert(-3, 100)
# sayilar.insert(len(sayilar), 100)

# silme
# sayilar.pop()
# sayilar.pop(0)
# isimler.remove('canan')

# sıralama
# sayilar.sort()
# isimler.sort()
# sayilar.reverse()

# arama
sonuc = sayilar.index(4)

# sonuc = sayilar.count(4)
# sonuc = isimler.count('canan')

print(sonuc)