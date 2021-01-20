#!/bin/env python3

from scapy.all import *
import scapy.contrib.gtp

from scapy.contrib.gtp import *

pcap = rdpcap("gtp-ping.pcap")
outer_payload_len = 1024
ping_loop_times = 100

for packet in pcap:
    #print(packet[GTP_U_Header][ICMP])
    #packet[GTP_U_Header][ICMP] = pincap[0][ICMP]

    x = packet[Ether]
    x.src = "3c:fd:fe:73:86:50"
    x.dst = "3c:fd:fe:73:82:a0"
    x.type = 0x800
    del x.chksum

    y = packet[IP]
    y.src = "10.100.200.1"
    y.dst = "10.100.200.3"
    y.len = outer_payload_len
    del y.chksum

    u = packet[UDP]
    udp_len = outer_payload_len - 20
    u.len = udp_len
    del u.chksum

    gtp_len = udp_len - 16 # 8 for UDP header and 8 for GTP mandatory header
    packet[GTP_U_Header].length = gtp_len

    w = packet[GTP_U_Header][ICMP]
    del w.chksum

    z = packet[GTP_U_Header][IP]
    z.src = "60.60.0.1"
    z.dst = "192.168.0.1"
    inner_payload_len = gtp_len - 4 # 4 for GTP seq and padding
    z.len = inner_payload_len
    del z.chksum

    payload = ""
    for i in range(inner_payload_len - 20 - 8): # 20 for IP header len & 8 for ICMP header len, rest of it is ICMP Rest of header
        payload += "z"
    packet[GTP_U_Header][ICMP][Raw].load = payload
    #packet[GTP_U_Header][Raw].load = payload
    del packet[Ether].chksum
    del packet[Padding]

    packet.show()
    #wireshark(packet)
    wrpcap("gtp_icmp_echo_request.pcap", packet)

    #send(y)
    #for i in range(100):
    #    wrpcap("gtp_icmp_echo_request_loop.pcap", packet, append=True)
    #send(packet, loop=10)
    #send(packet)
