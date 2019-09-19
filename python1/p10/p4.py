import datetime;
from datetime import date
class Person:

    def __init__(self,name,bdate,gender):
        self.name=name;
        self.bdate=bdate;
        self.gender=gender;
        print("called..");

    def set(self,name,bdate,gender):
        self.name=name;
        self.bdate=bdate;
        self.gender=gender;

    def get(self):
        self.name=input("Enter name : ");
        self.gender=input("Enter gender : ");
        
    def show(self):
        print("Name : ",self.name);
               
        print("Birthdate : ",self.bdate);
        print("Gender : ",self.gender);

##
class Student(Person):
    def __init__(self,name,bdate,gender,sem,py,java,php):
        super().__init__(name,bdate,gender);
        self.sem=sem;
        self.py =py;
        self.java=java;
        self.php =php;

    def set(self,name,bdate,gender,sem,py,java,php):
        super().set(name,bdate,gender);
        self.sem=sem;
        self.py =py;
        self.java=java;
        self.php =php;
    def get(self):
        super().get();
        self.sem=int(input("Enter semester  : "));
        self.py=int(input("Enter python marks  : "));
        self.java=int(input("Enter java marks  : "));
        self.php=int(input("Enter php marks  : "));

    def show(self):
        super().show();
        print("Semester : ",self.sem);
        print("Python marks : ",self.py);        
        print("Java marks : ",self.java);
        print("PHP marks : ",self.php);
        print("total : ",self.total);

    def calc_total(self):
        self.total = self.py+ self.java+self.php;
        

    def calc_grade(self):
        self.per = self.total/3;
        if self.per>=70:
            print("Grade A");
        elif self.per<70 or self.per>=60:
            print("Grade B");
        elif self.per<60 or self.per>=50:
            print("Grade C");
        elif self.per<50 or self.per>=40:
            print("Grade D");
        else:
            print("Fail.. better luck next ...");

##

class Employee(Person):

    def __init__(self,name,bdate,gender,basic_sal):
        self.basic_sal = basic_sal;
        super().__init__(name,bdate,gender);

    def set(self,name,bdate,gender,basic_sal):
        super().set(name,age,bdate,gender);
        self.basic_sal=basic_sal;

    def get(self):
        super().get();
        self.basic_sal=int(input("Enter basic salary  : "));
        self.bdate = input("enter date :");
        self.bdate= datetime.datetime.strptime(self.bdate,"%d/%m/%Y");
        



    def show(self):
        super().show();
        print(self.bdate);
        print("Basic salary : ",self.basic_sal);
        print("Gross salary : ",self.gross);

    def calc_da(self):
        if(self.gender == "female" or self.gender == "f"):
            self.da =(self.basic_sal * 70)/100;
            print("DA for female : ",self.da);
        else :
            self.da =(self.basic_sal * 80)/100;
            print("DA for male : ",self.da);
            

    def calc_hra(self):
        if(self.gender == "female" or self.gender == "f"):
            self.hra =(self.basic_sal * 15)/100;
            print("HRA for female : ",self.hra);
        else :
            self.hra =(self.basic_sal * 10)/100;
            print("HRA for male : ",self.hra);

    def calc_total_sal(self):
        self.mon_sal = self.basic_sal + self.da+self.hra;
        print("Total Monthly salary : ",self.mon_sal);
    def gross_sal(self):
        self.yrly_sal = self.mon_sal *12;
        if(self.age >=60):
            self.bon1 = (basic_sal *50)/100;
            self.bon2 = (basic_sal * 2 )/100;
            self.gross = self.yrly_sal + self.bon1+self.bon2;
        else:
            self.gross = self.yrly_sal + self.bon1;
        

    def getage(self):
        self.t =date.today();
        print("Curent time : ",self.t);
        self.age = self.t.year-self.bdate.year - ((self.t.month, self.t.day) < (self.bdate.month, self.bdate.day));
        print("Age : ",self.age);
        
        
        
                   
            
        


e1 = Employee("piyu","30/05/1998","f",20000);

e1.get();

e1.calc_da();
e1.calc_hra();
e1.calc_total_sal();
e1.getage();
e1.gross_sal();
e1.show();
