import sys
from collections import OrderedDict

if len(sys.argv) > 1:
    fname = sys.argv[1]

SPLIT_SYMBOL = ' '

# remove duplicated row according to ip and port
def scan_file(filepath):
    cache_dict = {}
    cache_array = []
    fd = open(filepath, 'r')
    for line in fd.readlines():
        features = line.split()
        # 15~27 是 kdd 的 10-22 特征 无法提取 都是0
        del features[15:28]
        address_port = features[2:6]
        cache_key = ' '.join(address_port)

        if cache_dict.get(cache_key):
            cache_dict[cache_key] += 1
            continue
        else:
            cache_dict[cache_key] = 1
            cache_array.append(features)

    def cache_filter(x):
        address_port = x[2:6]
        cache_key = ' '.join(address_port)
        return cache_dict[cache_key] == 1

    cache_array = list(filter(cache_filter, cache_array))
    
    conn_num = 0
    for index in range(len(cache_array)):
        conn_num += 1
        cache_array[index][0] = str(conn_num)

    duplicate_count = 0
    duplicate_number = 0
    for key in cache_dict:
        if cache_dict[key] > 1:
            duplicate_count += 1
            duplicate_number += cache_dict[key]
            # print(key, '重复次数:', cache_dict[key])
    print('总共重复次数:', duplicate_count, duplicate_number)
    fo = open('kqout', 'w')
    fo.writelines(map(lambda features: SPLIT_SYMBOL.join(features) + '\n', cache_array))
    fo.close()
    fd.close()

def main():
    scan_file(fname)

if __name__ == '__main__':
    main()
