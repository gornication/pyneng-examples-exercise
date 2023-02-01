add = input("IP-adress: ")
add_s = add.split(".")
n = 0

for octet in add_s:
    add_s[n] = int(octet)
    n += 1

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

