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
    filtering = ['system','exec','shell','`','open','file','eval', 'include', 'require', '$']
    for i in filtering:
        if i in data:
            return 0
    return 1

def timeout():
    sendline("Timeout!")
    sys.exit(1)

def execute(cmd):
    fileheader  = '<?php\n'
    code = fileheader + cmd + '\n'

    filename = 'PHP_' + getRand(__import__('string').lowercase, 16) + '.php'

    f = open('/tmp/' + filename, 'w')
    f.write(code)
    f.close()

    res = subprocess.check_output(['php','/tmp/' + filename])

    return res

if __name__ == '__main__':
    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(60)

    sendline("Plz send PHP code")
    sendline("If you send \"?>\", input will be ended")
    sendline("Then i will execute your code")

    sendline('-'*50)
    sendline("<?php")

    code = ''
    while True:
        cmd = recv() + '\n'
        code += cmd
        if "?>" in cmd:
            break

    
    sendline('-'*50)

    if filter(code):
        try:
            print execute(code)
        except:
            sendline("Error")
    else:
        sendline("Filtered")