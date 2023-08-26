


# cen_lst = []
# ves_lst = []
# vmest = int(input('Задайте вместимость рюкзака, кг: '))
# n = int(input('Введите количество разных предметов: '))
# k = 1
# while k < n + 1:
#     cen = float(input(f'Ценность {k}-го предмета, руб: '))
#     ves = float(float(input(f'Вес {k}-го предмета, г: ')) / 1000)
#     cen_lst.append(cen)
#     ves_lst.append(ves)
#     k += 1
# print(cen_lst)
# print(ves_lst)

# vmest = int(input('Задайте вместимость рюкзака, кг: '))
# k = 1
# while k < n + 1:
#     cen = float(input(f'Ценность {k}-го предмета, руб: '))
#     ves = float(float(input(f'Вес {k}-го предмета, г: ')) / 1000)
#     cen_lst.append(cen)
#     ves_lst.append(ves)
#     k += 1
# print(cen_lst)
# print(ves_lst)


cen_lst = []
ves_lst = []
with open('ceny_i_vesy.txt', 'r', encoding='utf-8') as f:
    ceny_vesy = f.read()

    # n = int(float(len(ceny_vesy) / 2))
    ceny_vesy = ceny_vesy.split(' ')
    # print(ceny_vesy)

for i in range(len(ceny_vesy)):
    if i % 2 == 0:
        cen_lst.append(float(ceny_vesy[i]))
    else:
        ves_lst.append(float(ceny_vesy[i])/1000)

for i in range(len(cen_lst)):
    print(f'Удельная ценность предмета №{i+1} ценностью {cen_lst[i]}руб и весом {round(ves_lst[i], 4)} кг: {round(cen_lst[i] / (ves_lst[i]), 4)} руб/кг')
print()
# print(cen_lst)
# print(ves_lst)


vmest = float(input('Задайте вместимость рюкзака, кг: '))
cen_str_lst = []
n = len(cen_lst)
k = 1
while k < n + 1:
    a = int(2**(k - 1))
    b = int(2**(n - k))
    str_n = list(('0' * a + '1' * a) * b)
    cen_str_lst.append(str_n)
    # print(str_n)
    del str_n
    k += 1
# print(cen_str_lst)
ves_str_lst = list(cen_str_lst)
# print(ves_str_lst)

good_inds = []
cen_sum = 0
ves_sum = 0
for i in range(2 ** n):
    for j in range(n):
        cen_sum += cen_lst[j] * int(cen_str_lst[j][i])
        ves_sum += ves_lst[j] * int(ves_str_lst[j][i])
    if ves_sum <= vmest:
            good_inds.append(i)
    cen_sum = 0
    ves_sum = 0

# print(good_inds)


cen_sum = 0
ves_sum = 0
max_ves_lst = []
max_cen_lst = []
for i in range(len(good_inds)):
    for j in range(n):
        cen_sum += cen_lst[j] * int(cen_str_lst[j][good_inds[i]])
        ves_sum += ves_lst[j] * int(ves_str_lst[j][good_inds[i]])
    max_cen_lst.append(cen_sum)
    cen_sum = 0
    ves_sum = 0
# print(max_cen_lst)

max_cen_inds = []
for i in range(len(max_cen_lst)):
    if max_cen_lst[i] == max(max_cen_lst):
        max_cen_inds.append(good_inds[i])
# print(max_cen_inds)


nabor = []
nabors = []
for j in range(len(max_cen_inds)):
    for i in range(len(ves_str_lst)):
        # print(ves_str_lst[i][max_cen_inds[j]])
        nabor.append(ves_str_lst[i][max_cen_inds[j]])
    nabors.append(nabor)
    nabor = []
    # print(nabors)
    print()

print()

max_sum_cen = 0
opt_sum_ves = 0
print(f'В рюкзак вместимостью {vmest} кг поместятся следующие наборы предметов:')
print()
for i in range(len(nabors)):
    print(f'Набор №{i+1} содержит:')
    for j in range(len(cen_lst)):
        if int(nabors[i][j]) * cen_lst[j] != 0:
            print(f'{j+1}-й предмет с ценностью {cen_lst[j]} руб и весом {1000*ves_lst[j]} г и с удельной ценностью {round(cen_lst[j]/(1000*ves_lst[j]), 4)} руб/кг')
            max_sum_cen += cen_lst[j]
            opt_sum_ves += ves_lst[j]
    print(f'Максимальная суммарная ценность: {max_sum_cen} руб')
    print(f'При максимальной загрузке рюкзака: {round(opt_sum_ves, 4)} кг')
    print(f'Удельная ценность набора: {round(max_sum_cen / opt_sum_ves, 4)} руб/кг')
    max_sum_cen = 0
    opt_sum_ves = 0
    print()
