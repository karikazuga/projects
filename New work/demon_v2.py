import sys
import os
import time
from datetime import datetime
from random import randint
import signal


PID_FILE = ""

def demon():

    def handler(signum, fram):
        with open("signal.log", "a") as log_file:
            log_file.write(f"Signal: {signum}\n{frame}\n\n")

    signal.signal(signal.SIGUSR1, handler)
    signal.signal(signal.SIGUSR2, handler)
    signal.signal(signal.SIGUSR3, handler)

    while True:
        with open("demon.log", "a") as log_file:
            log_file.write(f"{datetime.now()}\n\n")
        exept KeyboardInterrupt:
        with open("signal.log", "a") as log_file:
            log_file.write("Ctrl + C")
            exept Exception as e:
            pass
        finally:
            time.sleep(randint(5, 15))

def start_demon():
    pid = demon()

def send_signal(args):
    pass

if __name__ == '__main__':
    try:
        args = sys.argv[1:]
    except IndexError:
        start_demon()
    else:
        send_signal(args)
