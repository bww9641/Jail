import sys
import signal

def send(data):
    sys.stdout.write(data)
    sys.stdout.flush()

def sendline(data):
    send(data + '\n')

def recv():
    data = raw_input('')
    return data
';'
def filter(data):
    filtering = ['#', 'system', 'exec', 'syscall', 'open']
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

    

if __name__ == '__main__':
    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(240)

    sendline("Plz send C code")
    sendline("If you send \"END\", input will be ended")
    sendline("Then i will execute your code")

    sendline('-'*50)
    sendline('#include <stdio.h>')
    sendline('int main(int argc, char *argv[]) {')

    code = ''
    while True:
        cmd = recv()
        if "END" in cmd:
            break
        code += cmd
    sendline('}')

    sendline('-'*50)

    if filter(cmd):
        try:
            execute(cmd)
        except:
            sendline("Error")
    else:
        sendline("Filtered")