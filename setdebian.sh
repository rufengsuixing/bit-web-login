sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
sudo cat > /etc/apt/sources.list <<eof
deb http://mirrors.163.com/debian/ stretch main non-free contrib
deb http://mirrors.163.com/debian/ stretch-updates main non-free contrib
deb http://mirrors.163.com/debian/ stretch-backports main non-free contrib
deb-src http://mirrors.163.com/debian/ stretch main non-free contrib
deb-src http://mirrors.163.com/debian/ stretch-updates main non-free contrib
deb-src http://mirrors.163.com/debian/ stretch-backports main non-free contrib
deb http://mirrors.163.com/debian-security/ stretch/updates main non-free contrib
deb-src http://mirrors.163.com/debian-security/ stretch/updates main non-free contrib
eof
sudo apt-get update
sudo apt-get install libssl1.0
sudo chmod 777 /var/log
sudo chmod 777 /var/run
sudo wget --no-check-certificate https://github.com/pymumu/smartdns/releases/download/Release23/smartdns.1.2019.04.02-0832.x86_64.tar.gz
tar -zxvf smartdns.1.2019.03.15-2307.x86_64.tar.gz
rm smartdns.1.2019.03.15-2307.x86_64.tar.gz
cd smartdns/etc/smartdns
mv smartdns.conf smartdns.conf.bak
cat >smartdns.conf <<eof
bind [::]:53
cache-size 512
prefetch-domain yes
dualstack-ip-selection yes
rr-ttl-min 120
log-level error
server 10.0.0.10
server 10.0.0.9
server 211.157.15.189
server 210.22.84.3
server 203.240.193.11
server-tcp 8.8.8.8
server-tcp 114.114.114.114
server-tcp 119.29.29.29
eof
cd /usr/lib/x86_64-linux-gnu
ln -s ./libssl.so.1.0.2 ./libssl.so.1.0.0
ln -s ./libcrypto.so.1.0.2 ./libcrypto.so.1.0.0
