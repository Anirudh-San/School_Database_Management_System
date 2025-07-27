import mysql.connector
from datetime import date
from tabulate import tabulate
con=mysql.connector.connect(host="localhost", user="root", password="1234", database="project")
if con.is_connected():
    cur=con.cursor()
else:
    print("Connection Failed")
Q1="create table Student (GRno int(4) primary key, Name varchar(20), Gender char(1), DOB date, BusNo integer, Class varchar(4), Division char(1), Phymk int(3), Chemmk int(3), Biomk int(3), Engmk int(3), Mathmk int(3), SSmk int(3))"
cur.execute(Q1)
Q2='insert into student values(1000, "Aaron Sypher", "M", "2005-04-22", 57, "IX", "V", 92, 98, 95, 94, 97, 99)'
Q3='insert into student values(1001, "Abhiram Sankar", "M", "2000-05-12", 57, "X", "D", 91, 90, 88, 93, 95, 97)'
Q4='insert into student values(1002, "Abhjit Shekar", "M", "2000-09-13", 57, "X", "T", 90, 94, 98, 75,93, 97)'
Q5='insert into student values(1003, "Arjit Kumar", "M", "2005-04-22", 57, "X", "Q", 23, 45, 64, 65, 75, 54)'
Q6='insert into student values(1004, "Evie Frye", "F", "2006-06-14", 57, "IX", "D", 92, 89, 79,78, 99, 96)'
Q7='insert into student values(1005, "Ezio Auditore", "M", "2004-02-29", 57, "X", "E", 50, 50, 50, 50, 50, 50)'
Q8='insert into student values(1006, "Adarsh Anilkumar", "M", "2002-04-30", 57, "VIII", "P", 56, 54, 72, 64, 65, 69)'
Q9='insert into student values(1007, "Nandakumar Anilkumar", "M", "2006-03-24", 57, "VII", "U", 56, 98, 95, 94, 97, 99)'
Q10='insert into student values(1008, "Nathan Drake", "M", "2003-01-01", 57, "X", "M", 25, 34, 42, 51, 60, 71)'
Q11='insert into student values(1009, "Alexandra Sypher", "F", "2004-11-2", 57, "VIII", "A",71, 73, 78 ,81, 85, 82)'
Q12='insert into student values(1010, "Arno Dorian", "M", "2002-12-25", 57, "VI", "H", 52, 82, 61, 75, 89, 80)'
Q13='insert into student values(1011, "Alex Dunphy", "F", "2003-10-07", 57, "IX", "V", 92, 99, 97, 95, 97, 99)'
Q14='insert into student values(1012, "Elise DeLaSerre", "F", "2004-07-10", 57, "VI", "R", 64, 72, 75, 71, 74, 77)'
Q15='insert into student values(1013, "Jack Sparrow", "M", "2001-07-2", 57, "X", "S", 19, 21, 26, 27, 22, 24 )'
Q16='insert into student values(1014, "Jon Moxley", "M", "2002-03-24", 57, "IX", "G", 34, 37, 42, 35, 50, 34)'
Q17='insert into student values(1015, "Mefuenmwehe Osas", "M", "2005-02-6", 57, "X", "F", 67, 75, 82, 83, 80, 85)'
cur.execute(Q2)
cur.execute(Q3)
cur.execute(Q4)
cur.execute(Q5)
cur.execute(Q6)
cur.execute(Q7)
cur.execute(Q8)
cur.execute(Q9)
cur.execute(Q10)
cur.execute(Q11)
cur.execute(Q12)
cur.execute(Q13)
cur.execute(Q14)
cur.execute(Q15)
cur.execute(Q16)
cur.execute(Q17)
con.commit()
print("Table 'Student' Created")
