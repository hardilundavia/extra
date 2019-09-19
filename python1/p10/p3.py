class Bank:
    int1 = 4;
    n=0;
    def __init__(self):
        Bank.n = Bank.n+1;
        
    @staticmethod
    def noobj():
        print("no of object : ",Bank.n);
        
    @classmethod
    def set(cls):
        cls.int1+=1;
        
b1 =Bank();
print("interest of b1 : ",b1.int1);
b1.set();
print("interest of b1 : ",b1.int1);
b2=Bank();
Bank.noobj();

    
