from datetime import datetime


class Person():

    def __init__(self):
        self.__birth_day = datetime.now()
        self._name = None

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def get_birth_day(self):
        return self.__birth_day


class Human(Person):

    def __init__(self, name):
        super().__init__()
        self._name = name


class Man(Human):

    __sex = "M"

    def get_sex(self):
        return self.__sex


class Woman(Human):

    __sex = "F"

    def get_sex(self):
        return self.__sex

    @classmethod
    def test(cls, arg):
        print(arg)

if __name__ == '__main__':
    masha = Woman("Masha")
    print(masha.get_name())
    vasya = Man("Vasya")
    print(vasya.get_birth_day())
    print(vasya.get_name())

    print(masha.get_sex())
    print(vasya.get_sex())

    Woman.test("!!!!!!!")
