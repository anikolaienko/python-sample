class A():
    def ping(self):
        print('ping A: ', self)

class B(A):
    def pong(self):
        print('pong B: ', self)

class C(A):
    def pong(self):
        print('pong C: ', self)

class D(B, C):
    def ping(self):
        super().ping()
        print('ping D: ', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)

d = D()
d.ping()
print("-----------------")
d.pong()
print("-----------------")
d.pingpong()
print("-----------------")
