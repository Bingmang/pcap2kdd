import sys


if len(sys.argv) > 1:
    fname = sys.argv[1]

with open(fname, 'r') as fd:
    with open('kqout', 'w+') as fo:

        write_buffer = []
        prob_temp = ('0', '0', '000.000.000.000', '000.000.000.000')

        # [0] Keep add
        num_conn_temp = 1
        # [6] Select the last one
        duration_temp = 0
        # [9] udp: last one SF (check SHR/OTH/S0 is whether needed)
        flag_temp = 0
        # [10] Keep add ???
        src_bytes_temp = 0
        # [11] Keep add ???
        dst_bytes_temp = 0
        # [12] Last one. 若连接来自/送达同一个主机/端口则为1，否则为0，离散类型，0或1。
        land_temp = 0
        # [13] Last one. 错误分段的数量，连续类型，范围是 [0, 3] some > 3 ?
        wrong_fragment_temp = 0
        # [15] All 0 !
        hot_temp = 0
        # [16] All 0 !
        num_failed_logins_temp = 0
        # [17] All 0 !
        logged_in_temp = 0
        # [18] All 0 !
        num_compromised_temp = 0
        # [19] All 0 !
        root_shell_temp = 0
        # [20] All 0 !
        su_attempted_temp = 0
        # [21] All 0 !
        num_root_temp = 0
        # [22] All 0 !
        num_file_creations_temp = 0
        # [23] All 0 !
        num_shells_temp = 0
        # [24]
        num_access_files_temp = 0
        # [25]
        num_outbound_cmds_temp = 0
        # [26]
        is_hot_login_temp = 0
        # [27]
        is_guest_login_temp = 0
        # [28] Last one. 过去两秒内，与当前连接具有相同的目标主机的连接数，连续，[0, 511]
        count_sec_temp = 0
        # [29] Last one. 过去两秒内，与当前连接具有相同服务的连接数，连续，[0, 511]
        srv_count_sec_temp = 0
        # [30] Last one. 过去两秒内，在与当前连接具有相同目标主机的连接中，出现“SYN” 错误的连接的百分比，连续，[0.00, 1.00]
        serror_rate_sec_temp = 0
        # [31] Last one
        srv_serror_rate_sec_temp = 0
        # [32]
        rerror_rate_sec_temp = 0
        # [33]
        srv_error_rate_sec_temp = 0
        # [34]
        same_srv_rate_sec_temp = 0
        # [35]
        diff_srv_rate_sec_temp = 0
        # [36]
        srv_diff_host_rate_sec_temp = 0
        # [37] Last one
        count_100_temp = 0
        # [38]
        srv_count_100_temp = 0
        # [39]
        same_srv_rate_100_temp = 0
        # [40]
        diff_srv_rate_100_temp = 0
        # [41]
        same_src_port_rate_100_temp = 0
        # [42]
        srv_diff_host_rate_100_temp = 0
        # [43]
        serror_rate_100_temp = 0
        # [44]
        srv_serror_rate_100_temp = 0
        # [45]
        rerror_rate_100_temp = 0
        # [46]
        srv_rerror_rate_100 = 0

        for line in fd:
            num_conn, startTimet, orig_pt, resp_pt, orig_ht, resp_ht, duration, protocol, resp_pt, flag, src_bytes, dst_bytes, land, wrong_fragment, urg, hot, num_failed_logins, logged_in, num_compromised, root_shell, su_attempted, num_root, num_file_creations, num_shells, num_access_files, num_outbound_cmds, is_hot_login, is_guest_login, count_sec, srv_count_sec, serror_rate_sec, srv_serror_rate_sec, rerror_rate_sec, srv_error_rate_sec, same_srv_rate_sec, diff_srv_rate_sec, srv_diff_host_rate_sec, count_100, srv_count_100, same_srv_rate_100, diff_srv_rate_100, same_src_port_rate_100, srv_diff_host_rate_100, serror_rate_100, srv_serror_rate_100, rerror_rate_100, srv_rerror_rate_100 = line
            if (orig_pt, resp_pt, orig_ht, resp_ht) == prob_temp and protocol == 'udp':
                


        for line in fd:
            s = str(line)
            list = s.split()
            print list
            res = ''
            for s in list:
                res = res + s + ' '
            n = len(res) - 1
            fo.write(res[:(n - 1)] + '\n')
    fd.close()
    fo.close()


def lineParser(input_line):
    num_conn, startTimet, orig_pt, resp_pt, orig_ht, resp_ht, duration, protocol, resp_pt, flag, src_bytes, dst_bytes, land, wrong_fragment, urg, hot, num_failed_logins, logged_in, num_compromised, root_shell, su_attempted, num_root, num_file_creations, num_shells, num_access_files, num_outbound_cmds, is_hot_login, is_guest_login, count_sec, srv_count_sec, serror_rate_sec, srv_serror_rate_sec, rerror_rate_sec, srv_error_rate_sec, same_srv_rate_sec, diff_srv_rate_sec, srv_diff_host_rate_sec, count_100, srv_count_100, same_srv_rate_100, diff_srv_rate_100, same_src_port_rate_100, srv_diff_host_rate_100, serror_rate_100, srv_serror_rate_100, rerror_rate_100, srv_rerror_rate_100 = input_line
