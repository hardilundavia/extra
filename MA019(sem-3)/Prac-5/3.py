class Sample:
    age=15;
    def __init__(self,name,age):
        self.name = name; 
        self.age = age ;

    def salary(self,sal):
        self.salary=sal;

    def isadult():
        print("Age : ",Sample.age>18);

    def display(self):
        print("Name : ",self.name);
        print("Salary : ",self.salary);
        print("Age : ",self.age);
##

s1=Sample("Hari",21);
s1.salary(20000);
s1.display();
Sample.isadult();
