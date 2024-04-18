immutable_var = 1,44, 'Валет', False, 'ТУЗЗЗ'
print(immutable_var)
#immutable_var [2] = False
#print(immutable_var) # Питон не даёт мне заменить 3 элемент, так как кортеж - неизменяемый список.
# Внести какие-то поправки в нём нельзя, если только в кортеже нет списка. Вот в нём можно пошаманить:)
# Если я уберу решётку с кодов 3 и 4, то Питон не даст мне продолжить делать задание.
mutable_list = ["Scorpion", 22, "KK", True]
print(mutable_list)
mutable_list[0] = 'Sab-Zero'
mutable_list[1] = 10
mutable_list[2] = 'QQ'
mutable_list[3] = False
print(mutable_list)
