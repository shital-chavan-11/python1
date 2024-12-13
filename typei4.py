# Hierarchial Inheritane 
class Basic():
    def __init__ (self,info):
        self.name=info[0]
        self.occupation=info[1]
        self.address=info[2]
        self.age=info[3]
class Adolescene(Basic):
    def __init__ (self,info):
         Basic.__init__(self,info)
    def agot(self):
        mother=input("enter your mother name:")
        father=input("enter your father name:")
        print(mother,father,"of the ",self.name ,"you will get your child addhar as soon as possible.")
class Early_adulthood(Basic):
    def __init__ (self,info):
         Basic.__init__(self,info)
    def egot(self):
        print(self.name,"you will got the aadhar as soon as possible")

class Late_adulthood(Basic):
    def __init__ (self,info):
        Basic.__init__(self,info)
    def lgot(self):
        print(self.name,"you will got the aadhar as soon as possible")
print("hii indians , look at here  there is one way to create the new aadhar card in just only 24 hours")
print("please fill the below details:")
name=input("enter your name:")
occupation=input("enter your occupation")
address=input("enter your current address:")
age=int(input("enter your age :"))
info=[name,occupation,address,age]
if 13<=age<=18:
    print("you are the adolescene")
    obj=Adolescene(info)
    obj.agot()
elif 19<=age<=40:
    print("you are the early adulthood")
    obj=Early_adulthood(info)
    obj.egot()
else:
    print("you are the late adulthood")
    obj=Late_adulthood(info)
    obj.lgot()