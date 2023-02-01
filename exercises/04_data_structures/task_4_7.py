mac = "AAAA:BBBB:CCCC"
mac1 = mac.replace(":", "")

mac_dec = int(mac1,16)
mac_bin = bin(mac_dec).replace("0b", "")
print(mac_bin)
