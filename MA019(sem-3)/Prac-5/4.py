import datetime;
class Person:

    def __init__(self,name,age,bdate,gender):
        self.name=name;
        self.age=age;
        self.bdate=bdate;
        self.gender=gender;

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
    def __init__(self,semester,py_marks,j_marks,php_marks):
        self.semester=semester;
        self.py_marks=py_marks;
        self.j_marks=j_marks;
        self.php_marks=php_marks;

    def set(self,semester,py_marks,j_marks,php_marks):
        self.semester=semester;
        self.py_marks=py_marks;
        self.j_marks=j_marks;
        self.php_marks=php_marks;

    def get():
        self.semster=int(input("Enter semester  : "));
        self.py_marks=int(input("Enter python marks  : "));
        self.j_marks=int(input("Enter java marks  : "));
        self.php_marks=int(input("Enter php marks  : "));

    def show():
        print("Semester : ",self.semester);
        print("Python marks : ",self.py_marks);        
        print("Java marks : ",self.j_marks);
        print("PHP marks : ",self.php_marks);
        
p1=Person("Hari",22,"30/05/1998","male");
p1.show();
p1.set("Hariom",21,"30/10/1998","male");
p1.show();
p1.get();
p1.show();
