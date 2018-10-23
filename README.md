# pcap2kddcup

## 1. Requirements

- bro
- python
- gcc
- larger than 2GB memory

## 2. Usage

```bash
gcc trafAld.c -o trafAld.out
mkdir feats
./pcap2kdd.sh your_data.pcap
```

Then it will generate your_data.feat

## 3. Features

For each connection the attributes of .feat file: 
- 0  num_conn
- 1  startTimet
- 2  orig_pt
- 3  resp_pt
- 4  orig_ht
- 5  resp_ht
- 6  duration
- 7  protocol
- 8  resp_pt
- 9  flag
- 10 src_bytes
- 11 dst_bytes
- 12 land
- 13 wrong_fragment
- 14 urg
- 15 count_sec
- 16 srv_count_sec
- 17 serror_rate_sec
- 18 srv_serror_rate_sec
- 19 rerror_rate_sec
- 20 srv_error_rate_sec
- 21 same_srv_rate_sec
- 22 diff_srv_rate_sec
- 23 srv_diff_host_rate_sec
- 24 count_100
- 25 srv_count_100
- 26 same_srv_rate_100
- 27 diff_srv_rate_100
- 28 same_src_port_rate_100
- 29 srv_diff_host_rate_100
- 30 serror_rate_100
- 31 srv_serror_rate_100
- 32 rerror_rate_100
- 33 srv_rerror_rate_100

total 34 features.
