def menu():
    print("....MENU....");
    print("1.String Length");
    print("2.Join Strings");
    print("3.Compare String");
    print("4.Reverse String");
    print("5.Check string is palindrome or not");
    print("6.Check word in sentence");
    print("7.Exit");

def getchoice():
   
    print("...collecting choice from user...");
    ch = int(input("Enter your choice : "));
    return ch;


            
def string_length():
    string = input("Enter string : ");
    print(string);
    print(len(string));

def join_string():
    string1 = input("Enter String 1 : ");
    string2 = input("Enter string 2 : ");
    print(string1+string2);

def compare_string():
    s1 = input("Enter String 1 : ");
    s2 = input("Enter string 2 : ");
    if(s1==s2):
        print("both string are same..");
    else:
        print("both are not same...");

def Rev_str():
    s1 = input("Enter String 1 : ");
    print(s1[::-1]);

def str_pal():
    s1 = input("Enter String 1 : ");
    if(s1==s1[::-1]):
        print("String is palindrome");
    else:
        print("String is not palindrome");
    
def count_word():
    s1 = input("Enter sentence : ");
    lst = s1.split(' ');
    print(lst);
    print(len(lst));
   


def perform_operation(ch):
    if ch == 1:
        print("...String Length...");
        string_length();
    elif ch == 2:
        print("...Join String...");
        join_string();
    elif ch == 3:
        print("...Compare String...");
        compare_string();
    elif ch == 4:
        print("...Reverse String...");
        Rev_str();
    elif ch == 5:
        print("Check string is palindrome or not");
        str_pal();
    elif ch ==6 :
        print("check word in sentence");
        count_word();




menu();
choice = getchoice();
perform_operation(choice);
print("Bye...");

    
