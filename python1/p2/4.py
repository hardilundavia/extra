import sys
import time;
start=time.time()
print(start)

args=sys.argv
n1=int(args[1])
n2=int(args[2])

for i in range(n1,n2+1):
    if(i>1):
            for n in range(2,i):
                if(i%n==0):
                    break;
            else:
                print(i)
end=time.time()
print(end)
print("Execution time : %.10f " %(end-start))
