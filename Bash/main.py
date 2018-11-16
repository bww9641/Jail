import sys
import signal

def send(data):
    sys.stdout.write(data)
    sys.stdout.flush()

def sendline(data):
    send(data + '\n')

def recv():
    data = raw_input(':> ')
    return data

def filter(data):
    filtering = []
    for i in filtering:
        if i in data:
            return 0
    return 1

def timeout():
    sendline("Timeout!")
    sys.exit(1)

if __name__ == '__main__':
    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(240)

    while True:
        cmd = recv()
        if filter(cmd):
            try:
                # Eval command
            except:
                sendline("Error")
        else:
            sendline("Filtered")