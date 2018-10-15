DP = './Data/dulplicated.feat'
NM = './feats/104.pcap.feat'
fd = open(NM, 'r')



line_count = 0
error_count = 0
for line in fd.readlines():
    line_count += 1
    list = line.split()
    if float(list[30]) > 0.8:
        error_count += 1
        print line,
print(line_count)
print(error_count)