class A:
    def show(self):
        return 1


class B:
    def show(self):
        return 2


class C(A):
    def show(self):
       return 3+super().show()

c = C()
print(c.show())