my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4)
print(type(my_list))  # değiştirilebilir
print(type(my_tuple))  # değiştirilemez
my_list[0] = 2
# my_tuple[0] = 2

my_list.append(3)
sonuc = my_tuple.count(1)

my_tuple2 = tuple([2, 3, 4])
my_list2 = list((2, 3, 4))

print(type(my_tuple2))
print(type(my_list2))
