from datetime import date
import datetime;
class age():
    def __init__(self):
        print("con called");
    def get(self):
        self.t =date.today();
        print(self.t);
        
        self.bdate = input("enter date :");
        #d=input("Enter birth date : ");
        self.bdate= datetime.datetime.strptime(self.bdate,"%d/%m/%Y");
        print(self.bdate);
        self.age = self.t.year-self.bdate.year - ((self.t.month, self.t.day) < (self.bdate.month, self.bdate.day));
        print(self.age);
        

a1 =age();
a1.get();


p1=Person("mina","30/05/1998","male");
p1.set("visu","30/10/1998","male");
p1.show();
#p1.get();
#p1.show();

s1 = Student("Hari","30/05/1998","male",2,20,20,20);
s1.calc_total();
s1.show();
s1.calc_grade();
