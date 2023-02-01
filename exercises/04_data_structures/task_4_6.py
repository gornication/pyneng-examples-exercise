ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
template = """
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
"""
route_list = ospf_route.split()
route_list[1] = route_list[1].strip("[]")
route_list[3] = route_list[3].strip(",")
route_list[4] = route_list[4].strip(",")

print(template.format(*route_list))
