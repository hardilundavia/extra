import sys
count=len(sys.argv)-1;
args=sys.argv
i=1
sum=0
max=0
min=999
while(i<=count):
    sum=int(args[i])+sum
    avg=int(sum//count)
    if (int(max) < int(args[i])):
        max=args[i]
    if(int(min)>int(args[i])):
        min=args[i]
    i=i+1
print("Sum : ",sum)
print("Averages : ",avg)
print("MAX : ",max)
print("MIN : ",min)
