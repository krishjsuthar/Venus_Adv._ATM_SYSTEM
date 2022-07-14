import mysql.connector as sql
conn=sql.connect(host='127.0.0.1',user='root',password='*****',database='  atm_machine')
if conn.is_connected():
      print("sucessfully connected")
c1=conn.cursor()
mn="CREATE TABLE RECORDS( MEMBER_ID  INT(4) primary key,PASSWORD INT(3),NAME VARCHAR(20),CREDIT_AMT INT default(0),WITHDRAWL INT default(0),BALANCE INT default(0))"
c1.execute(mn)
print("Sucessfulluy created")
