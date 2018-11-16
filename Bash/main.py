#!/usr/bin/python2.7
import sys
import signal
import random
import subprocess

def send(data):
    sys.stdout.write(data)
    sys.stdout.flush()

def sendline(data):
    send(data + '\n')

def recv():
    send('> ')
    data = raw_input()
    return data

def getRand(table, length):
    res = ''
    for i in xrange(length):
        res += random.choice(table)
    return res

def filter(data):
    filtering = ['cat', '$', 'sh', '`', '<', '>', 'rm', 'more', 'less', 'echo', 'grep', 'flag', '*', 'vi', 'nc']
    for i in filtering:
        if i in data:
            return 0
    return 1

def timeout():
    sendline("Timeout!")
    sys.exit(1)

def execute(cmd):
    fileheader  = '#!/bin/bash\n'
    code = fileheader + cmd + '\n'

    filename = 'SH_' + getRand(__import__('string').lowercase, 16) + '.sh'

    f = open('/tmp/' + filename, 'w')
    f.write(code)
    f.close()

    subprocess.call(['chmod','+x','/tmp/'+filename])

    res = subprocess.check_output(['/tmp/' + filename])

    return res

if __name__ == '__main__':
    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(60)

    sendline("Plz send SH code")
    sendline("If you send \"END\", input will be ended")
    sendline("Then i will execute your code")

    sendline('-'*50)
    sendline('#!/bin/bash')
   
    code = ''
    while True:
        cmd = recv()
        if "END" in cmd:
            break
        code += cmd
    
    sendline('-'*50)

    if filter(code):
        try:
            print execute(code)
        except:
            sendline("Error")
    else:
        sendline("Filtered")