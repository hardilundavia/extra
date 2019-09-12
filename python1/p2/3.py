import time;
import sys
start=time.time();
print(start);

args=sys.argv

n1=int(args[1])
if n1>1:
    for i in range(2,n1//2):
        if(n1%i==0):
           print(n1, "is not a prime number") 
           break
    else: 
        print(n1, "is a prime number") 

end=time.time();
print(end);
print(end - start ,"ms");
