class Sample:
    x=10;
    def modify(cls):
        cls.x+=1;

s1=Sample();
s2=Sample();
print("x in s1 : ",s1.x);
print("x in s2 : ",s2.x);

s1.modify();
print("x in s1 : ",s1.x);
s2.modify();
print("x in s2 : ",s2.x);
