n1=int(input("Enter n1 value : "));
n2=int(input("Enter n2 value : "));

if(n1<n2):
    for i in range(n1,n2+1):
        if(i%2!=0):
            print(i)
else:
    #print("N1 must be greater then n2")
    i=n2
    while(i>=n2):
        print(i)
    i=i-1
