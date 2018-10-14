import sys
if len(sys.argv) > 1:
    fname = sys.argv[1]
with open(fname, "r") as f:
    with open("kqout", "w+") as fo:
        for line in f:
            s = str(line)
            list = s.split()
            list.pop(0)
            list.pop(0)
            list.pop(0)
            list.pop(0)
            list.pop(0)
            list.pop(0)
            res = ''
            for s in list:
                res = res + s + ','
            n = len(res) - 1
            fo.write(res[:(n - 1)] + '\n')
    f.close()
    fo.close()
