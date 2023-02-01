ip = "192.168.3.1"

ip_list = ip.split(".")
ip_list[0] = int(ip_list[0])
ip_list[1] = int(ip_list[1])
ip_list[2] = int(ip_list[2])
ip_list[3] = int(ip_list[3])
print("{:<10}{:<10}{:<10}{:<10}".format(ip_list[0], ip_list[1], ip_list[2], ip_list[3]))
print("{:08b}  {:08b}  {:08b}  {:08b}".format(ip_list[0], ip_list[1], ip_list[2], ip_list[3]))