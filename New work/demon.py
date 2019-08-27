import sys
import os
import time
import signal


def handler(signum, frame):
    print('Signal handler called with signal', signum)
    sys.exit(1)

signal.signal(signal.SIGUSR1, handler)

pid = os.fork()

print(os.getpid())

if sys.argv[1] == "-k":
    os.kill(pid, signal.SIGKILL)
    os.unlink("demon.pid")
elif sys.argv[1] == "-c":
    os.kill(pid, signal.SIGINT)
elif sys.argv[1] == "-u":
    os.kill(pid, signal.SIGUSR1)
else:
    if pid == 0:
        demon()
        while True:
            try:
                pass
            except KeyboardInterrupt:
                print("Работаем дальше")
            pass
    else:
        if not os.path.isfile("demon.pid"):
            with open("gemon.pid", "w") as pid_file:
                pid_file.write(f"{pid}")
            print("Master close")
            print("Demon has pid {}".format(pid))


    #
    # time.sleep(10)
    # os.kill(pid, signal.SIGKILL)
