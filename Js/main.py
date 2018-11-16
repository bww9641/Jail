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
    filtering = ['fs','child', '.','process', "'", "\"", '`']
    for i in filtering:
        if i in data:
            return 0
    return 1

def timeout():
    sendline("Timeout!")
    sys.exit(1)

def execute(cmd):
    fileheader  = ''
    code = fileheader + cmd + '\n'

    filename = 'JS_' + getRand(__import__('string').lowercase, 16) + '.js'

    f = open('/tmp/' + filename, 'w')
    f.write(code)
    f.close()

    res = subprocess.check_output(['node','/tmp/' + filename])

    return res

if __name__ == '__main__':
    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(60)

    sendline("Plz send JS code")
    sendline("If you send \"END\", input will be ended")
    sendline("Then i will execute your code")

    sendline('-'*50)
   
    code = ''
    while True:
        cmd = recv() + '\n'
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