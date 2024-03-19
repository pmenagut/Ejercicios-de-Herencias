

class Base:
    def __init__(self):
        self.a = "a"
        self.b = "b"
        self.c = "c"

    def A(self):
        print(self.a)

    def B(self):
        print(self.b)

    def C(self):
        print(self.c)


class Derivada(Base):
    def __init__(self):
        super().__init__()
        self.a = "aa"
        self.c = "cc"

    def B(self):
        self.b = "bb"
        super().B()
        print(self.b)


def main():
    base = Base()
    derivada = Derivada()

    base.A()

    derivada.A()
    print()

    base.B()

    derivada.B()
    print()

    base.C()

    derivada.C()
    print()

    derivada = base

    derivada.C()


if __name__ == "__main__":
    main()


