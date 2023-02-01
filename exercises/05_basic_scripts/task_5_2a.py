prefix = input("Enter ip-prefix: ")

m = prefix.split("/")[1]
msb = "1" * int(m) + "0" * (32 - int(m))
mld = int(msb[0:8], 2), int(msb[8:16], 2), int(msb[16:24], 2), int(msb[24:32], 2)

addr_list_str = prefix.split("/")[0].split(".")
addr_list_int = list(map(int, addr_list_str))
addr_sb = "{:08b}{:08b}{:08b}{:08b}".format(*addr_list_int)[0:int(m)] + "0" * (32 - int(m))
addr_bo = addr_sb[0:8] + "  " + addr_sb[8:16] + "  " + addr_sb[16:24] + "  " + addr_sb[24:32]
addr_li = [int(addr_sb[0:8], 2), int(addr_sb[8:16], 2),int(addr_sb[16:24], 2), int(addr_sb[24:32], 2)]

print("Network:\n{:<10}{:<10}{:<10}{:<10}".format(*addr_li))
print(addr_bo)

print("\nMask:\n" + "/" + m)
print("{:<10}{:<10}{:<10}{:<10}".format(*mld))
print("{:08b}  {:08b}  {:08b}  {:08b}".format(*mld))
