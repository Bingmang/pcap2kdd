import sys

if len(sys.argv) > 1:
    fname = sys.argv[1]

SPLIT_SYMBOL = ' '

fd = open(fname, 'r')
# fo = open('kqout', 'w')


pre_address_port = []
features_cache = []
conn_num = -1

for line in fd.readlines():
    features = line.split()
    address_port = features[2:6]
    keep_add_features = features

    # 如果判定为重复的连接, 就累加10、11特征并将其他特征更新到最后状态
    if address_port == pre_address_port and features[7] == 'udp':
        features[0] = conn_num + 1
        features[10] = int(features[10]) + int(features_cache[conn_num][10])
        features[11] = int(features[11]) + int(features_cache[conn_num][11])
        features_cache[conn_num] = features
    # 如果不是重复的连接，则将该行特征写入cache并增加conn_num
    else:
        conn_num += 1
        features[0] = conn_num + 1
        features_cache.append(features)
    # 更新连接信息
    pre_address_port = address_port
# lines = map(lambda features: SPLIT_SYMBOL.join(map(lambda x: str(x), features)) + '\n', features_cache)
add_temp = {}
error_counter = 0
for feat in features_cache:
    ap = ' '.join(feat[2:6])
    if add_temp.get(ap):
        # print(ap)
        error_counter +=1
    else:
        add_temp[ap] = True
print(error_counter)

lines = '\n'.join(map(lambda feat_list: ' '.join(map(lambda x: str(x), feat_list)), features_cache))
lines += '\n'
# fo.write(lines)
fd.close()
# fo.close()
