access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
m = input("Switchport mode(access/trunk): ")
i = input("Interface: ")
v = input("Vlan(s): ")

t = dict(trunk = trunk_template, access = access_template)
print("-" * 33 + "\nInterface" + i)
print("\n".join(t[m]).format(v))
