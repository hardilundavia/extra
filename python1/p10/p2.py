class Bank:
    int1 = 4;
    @classmethod
    def set(cls):
        cls.int1+=1;
        
b1 =Bank();
print("interest of b1 : ",b1.int1);
b1.set();
print("interest of b1 : ",b1.int1);

    
