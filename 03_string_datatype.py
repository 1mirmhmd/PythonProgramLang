kursAdi = "Python ile programlama"
kursAciklamasi="Güzel bir kurs"
kursSuresi="20 Saat"
mesaj="Kurs adı : "+kursAdi+" "+"Kurs açıklaması : "+kursAciklamasi+" "+"Kurs süresi : "+" "+kursSuresi
print(mesaj)
# Metin dizisinin ilk ve son karakterlerine ulaşma
print(mesaj[0],mesaj[-1])

# string slicing
adet=len(kursAdi)
print(kursAdi[adet-1])           #a
print(kursAdi[0:])               #Python ile programlama
print(kursAdi[11:22])            #programlama
print(kursAdi[:6])               #Python
print(kursAdi[11:len(kursAdi)])  #programlama
print(kursAdi[6:])               #ile programlama
print(kursAdi[-11:-1])           #programlam
print(kursAdi[0:20:2])           #Pto l rgal
print(kursAdi[::])               #Python ile programlama
print(kursAdi[::2])              #Pto l rgalm
print(kursAdi[::-1])             #amalmargorp eli nohtyP

# Format string
name = "Hasan"
lname= "Ali"
age = 36
# string concat
user= "Bu kişinin adı :"+name+" "+" \nSoyadı : "+lname+" \nYaşı : "+str(age)
print(user)
print('My name is {} {}'.format(name, lname))
print('My name is {1} {0}'.format(name, lname))
print('My name is {l} {n}'.format(n=name, l=lname))
print("My name is {} {} and I'am {} years old".format(name, lname, '45'))
print("My name is {} {} and I'am {} years old".format(name, lname, age))

result = 200 / 700
print('The result is {}'.format(result))
print('The result is {r:1.3}'.format(r=result))
print(f"My name is {name} {lname} and I'm {age} years old") #<-- asstring






