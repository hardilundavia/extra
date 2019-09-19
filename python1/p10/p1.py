class String:
    def __init__(self,str1=""):
        print("Constructor called...");
        self.str =str1;
    #
    def set(self,str1=""):
        self.str= str1;
    #
    def get(self):
        return self.str;
    #
    def length(self):
        return(len(self.str));
    #
    def join(self,String_s2):
        self.str = self.str+String_s2.str;
    #
    def compare(self,s):
        if(self.str == s.str):
           return True;
        else:
            return False;
    #
    def reverse(self):
        self.str = self.str[::-1];
        return self.str;
    #
    def palindrome(self):
        if(self.str == self.str[::-1]):
            return True;
        else:
            return False;
    #
    def checkword(self):
        s3 = input("Enter sentence : ");
        lst = s3.split(' ');
        print(lst);
        if(self.str in lst):
            return True;
        else:
            return False;
        
        
        
        
        

s1=String("hello");
print("s1 = ",s1.get());
s2=String("ddu");
print("s2 = ",s2.get());
print("length : ",s2.length());
s1.join(s2);
print("join:",s1.get());
if(s1.compare(s2)):
    print("s1 is same as s2 ");
else:
    print("s1 is not same as s2");

s1.reverse();
print("s1 = ",s1.get());
s1.set("hello");
if(s1.palindrome()):
    print("s1 is palindrome ");
else:
    print("s1 is not palindrome");
s1.set("gm")
if(s1.checkword()):
    print("word is available ");
else:
    print("word is not available");


