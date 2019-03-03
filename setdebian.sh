sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
sudo cat > /etc/apt/sources.list <<eof
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ stretch main contrib non-free
deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ stretch main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ stretch-updates main contrib non-free
deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ stretch-updates main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ stretch-backports main contrib non-free
deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ stretch-backports main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian-security stretch/updates main contrib non-free
deb-src https://mirrors.tuna.tsinghua.edu.cn/debian-security stretch/updates main contrib non-free
eof
sudo apt-get install libssl1.0
sudo chmod 777 /var/log
sudo chmod 777 /var/run
sudo wget --no-check-certificate https://github.com/pymumu/smartdns/releases/download/Release21/smartdns.1.2019.03.02-1141.x86_64.tar.gz
tar -zxvf smartdns.1.2019.03.02-1141.x86_64.tar.gz
rm smartdns.1.2019.03.02-1141.x86_64.tar.gz
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
eof
