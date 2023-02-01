import sys
def is_octet_correct(oct) -> bool:
    if (oct.isdigit() and int(oct) in range(256)):
        return True
    return False

add = sys.argv[1]
add_s = add.split(".")
ip_correct = True

if len(add_s) != 4:
    ip_correct = False
else:
    for octet in add_s:
        if not is_octet_correct(octet):
            ip_correct = False
            break

if not ip_correct:
    print("INCORRECT ip-address!!!\n")
    exit(AttributeError)
else:
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
exit(0)