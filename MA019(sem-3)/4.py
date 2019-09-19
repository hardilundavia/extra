name=input("Enter name : ");
rn=int(input("Enter rollno : "));
s1=int(input("Enter C marks : "));
s2=int(input("Enter C++ marks : "));
s3=int(input("Enter Java marks : "));
s4=int(input("Enter Python marks : "));

total=s1+s2+s3+s4;
per=total/4;

print("Total : ",total);
print("Percentage : ",per);


if per>80:
    grade="A;";
elif per>=70 and per<80:
    grade="B";
elif per>=60 and per<70:
    grade="C";
elif per>=50 and per<60:
    grade="D";
else:
    grade="Fail";

print("\n--------------------------------Marksheet---------------------------------\n");
print("Name\tRollNo\t C\t C++\tJAVA\tPython\tTotal\tPercentage\tGrade\n");
print(name,"\t",rn,"\t",s1,"\t",s2,"\t",s3,"\t",s4,"\t",total,"\t",per,"\t\t",grade);
