import sys
args=sys.argv
n1=int(args[1]);
n2=int(args[2]);

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
