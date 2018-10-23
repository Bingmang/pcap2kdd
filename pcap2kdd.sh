#!/bin/bash
bro -r $1 darpa2gurekddcup.bro > conn.list
sort -n conn.list > conn_sort.list
./trafAld.out conn_sort.list
python3 kdd.py trafAld.list
mv kqout "Kdd/${1##*/}.txt"
echo "pcap2kdd.sh - ${1##*/} - Done."
