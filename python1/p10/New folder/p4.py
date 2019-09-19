import datetime;
class Person:

    def __init__(self,name,age,bdate,gender):
        self.name=name;
        self.age=age;
        self.bdate=bdate;
        self.gender=gender;
        print("called..");

    def set(self,name,age,bdate,gender):
        self.name=name;
        self.age=age;
        self.bdate=bdate;
        self.gender=gender;

    def get(self):
        self.name=input("Enter name : ");
        self.age=int(input("Enter age : "));
        d=input("Enter birth date : ");
        self.bdate= datetime.datetime.strptime(d, "%d/%m/%Y")
        self.gender=input("Enter gender : ");
        
    def show(self):
        print("Name : ",self.name);
        print("Age : ",self.age);        
        print("Birthdate : ",self.bdate);
        print("Gender : ",self.gender);

##
class Student(Person):
    def __init__(self,name,age,bdate,gender,sem,py,java,php):
        super().__init__(name,age,bdate,gender);
        self.sem=sem;
        self.py =py;
        self.java=java;
        self.php =php;

    def set(self,name,age,bdate,gender,sem,py,java,php):
        super().set(name,age,bdate,gender);
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

    def __init__(self,name,age,bdate,gender,basic_sal):
        self.basic_sal = basic_sal;
        super().__init__(name,age,bdate,gender);

    def set(self,name,age,bdate,gender,basic_sal):
        super().set(name,age,bdate,gender);
        self.basic_sal=basic_sal;

    def get(self):
        super().get();
        self.basic_sal=int(input("Enter basic salary  : "));


    def show(self):
        super().show();
        print("Basic salary : ",self.basic_sal);

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
            self.da =(self.basic_sal * 10)/100;
            print("HRA for male : ",self.hra);

    def calc_total_sal(self):
        self.mon_sal = self.basic_sal + self.da+self.hra;
        print("Total Monthly salary : ",self.mon_sal);
    def gross_sal(self):
        print
                   
            
        
p1=Person("mina",22,"30/05/1998","male");
p1.set("visu",21,"30/10/1998","male");
p1.show();
#p1.get();
#p1.show();

s1 = Student("Hari",22,"30/05/1998","male",2,20,20,20);
s1.calc_total();
s1.show();
s1.calc_grade();


e1 = Employee("piyu",22,"30/05/1998","f",20000);
e1.show();
e1.get();
e1.show();
e1.calc_da();
e1.calc_hra();
e1.calc_total_sal();
