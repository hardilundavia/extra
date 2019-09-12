n1 = (input("enter no1 : "));
n2 = (input("enter no2 : "));
if not n1.isnumeric() or not n2.isnumeric():
    print("not numeric");
else  :
    print(" numeric ");
    n1 = int(n1);
    n2 = int(n2);
    add = n1 + n2;
    mul = n1 * n2;
    div = n1 /n2;
    sub = n1 - n2;
    print(add);
    print(mul);
    print(div);
    print(sub);
