def func(*args, **kwargs):
    print(args)
    print(kwargs)


if __name__== '__main__':
    func(
        3,
        4,
        "string",
        key="value",
        key2="value2"
    )
