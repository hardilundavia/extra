import mysql.connector;
from mysql.connector import Error;
try:
    con = mysql.connector.connect(host="localhost",database="sample",user="root",password="");
    query = "select * from student";
    print(query);

    cursor = con.cursor();
    result = cursor.execute(query);
    resultset = cursor.fetchall();
    print("RollNo\tName\tGender\n")
    for row in resultset:
        if row[3] ==1:
            gen = "Male";
        else:
            gen = "Female";
        print(row[0],"\t",row[1],"\t",gen);
except Error as e:
    print("Error while connecting to mydb =",e);
print("Bye...");
