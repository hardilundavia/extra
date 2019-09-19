import datetime;
class Person:
    x = datetime.datetime.now();
    current_Year = x.strftime("%Y");
    def __init__(self,nm="",bdt=datetime.datetime(2000,1,1),gen=""):
        self.name=nm;
        self.bdate=bdt.strftime ("%d-%m-%Y");
        self.bdate = datetime.datetime.strptime(self.bdate,"%d-%m-%Y");
        self.year = self.bdate.strftime("%Y");
        self.gender=gen;
    
    def set(self):
        self.name=input("Enter Name : ");
        self.bdate=input("Enter Date of Birth : ");
        self.bdate = datetime.datetime.strptime(self.bdate,"%d-%m-%Y");
        self.year = self.bdate.strftime("%Y");
        self.count_age();
        self.gender=input("Enter Gender : ");

    def count_age(self):
        self.age = int(Person.current_Year) - int(self.year);
        
    def show(self):
        print("Name : ",self.name);
        print("Date of Birth : ",self.bdate);
        print("Age : ",self.age);
        print("Year",self.year);
        print("Gender : ",self.gender);

#
class Student(Person):
    def __init__(self,sem=0,pym=0,jm=0,phpm=0):
        super().__init__();
        self.semester = sem;
        self.py_marks = pym;
        self.j_marks = jm;
        self.php_marks = phpm;

    def set(self):
        self.semester = int(input("Enter Semester : "));
        self.py_marks = int(input("Enter Python Marks : "));
        self.j_marks = int(input("Enter Java Marks : "));
        self.php_marks = int(input("Enter Php Marks : "));

    def calc_total(self):
        self.total = self.py_marks + self.j_marks + self.php_marks;
        self.percentage = self.total/3;

    def calc_grade(self):
        if self.percentage >=70:
            self.grade = "Distinction Class";
        elif self.percentage >=60 and self.percentage<70:
            self.grade = "First Class";
        elif self.percentage >=50 and self.percentage<60:
            self.grade = "Second Class";
        elif self.percentage >=40 and self.percentage<50:
            self.grade = "Pass Class";
        else:
            self.grade = "Fail";

    def show(self):
        print("Semester : ",self.semester);
        print("Python Marks :",self.py_marks);
        print("Java Marks :",self.j_marks);
        print("Php Marks :",self.php_marks);

#
class Employee(Person):
    def __init__(self,b_salary=0):
        super().__init__();
        self.basic_salary = b_salary;

    def set(self):
        super().set();
        self.basic_salary = int(input("Enter A Basic Salary :"));

    def calc_hra_da(self):
        self.calc_da();
        self.calc_hra();
        self.calc_total_sal();
        self.calc_gross_sal();

    def calc_da(self):
        if (self.gender)=='male' and (self.gender)=='Male':
            self.da = (self.basic_salary*0.80);
        else:
            self.da = (self.basic_salary*0.70);

    def calc_hra(self):
        if (self.gender)=='male' and (self.gender)=='Male':
            self.hra = (self.basic_salary*0.10);
        else:
            self.hra = (self.basic_salary*0.15);

    def calc_total_sal(self):
        self.total_salary = self.basic_salary + self.hra + self.da;

    def calc_gross_sal(self):
        self.bonus = self.basic_salary * 0.50;
        self.senbonus = 0;
        if self.age >= 60:
            self.senbonus = self.bonus * 0.02;
        self.gross_salary = (self.total_salary * 12) + self.bonus + self.senbonus;

    def show(self):
        super().show();
        print("Basic Salary    : ",self.basic_salary);
        print("DA              : ",self.da);
        print("HRA             : ",self.hra);
        print("Total Salary    : ",self.total_salary);
        print("Bonus           : ",self.bonus);
        print("Addtional Bonus : ",self.senbonus);
        print("Gross_salary : ",self.gross_salary);

e1=Employee();
e1.set();
e1.calc_hra_da();
e1.show();
