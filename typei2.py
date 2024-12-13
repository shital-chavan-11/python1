#multiple inheritance 
class Electronic_shop():
    def __init__ (self,info1):
        self.frige=info1[0]
        self.pricef=info1[1]
        self.tv=info1[2]
        self.pricev=info1[3]
        self.cooler=info1[4]
        self.pricec=info1[5]
class stationary_shop():
    def __init__ (self,info2):
        self.books=info2[0]
        self.priceb=info2[1]
        self.pens=info2[2]
        self.peicep=info2[3]
        self.bags=info2[4]
        self.pricebag=info2[5]
class Customer(Electronic_shop,stationary_shop):
    def __init__ (self,info1,info2):
        Electronic_shop.__init__(self, info1)
        stationary_shop.__init__(self, info2)
    def customer1(self):
        total_expensive=self.pricef+self.pricev+self.priceb+self.pricebag
        print(total_expensive)
        print("what you buyed",self.frige,self.tv,self.books,self.bags)
    
print("welcome , customer  in Electronic shop")
frige=input("which brand you selected for the buying:")
pricef=int(input("enter the price of the frige :"))
tv=input("which brand you slectde for buying the tv:")
pricev=int(input("enter the price of the tv:"))
cooler=input("which brand you selected for the buying:")
pricec=int(input("enter the price of the cooler:"))
info1=[frige,pricef,tv,pricev,cooler,pricec]

print("welcome , customer  in stationary shop")
books=input("which book you buyed:")
priceb=int(input("enter the price of the books"))
pens=input("enter the how many pens you buyed")
pricep=(input("enter the price of the pens"))
bags=input("enter the brand of your bag")
pricebag=int(input("enter the price of the bag"))
info2=[books,priceb,pens,pricep,bags,pricebag]
obj=Customer(info1,info2)
obj.customer1()


