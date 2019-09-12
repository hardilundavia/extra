def print_menu():
    print("1). Addition");
    print("2). Subtraction");
    print("3). Multiplication");
    print("4). Divition");
    print("5). Average");
    print("6). Maximum");
    print("7). Minimum");



def get_choice():
    print("for Exit press 8...")
    choice = int(input("Enter the choice from menu : "));
    return choice;


def add(l):
    print("sum function...");
    s=0;
    for i in l:
        s=s+i;
    return s;

def sub(l):
    print("sub function...");
    print(l);
    n1 = int(input("element index : "));
    n2 = int(input("element index : "));
    sb = l[n1]-l[n2];
    return sb;
    
def mul(l):
    m=1;
    print("mul function...");
    for i in l:
        m=m*i;
    return m;

def div(l):
   
    print("div function...");
    n1 = int(input("element index : "));
    n2 = int(input("element index : "));
    d = l[n1]/l[n2];
    return d;

def avg(l):
    for i in l:
        s=0;
        s = s + i;
        ln=len(l);
        a = s/ln;
    return a;
    
    
lst= [10,20,30];

print("....Menu....");
print_menu();
print("....choice.... ");
ch = get_choice();
while ch != 8:
    if ch == 1:
        sum = add(lst);
        print("addition ",sum);
    elif ch==2:
        sub = sub(lst);
        print("Subtraction : ",sub);
    elif ch ==3:
        mul = mul(lst);
        print("Multiplication : ",mul);
    elif ch == 4:
        div = div(lst);
        print("Division : ",div);
    elif ch ==5:
        avg = avg(lst);
        print("Average : ",avg);
    elif ch == 6:
        ma = max(lst);
        print(ma);
    elif ch == 7:
        mn = min(lst);
        print(mn);


    

