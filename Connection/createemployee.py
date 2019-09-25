import mysql.connector;
from mysql.connector import Error;

try:
    con=mysql.connector.connect(host="localhost",database="sample",user="root",passwd="");
    print("Establishing connection sample : ",con);
    queryCreateTable="Create table employee(";
    queryCreateTable=queryCreateTable+"eno int not null,ename varchar(40)not null,gender boolean not null,py_marks int not null,dob date not null,jdate date not null,basicsal int not null,da int,hra int,netsal int)";
    print(queryCreateTable);
    cursor=con.cursor();
    cursor.execute(queryCreateTable);
    print("Table employee created succefully");
except Error as e:
    print("Error : ",e);
finally:
    if(con.is_connected()):
        cursor.close();
        con.close();
