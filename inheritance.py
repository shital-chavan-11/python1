class A:
    def login(self):
        print("this is login function in the classA")
class B(A):
    def register(self):
        print("this is register function in the class B")
class C(A):
    def register(self):
        print("this is register function in the class c")
class D(C,B):
    pass
obj=D()
obj.register()