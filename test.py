DP = './Data/dulplicated.feat'
NM = '206.feat'
fd = open(NM, 'r')

line_count = 0
error_count = 0
oh = {'icmp': 0, 'udp': 0, 'tcp': 0}
for line in fd.readlines():
    line_count += 1
    _list = line.split()
    oh[_list[7]] += 1

print(oh)
