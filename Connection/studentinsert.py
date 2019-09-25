import mysql.connector;
from mysql.connector import Error;

try:
    con=mysql.connector.connect(host="localhost",database="sample",user="root",passwd="");
    print("Establishing connection sample : ",con);
    rno=input("Enter rollno : ");
    nm=input("Enter name : ");
    sem=input("Enter semester : ");
    gen=input("Enter gender : ");
    if gen=="male" or gen=="Male":
        gender="1";
    elif gen=="female" or gen=="Female":
        gender="0";
    else:
        print("Enter either male or female");
        #break;
        exit(0);
    
    p_marks=input("Enter Python marks : ");
    j_marks=input("Enter Java marks : ");
    ph_marks=input("Enter PHP marks : ");
    
    queryInsertTable="Insert into student values(";
    queryInsertTable=queryInsertTable+rno+",";
    queryInsertTable=queryInsertTable+"'"+nm+"',";
    queryInsertTable=queryInsertTable+sem+",";
    queryInsertTable=queryInsertTable+"'"+gender+"',";
    queryInsertTable=queryInsertTable+p_marks+",";
    queryInsertTable=queryInsertTable+j_marks+",";
    queryInsertTable=queryInsertTable+ph_marks+")";
    
    #print(queryCreateTable);
    cursor=con.cursor();
    result=cursor.execute(queryInsertTable);
    con.commit();
    #cursor.execute(queryCreateTable);
    print("Student data inserted succefully");
except Error as e:
    print("Error : ",e);
finally:
    if(con.is_connected()):
        cursor.close();
        con.close();
