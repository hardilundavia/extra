import mysql.connector;
from mysql.connector import Error;

try:
    con=mysql.connector.connect(host="localhost",database="sample",user="root",passwd="");
    print("Establishing connection sample : ",con);
    queryCreateTable="Create table person(";
    queryCreateTable=queryCreateTable+"name varchar(30)not null,age int not null)";
    print(queryCreateTable);
    cursor=con.cursor();
    cursor.execute(queryCreateTable);
    print("Table person created succefully");
except Error as e:
    print("Error : ",e);
finally:
    if(con.is_connected()):
        cursor.close();
        con.close();
