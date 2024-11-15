sayilar = [1, 3, 5, 6, 7, 3, 2, 34, 567, 9]
isimler = ["aziz", 'burhan', "cafer", "deniz", "ezgi"]
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
sonuc = sayilar.index(5)

# sonuc = sayilar.count(4)
# sonuc = isimler.count('canan')

print(sonuc)

# List methods demo
customers = ["sadik turan", "ahmet yılmaz", "cinar turan", "yigit bilgi"]
order_totals = [12000, 24000, 10000, 8700]
# 1- 'sadikturan' kullanıcı adıyla yapılan 5000 liralık siparişi listeye ekleyiniz.
# customers.append("sadikturan")
order_totals.append(5000)
# 2- Son eklenen siparişi siliniz.
print(order_totals.pop(-1))

# 3- Tüm müşteriler için aşağıdaki özet cümleyi yazdırınız.
# '<username>' isimli müşterinin sipariş toplamı '<10000>' liradır. (döngüler)

# sonuc = f"{customers[0]} isimli müşterinin sipariş toplami {
#     order_totals[0]} tl'dir"
# sonuc = f"{customers[1]} isimli müşterinin sipariş toplami {
#     order_totals[1]} tl'dir"

# 4- Müşterileri alfabetik olarak sıralayınız.
# customers.sort()
print(customers)

# 5- Sipariş toplamlarını azalan şekilde sıralayınız.
order_totals.sort()
order_totals.reverse()
print(order_totals)

# 6- En düşük sipariş hangisidir?
print(min(order_totals))

# 7- 'sadikturan' isimli kullanıcının kaç tane siparişi vardır?
sonuc = customers.count('sadik turan')
print(sonuc)

# 8- Customers listesinden 'ahmetyilmaz' isimli kullanıcıyı siliniz.
customers.remove("ahmet yılmaz")
print(customers)

# 9- Listelerdeki tüm içerikleri siliniz.
# customers.clear()
# order_totals.clear()

# 10- Kullanıcıdan aldığınız kullanıcı adı ve sipariş toplamlarını listeye ekleyiniz.
username = input("müşteri adi : ")
order_total = input("sipariş toplamı : ")
customers.append(username)
order_totals.append(int(order_total))
print(customers)
print(order_totals)
