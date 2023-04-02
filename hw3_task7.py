n = input()
a1 = n.find('f')  # первый индекс
a2 = n.rfind('f')  # последний индекс
if a1 == -1:  # если не найдено
    print()
elif a1 == a2:  # если только одна f, индексы совпадут
    print(a1)
else:
    print(a1, a2)
