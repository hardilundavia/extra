n1 = int(input("enter no 1 : "));
n2 = int(input("enter no 2 : "));
a = n1 + n2 ;
m = n1 * n2;
s = n1 - n2;
d = n1 / n2;
mul = oct(m);
sub = oct(s);
add = oct(a);
print(n1 ,"+", n2 ,"=" ,add);
print(n1 ,"*", n2, "=" ,mul);
print(n1 ,"-" ,n2 ,"=" ,sub);
print("hexadecimal opration")
mul = hex(m);
sub = hex(s);
add = hex(a);
print(n1 ,"+", n2 ,"=" ,add);
print(n1 ,"*", n2, "=" ,mul);
print(n1 ,"-" ,n2 ,"=" ,sub);

