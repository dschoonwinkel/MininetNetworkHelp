#! /bin/bash

addr="127.0.0.1"

#/home/daniel/Development/ITGTrafficGen/bin/ITGSend -T UDP -a 10.0.0.2 -rp 10002 -C 100 -c 1000000 -t 20000 -x receiver.log -l sender.log -Sda 10.0.0.2 -Sdp 11234

#/home/daniel/Development/ITGTrafficGen/bin/ITGSend -T UDP -a $addr -rp 10002 -C 100 -c 10 -t 20000 -x receiver.log -l sender.log -Sda 10.0.0.2 -Sdp 11234
ITGSend -T UDP -a $addr -rp 10002 -C 1 -c 1200 -t 2000 -x receiver12.log -l sender12.log -Sda 10.0.0.2 -Sdp 11234
#/home/daniel/Development/ITGTrafficGen/bin/ITGSend -T UDP -a 127.0.0.1 -rp 10002 -C 100 -c 20 -t 20000 -x receiver.log -l sender.log -Sda 10.0.0.2 -Sdp 11234
#/home/daniel/Development/ITGTrafficGen/bin/ITGSend -T UDP -a 127.0.0.1 -rp 10002 -C 200 -c 20 -z 200 -x receiver.log -l sender.log -Sda 10.0.0.2 -Sdp 11234





