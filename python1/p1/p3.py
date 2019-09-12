import sys;
import timeit;
import time;
args = sys.argv
n1 = (args[1]);

t1 = timeit.timeit();
print(t1);
if not n1.isnumeric():
    print("not numeric ");
else:
    print("numeric..");
    n1 =int(n1);
    if(n1%2==0):
        print("no is prime no ");
    else:
        print("no is not  prime no ");

t2=timeit.timeit();
print(t2);
t3 =t1-t2;

print("Elapsed time is : ",t3);
t4 = time.process_time();
print("process time  : ",t4);
