class BankAccount:
    intrest_rate=4;
    def set(self):
        self.ac_no=int(input("Enter Account Number :"));
        self.ac_name=input("Enter Account Name :");
        self.balance=int(input("Enter Balance :"));
    def show(self):
        print("Ac_no\tAc_name\tBalance");
        print(self.ac_no,"\t",self.ac_name,"\t",self.balance);
    def deposite(self):
        w=int(input("Enter Deposited Amount :"));
        self.balance=self.balance+w;
        self.show();
    def withdraw(self):
        w=int(input("Enter Withdraw Amount :"));
        if self.balance < w:
            print("Insufficient Balance");
            return;
        else:
            self.balance=self.balance-w;
        self.show();
    def calc_intrest_rate(self):
        self.balance = self.balance + (self.balance * self.intrest_rate)/100;
        self.show();
b1=BankAccount();
b2=BankAccount();
b1.set();
b1.show();
b1.deposite();
b1.withdraw();
b1.calc_intrest_rate();

print("New Object b2");
b2.set();
b2.show();
b2.deposite();
b2.withdraw();
b2.calc_intrest_rate();
