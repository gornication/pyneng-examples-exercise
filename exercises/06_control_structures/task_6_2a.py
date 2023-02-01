add = input("IP-adress: ")
add_s = add.split(".")
n = 0
#Convert str to int and check for int
try:
    for octet in add_s:
        add_s[n] = int(octet)
        n += 1
except ValueError:
    print("Incorrect ip-address!")
else:
#check separation by dots into 4 perts and the number falls into the range of the octet of the IP
    if add.count(".") != 3:
        print("Incorrect ip-address!")
    else:
        for oct in add_s:
            if oct not in range(0,256):
                print("Incorrect ip-address!")

#ip-address classification
    if 1 <= add_s[0] <= 223:
        print("unicast")
    elif 224 <= add_s[0] <= 239:
        print("multicast")
    elif add == "255.255.255.255":
        print("local broadcast")
    elif add == "0.0.0.0":
        print("unassigned")
    else:
        print("unused")


# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
