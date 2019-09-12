n1 = int(input("Enter no 1 : "));
n2 = int(input("Enter no 2 : "));

if(n1<n2):
    i=n1;
    while(i<=n2):
        print(i);
        i=i+1;
else:
    i=n1;
    while(i>=n2):
        print(i);
        i=i-1;

print("bye");
