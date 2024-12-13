
lst=[]
class Student():
    def __init__ (self,info,n):
       
            self.f_name=info[i][0]
            self.m_name=info[i][1]
            self.l_name=info[i][2]
            self.mobile_no=info[i][3]
            self.student_email=info[i][4]
            self.category=info[i][5]
            self.date_of_birth=info[i][6]
            self.parent_name=info[i][7]
            self.parent_email=info[i][8]
            self.perment_Address=info[i][9]
            self.year_admission=info[i][10]
            self.generate_PRN()
    def generate_PRN(self):
       
        unique=""
        for i in mobile_no[2:7]:
            unique=unique+i
           
        PRN=self.year_admission+self.category+unique
        if PRN is not lst:
            lst.append(PRN)
            print(lst)
        print(PRN)
        self.admit()
    def admit(self):
        print("you have unique PRN number then you admission successfull!!")
        self.department()
    def department(self):
        print("select your Department 1)CSE 2)ENTC 3)CIVILE 4)MECHANICAL 5) ELECTRICAL ")
        department=input("enter the your department:")
        if department=="CSE":
            print("welcome in the CSE department")
        if department=="ENTC":
            print("Welcome in ENTC Department")
        if department=="CIVILE":
            print("welcome in CIVILE department")
        if department=="MECHANICAL":
            print("welcome in MECHANICAL department")
        if department=="ELECTRICAL":
            print("welcome in ELECTRICAL department")

   
info={}     
p=int(input("enter the no of student:"))
for i in range(1,p+1):
    f_name=input("Enter the sudent first name:")
    m_name=input("Enter the sudent middle name:")
    l_name=input("Enter the sudent last name:")
    mobile_no=input("Enter the sudent mobile no:")
    student_email=input("Enter the sudent email :")
    category=input("Enter the sudent category:")
    date_of_birth=input("Enter the sudent date of birth:")
    parent_name=input("Enter the parent/Gaurdian_name:")
    parent_email=input("Enter the parent Email:")
    Perment_Address=input("Enter the perment address:")
    year_admission=input("Enter the Year of Admisiion:")

info.setdefault(i,[f_name,m_name,l_name,mobile_no,student_email,category,date_of_birth,parent_email,parent_name,Perment_Address,year_admission])
a=Student(info,p)

