import mysql.connector;
from mysql.connector import Error;

try:
    con=mysql.connector.connect(host="localhost",database="sample",user="root",passwd="");
    print("Establishing connection sample : ",con);

except Error as e:
    print("Error while connecting to sample");
