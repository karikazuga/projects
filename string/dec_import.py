import decorators as dc

@dc.clock
def new_func():
    for i in range(5):
        print(i)

if __name__ == '__main__':
    print(dc.func_wrap)
    print(dc.func_clock)
    
