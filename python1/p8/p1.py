def avg(l):
    for i in l:
        s=0;
        s = s + i;
        ln=len(l);
        a = s/ln;
    return a;
    

lst= [10,20,30];
avg = avg(lst);
print("Average : ",avg);

