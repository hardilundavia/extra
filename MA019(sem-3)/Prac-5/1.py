class String:
    def __init__(self,str):
        print("Default constructor is called");
        self.str=str;
        
    def set(self,str):
        self.str=str;

    def get(self):
        return self.str;
    
    def length(self,str):
        return len(self.str);

    def join(self,s2):
        self.str=self.str+s2.str;

    def compare(self,str1,str2):
        return str1==str2;

    def reverse(self,str):
        return str[::-1];

    def palindrome(self,str):
        return str==str[::-1];

    def wordinsen(self,str,word):
        return word in str;
##

s1=String("Hari");
s2=String("Om");
str1=input("Enter String 1 : ");
str2=input("Enter String 2 : ");
s1.set(str1);
print("String : ",s1.get());

print("--------Length of String--------");
print("Length of String : ",s1.length(str1));

print("--------Join Strings--------\n");
s1.join(s2);
print("Join strings : ",s1.get());

print("--------Compare Strings--------\n");
print("Compare string : ",s1.compare(str1,str2));
if(s1.compare(str1,str2)):
    print("String same");
else:
    print("String is not same");

print("\n--------Reverse String--------");
print("Reverse String : ",s1.reverse(str1));


print("\n--------Palindrome String or not--------");
if(s1.palindrome(str1)):
        print("Palindrome string");
else:
        print("not palindrome string");


print("\n--------Word in String----------");

str3=input("Enter String : ");
word=input("Enter word : ");
if(s1.wordinsen(str3,word)):
    print("Word found");
else:
    print("Word not found");
