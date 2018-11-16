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
    filtering = ['#', 'system', 'exec', 'syscall', 'open', 'asm', 'mmap', 'mprotect']
    for i in filtering:
        if i in data:
            return 0
    return 1

def timeout():
    sendline("Timeout!")
    sys.exit(1)

def execute(cmd):
    fileheader  = '#include <stdio.h>\n'
    fileheader += 'int main(int argc, char *argv[]) {\n'

    code = fileheader + cmd + '\n}\n'

    filename = 'C_' + getRand(__import__('string').lowercase, 16)
    
    f = open('/tmp/' + filename + '.c', 'w')
    f.write(code)
    f.close()

    status = subprocess.call(['gcc','-o','/tmp/' + filename, '/tmp/' + filename + '.c'])
    
    if status:
        return 'Compile error'

    res = subprocess.check_output(['/tmp/' + filename])

    return res

if __name__ == '__main__':
    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(60)

    sendline("Plz send C code")
    sendline("If you send \"return 0;\", input will be ended")
    sendline("Then i will execute your code")

    sendline('-'*50)
    sendline('#include <stdio.h>')
    sendline('int main(int argc, char *argv[]) {')

    code = ''
    while True:
        cmd = recv() + '\n'
        code += cmd
        if "return 0;" in cmd:
            break

    sendline('}')

    sendline('-'*50)

    if filter(cmd):
        try:
            sendline(execute(code))
        except:
            sendline("Error")
    else:
        sendline("Filtered")
 