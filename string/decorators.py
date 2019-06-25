from datetime import datetime

func_wrap = []
func_clock = []


def wrap(func):
    print("Wrap", func)
    func_wrap.append(func)

    def action(*args, **kwargs):
        result = func(*args, **kwargs)
        print("decorator wrapper", result)
        return result

    return action


def clock(func):
    func_clock.append(func)
    print("Clock", func)

    def action(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        message = "Start: {0}\n, End: {1}\n"
        print(message.format(start, end-start))
        return result

    return action

@wrap
@clock
def func():
    for i in range(0,10000):
        print(i)


if __name__ == '__main__':
    func()
