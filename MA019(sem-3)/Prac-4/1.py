def printchoice():
    print("1.String length");
    print("2.Join Strings");
    print("3.Compare Strings");
    print("4.Reverse Strings");
    print("5.Palindrome Strings");
    print("6.Check word in sentence");
    ch=int(input("Enter your choice : "));
    return ch;
def lengthstring(str):
    return len(str);

def joinstring(str1,str2):
    return str1+str2;

def comparestring(str1,str2):
    return str1==str2;

def reversestring(str):
    return str[::-1];

def palindromestring(str):
    return str==str[::-1];

def wordinsen(str,word):
    return word in str;

ch=printchoice();
if(ch==1):
    str=input("Enter String : ");
    print("Length : ",lengthstring(str));

elif(ch==2):
    str1=input("Enter String 1 : ");
    str2=input("Enter String 2 : ");
    print("Concated string : ",joinstring(str1,str2));

elif(ch==3):
    str1=input("Enter String 1 : ");
    str2=input("Enter String 2 : ");
    print("Compare string : ",comparestring(str1,str2));
    if(comparestring(str1,str2)):
        print("String same");
    else:
        print("String is not same");
elif(ch==4):
    str=input("Enter String : ");
    print("Reverse String : ",reversestring(str));

elif(ch==5):
    str=input("Enter String : ");
    if(palindromestring(str)):
        print("Palindrome string");
    else:
        print("not palindrome string");
elif(ch==6):
    str=input("Enter String : ");
    word=input("Enter word : ");
    if(wordinsen(str,word)):
        print("Word found");
    else:
        print("Word not found");
