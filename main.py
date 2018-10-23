import os
import sys
import time
import multiprocessing

if len(sys.argv) > 1:
    dir_name = sys.argv[1]

if not os.path.exists('./Kdd'):
    print('main.py - Creating directory: Kdd ...')
    os.makedirs('./Kdd')
    print('main.py - Done.')


def get_pcap_files(directory):
    res = []
    for root, _, files in os.walk(directory):
        for name in files:
            res.append(os.path.join(root, name))
    return list(filter(lambda x: x.endswith('.pcap'), res))


def pcap_to_kdd(pcap_file):
    pipeline = os.popen('./pcap2kdd.sh %s' % pcap_file)
    print(pipeline.read())


def main():
    print(
        'main.py - Creating process pool with [%d] cpus ...' % multiprocessing.cpu_count())
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    print('main.py - Done.')
    print('main.py - Starting process ...')
    for pcap_file in get_pcap_files(dir_name):
        pool.apply_async(pcap_to_kdd, (pcap_file, ))
    pool.close()
    pool.join()
    print('main.py - Pool - Done')


if __name__ == '__main__':
    main()
