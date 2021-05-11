# test-packet
1. Please put "test-packet" dir under $HOME dir
2. Assume "MoonGen" dir  is under $HOME dir
3. Modify Line#9 pcap with the absolute path of "gtp-ping.pcap" file in "test-packet"(in both "gtp_packet.py" and "icmp_packet.py")
4. put "sendpacket" folder under "MoonGen" dir

## Usage
* go to "sendpacket" under "MoonGen"
* send packet with loop "bash sendicmppacket.sh(sendpacket.sh) [packet size] l". ex. "bash sendicmppacket.sh 68 l"
* send just one packet "bash sendicmppacket.sh(sendpacket.sh) [packet size] s". ex. "bash sendicmppacket.sh 68 s"

