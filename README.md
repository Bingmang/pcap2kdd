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
- num_conn
- startTimet
- orig_pt
- resp_pt
- orig_ht
- resp_ht
- duration
- protocol
- resp_pt
- flag
- src_bytes
- dst_bytes
- land
- wrong_fragment
- urg
- hot
- num_failed_logins
- logged_in
- num_compromised
- root_shell
- su_attempted
- num_root
- num_file_creations
- num_shells
- num_access_files
- num_outbound_cmds
- is_hot_login
- is_guest_login
- count_sec
- srv_count_sec
- serror_rate_sec
- srv_serror_rate_sec
- rerror_rate_sec
- srv_error_rate_sec
- same_srv_rate_sec
- diff_srv_rate_sec
- srv_diff_host_rate_sec
- count_100
- srv_count_100
- same_srv_rate_100
- diff_srv_rate_100
- same_src_port_rate_100
- srv_diff_host_rate_100
- serror_rate_100
- srv_serror_rate_100
- rerror_rate_100
- srv_rerror_rate_100

total 47 features.
