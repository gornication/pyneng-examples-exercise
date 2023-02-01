while True:
    add = input("IP-adress: ")
    add_s = add.split(".")
    check = True
# if this 'True' survives until 'break' in the 14th line, then the check was successful
    if len(add_s) == 4:
        for octet in add_s:
            if not (octet.isdigit() and int(octet) in range(256)):
                check = False
                break # this 'break' ->
    # moves the script here
    else:
        check = False
    if check:
        break
    print("INCORRECT ip-address!!!\n")

#ip-address classification
if 1 <= int(add_s[0]) <= 223:
    print("unicast")
elif 224 <= int(add_s[0]) <= 239:
    print("multicast")
elif add == "255.255.255.255":
    print("local broadcast")
elif add == "0.0.0.0":
    print("unassigned")
else:
    print("unused")
