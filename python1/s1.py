n1 = int(input("enter no 1 : "));
n2 = int(input("enter no 2 : "));
octal = oct(n1);
sum1 = n1 - n2;
octal2 = oct(sum1);
print(n1 ,"/", n2 ,"=" ,octal2);
print(type(octal2));
