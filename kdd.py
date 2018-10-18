import sys

if len(sys.argv) > 1:
    fname = sys.argv[1]

SPLIT_SYMBOL = ' '

# remove duplicated row according to ip and port
def removeDuplicated(filepath):
    conn_num = 0
    cache_dict = {}
    cache_array = []
    fd = open(filepath, 'r')
    for line in fd.readlines():
        features = line.split()
        if features[7] == 'icmp':
            continue
        features[0] = str(conn_num) # TODO convert to int
        address_port = features[2:6]
        cache_key = ' '.join(address_port)
        if cache_dict.get(cache_key):
            cache_dict[cache_key] += 1
        else:
            cache_dict[cache_key] = 1
            cache_array.append(features)
            conn_num += 1
    fo = open('kqout', 'w')
    fo.writelines(map(lambda features: SPLIT_SYMBOL.join(features) + '\n', cache_array))
    fo.close()
    fd.close()

def main():
    removeDuplicated(fname)

if __name__ == '__main__':
    main()
