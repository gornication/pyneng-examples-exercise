prefix = input("Enter ip-prefix: ")

addr_list_str = prefix.split("/")[0].split(".")
addr_list = list(map(int, addr_list_str))
print("Network:\n{:<10}{:<10}{:<10}{:<10}".format(*addr_list))
print("{:08b}  {:08b}  {:08b}  {:08b}".format(*addr_list))

m = prefix.split("/")[1]
msb = "1" * int(m) + "0" * (32 - int(m))
mld = int(msb[0:8], 2), int(msb[8:16], 2), int(msb[16:24], 2), int(msb[24:32], 2)

print("\nMask:\n" + "/" + m)
print("{:<10}{:<10}{:<10}{:<10}".format(*mld))
print("{:08b}  {:08b}  {:08b}  {:08b}".format(*mld))
