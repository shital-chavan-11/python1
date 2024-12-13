#single inheritance
class Car():
    def __init__ (self,lst):
        self.name=lst[0]
        self.launching_year=lst[1]
        self.price=lst[2]
        self.color=lst[3]
        self.founder=lst[4]
        self.name_tractor=lst[5]
        self.launching_tractor=lst[6]
        self.price_tractor=lst[7]
        self.color_tractor=lst[8]
        self.founder_tractor=lst[9]
    def info(self):
        print("i like cars.so i have better combination of the car")
    def driving(self):
        print(self.color,self.name ,"car is running")
class Tractor(Car):
    def tractor(self):
        print(self.name_tractor,"is running for the firming")
    def stop(self):
        print(self.color,self.name_tractor,"is stop because  driver is very tired ")
name=input("enter the brand name of the car")
launching_year=input("enter the launching year")
price=input("enter the price of the car")
color=input("enter the color of the car")
founder=input("enter the founder name of the car")
name_tractor=input("enter the brand name of the tractor")
launching_tractor=input("enter the launching year")
price_tractor=input("enter the price of the tractor")
color_tractor=input("enter the color of the tractor")
founder_tractor=input("enter the founder name of the tractor")
lst=[name,launching_year,price,color,founder,name_tractor,launching_tractor,price_tractor,color_tractor,founder_tractor]
obj=Tractor(lst)
obj.driving()
obj.info()
obj.tractor()
obj.stop()
