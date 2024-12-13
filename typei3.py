#multilevel inheritance
class Basic():
    def __init__ (self,info):
        self.name=info[0]
        self.field=info[1]
        self.books=info[2]
        self.exam=info[3]
        self.hours=info[4]
class Secondary(Basic):
    def branch(self):
        print("you  want to focus on the study of the tenth standard because that exam deside your future ")
        marks=int(input("please enter your desired marks that you want to acheive :"))

        if marks>=80:
           print("you will got the science ")
        elif marks>=79:
           print("you will got the commerce")
        else:
            print("you will got the art")
class Higher_secondary(Secondary):
    def __init__(self, info):
        Basic.__init__(self, info) 
    def deside_field(self):
        print("you  want to focus on the study of the 12th standard because that exam deside your future ")
        marks=int(input("please enter your desired marks that you want to acheive :"))
        if marks>=80:
           print("you  go for the engineering ")
        elif marks>=79:
           print("you go for the bcs")
        else:
           print("you go for the Bsc")
class Student(Higher_secondary):
    def __init__(self, info):
        Higher_secondary.__init__(self, info) 
    def behaviour(self):
        if self.hours>10:
            print("you are the topper")
        elif self.hours>5:
            print("you are the average")
        else:
            print("you are the backbancher")  
        
print("welcome student let's analize the what study you did okay")
name=input("enter your name:")
field=input("enter your field like secondary , higher seconadry ")
books=input("enter your books")
exam=input("please share the upcoming exam details :")
hours=int(input("enter the how many hours are spend you with the books "))
info=[name,field,books,exam,hours]
obj=Student(info)
obj.behaviour()
if field=="secondary":
    obj.branch()
else:
    obj.deside_field()

