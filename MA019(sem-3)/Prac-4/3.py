class Student:
    total=0;

    def __init__(self):
        Student.total=Student.total+1;
    def input(self):
        self.rno=int(input("Enter Rollno : "));
        self.name=input("Enter Name : ");
        self.c_marks=int(input("Enter C_marks : "));
        self.cpp_marks=int(input("Enter CPP_marks : "));
        self.python_marks=int(input("Enter Python marks : "));

    def show(self):
        print("Roll no : ",self.rno);
        print("Name : ",self.name);
        print("C_marks : ",self.c_marks);
        print("CPP_marks : ",self.cpp_marks);
        print("Python_marks : ",self.python_marks);

    def calc_total(self):
        return self.c_marks + self.cpp_marks + self.python_marks;

    def calc_per(self):
        return self.calc_total()/3;

    def calc_grade(self):
        if(self.calc_per()>=70):
            print("Grade : a");
        elif(self.calc_per()>=60 and self.calc_per()<70):
            print("Grade : b");
        elif(self.calc_per()>=50 and self.calc_per()<60):
            print("Grade : c");
        elif(self.calc_per()>=40 and self.calc_per()<50):
            print("Grade : d");
        else:
            print("fail");
##
s1=Student();
s1.input();
s1.show();

print("Total : ",s1.calc_total());
print("Percentage : ",s1.calc_per());
s1.calc_grade();
