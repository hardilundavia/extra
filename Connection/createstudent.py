import mysql.connector;
from mysql.connector import Error;

try:
    con=mysql.connector.connect(host="localhost",database="sample",user="root",passwd="");
    print("Establishing connection sample : ",con);
    queryCreateTable="Create table student(";
    queryCreateTable=queryCreateTable+"rno int not null,name varchar(40)not null,sem int not null,gender boolean not null,py_marks int not null,j_marks int not null,php_marks int not null,total_marks int,grade varchar(10),percentage decimal(5,2))";
    print(queryCreateTable);
    cursor=con.cursor();
    cursor.execute(queryCreateTable);
    print("Table student created succefully");
except Error as e:
    print("Error : ",e);
finally:
    if(con.is_connected()):
        cursor.close();
        con.close();
