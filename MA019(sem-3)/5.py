eno=int(input("Enter employee number : "));
name=input("Enter employee name : ");
gender=input("Enter employee gender : ");
sal=input("Enter employee salary : ");
if gender=="Male" or gender=="male":
    da=sal*(80/100);
    hra=sal*(10/100);
    net=sal+da+hra;
elif gender=="Female" or gender=="female":
    da=sal*(70/100);
    hra=sal*(15/100);
    net=sal+da+hra;

print("\nEno\tname\tgender\tsalary\tda\thra\tnet\n");
print(eno,"\t",name,"\t",sal,"\t",da,"\t",hra,"\t",net);
    
