class ACLass():
    name = "Uasya"

    def __init__(self, name, first_name):
        self.name = name
        self.first_name = first_name

    def __repr__(self):
        return "<class ACLass()>"

    def __str__(self):
        return f"{self.name}"

    def __setattr__(self, name, value):
        # print(name, value, "Установка значения")
        super().__setattr__(name, value)
        # self.__dict__[name] = value


def __getattr__(self, name):
    if name == "attr2":
        raise AttributeError(f"Attribute '{name}' not found")
    try:
        value = self.__dict__[name]
    except KeyError:
        raise AttributeError(f"Attribute '{name}' not found")
    else:
        return value

    # def __len__(self):
    #     return 5

def __bytes__(self):
    return bytes(4)

def __call__(self):
    return "Object"

if __name__ == '__main__':
    a = ACLass("A", "Object")
    b = ACLass("B", "Object")
    a.attr1 = 1
    # a.attr2 = 2
    print(a.attr1)
    # print(a.attr2)
    # print(len(a))

    
