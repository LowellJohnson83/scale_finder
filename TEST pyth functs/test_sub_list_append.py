my_lst = []
my_sub_lst = []

for x in range(5):
    a = x + 10
    b = x + 100
    c = [a, b]
    my_sub_lst.append([a, b])
my_lst.append(my_sub_lst)

print(my_lst)