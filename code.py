import mysql.connector
from datetime import date
from tabulate import tabulate
con=mysql.connector.connect(host="localhost", user="root", password="1234", database="project")
if con.is_connected():
    cur=con.cursor()
    cpd="1234"
    while True:
        pd=input("Enter the Administrative Password: ")
        if pd==cpd:
                print('\n'+"Password Accepted, Loading Main Menu.....",end="\n \n")
                for i in range (9000000):
                    pass
                break
        else:
            print ("Incorrect Password, would you like to retry?")
            retry=input("Yes(Y)/No(N): ")
            if not retry.lower() in ["yes","y","true",""]:
                exit()
    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    print()
    print("\t \t \t \t \t   ＳＣＨＯＯＬ　ＭＡＮＡＧＥＭＥＮＴ")
    print("\t \t \t \t \t  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    while True:
        def MainMenu():
            while True:
                print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
                print()
                print("⌂ Main Menu:")
                print("  ‾‾‾‾‾‾‾‾‾")
                print("1. New Admission")
                print("2. View Student Records")
                print("3. View Student Statistics")
                print("4. Edit Student Records")
                print("5. Delete Student Records")
                print("6. Exit")
                print()
                choice=input("Enter Your Choice : ")
                print()
                if choice not in ("1","2", "3", "4", "5", "6"):
                    print()
                    print("❗Please enter a valid option by its number from the above list!")
                    print("  ════════════════════════════════════════════════════════════════")
                    print()
                    continue
                return choice
                break
        choice=int(MainMenu())
        if choice==1:
            def NewAdm():
                while True:
                    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
                    print("\t \t \t \t \t    _____________")
                    print("\t \t \t \t \t  + NEW ADMISSION")
                    print("\t \t \t \t \t    ‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
                    while True:
                        gr1=input("Enter the G.R. number of the student: ")
                        if len(gr1)!=4 or not gr1.isdigit():
                            print()
                            print("❗Please enter a valid G.R. Number consisting of 4 digits.")
                            print("  ══════════════════════════════════════════════════════════")
                            continue
                        Q1="Select * from Student where grno={}".format(gr1)
                        cur.execute(Q1)
                        grcheck=cur.fetchall()
                        if not grcheck:
                            gr=int(gr1)
                            break
                        else:
                            print()
                            print("❗A student with that G.R. number already exists. Please enter another G.R. number.")
                            print("  ═══════════════════════════════════════════════════════════════════════════════════")
                            continue
                    while True:
                        nm1=input("Enter the name of the Student: ")
                        if not all(char.isalpha() or char.isspace() for char in nm1) or nm1==" " or nm1=="": 
                            print()
                            print("❗Please enter the legal and full name of the student")
                            print("  ═════════════════════════════════════════════════════")
                            continue
                        nm=nm1
                        break
                    while True:
                        gen1=input("Enter the gender of the Student (M/F): ").upper()
                        if len(gen1)!=1 or not gen1.isalpha() or gen1 not in ["M","F"]:
                            print()
                            print("❗Please enter only either m/M for male and f/F for female.")
                            print("  ═══════════════════════════════════════════════════════════")
                            continue
                        gen=gen1
                        break
                    while True:
                        y1=input("Enter the year of birth of the student: ")
                        if len(str(y1))!=4 or not y1.isdigit() or int(y1)>2022:
                            print()
                            print("❗Please enter a valid year consisting of 4 digits.")
                            print("  ═══════════════════════════════════════════════════")
                            continue
                        y=int(y1)
                        break
                    while True:
                        m1=input("Enter the month of birth of the student (number): ")
                        if not str(m1).isdigit() or int(m1)>12 or int(m1)<1:
                            print()
                            print("❗Please enter a valid month by its number")
                            print("  ═══════════════════════════════════════════")
                            continue
                        m=int(m1)
                        break
                    def leap(Y):
                        x=0
                        if (Y%4 == 0 and Y%100 != 0) or (Y%400 == 0):
                            x=1
                        return x
                    while True:
                        d1=input("Enter the date of birth of the student: ")
                        if not str(d1).isdigit() or int(d1)>31 or int(d1)<1:
                            print()
                            print("❗Please enter a valid date for the entered month")
                            print("  ═════════════════════════════════════════════════")
                            continue
                        if m in [4,6,9,11] and int(d1)>30:
                            print()
                            print("❗The Entered month does not have more that 30 days... please enter a valid date")
                            print("  ════════════════════════════════════════════════════════════════════════════════")
                            continue
                        if m==2 and int(d1)>29:
                            print()
                            print("❗February at maximum only has 29 days... please enter a valid date")
                            print("  ═══════════════════════════════════════════════════════════════════")
                            continue
                        if m==2 and int(d1)>28 and leap(int(y))==0:
                            print()
                            print("❗February only has 28 days in the entered year... please enter a valid date")
                            print("  ════════════════════════════════════════════════════════════════════════════")
                            continue
                        d=int(d1)
                        break
                    while True:
                        bno1=input("Enter the Bus number of the student: ")
                        if not bno1.isdigit():
                            print()
                            print("❗Please enter a valid bus number.")
                            print("  ══════════════════════════════════")
                            continue
                        bno=int(bno1)
                        break
                    while True:
                        cl1=input("Enter the class of the Student in roman numerals (grade only): ").upper()
                        if not cl1 in ['I','II','III','IV','V','VI','VII','VIII',"X","IX"] and not cl1 in ["XI","XII"]:
                            print()
                            print("❗Please enter a valid grade in the roman numeral format")
                            print("  ════════════════════════════════════════════════════════")
                            continue
                        if cl1 in ["XI","XII"]:
                            print()
                            print("❗Sorry, we do not store data of students above the 10th grade.")
                            print("  ═══════════════════════════════════════════════════════════════")
                            continue
                        cl=cl1
                        break
                    while True:
                        div1=input("Enter the class division of the Student: ").upper()
                        if len(div1)!=1 or not div1.isalpha():
                            print()
                            print("❗Please enter a valid class division.")
                            print("  ══════════════════════════════════════")
                            continue
                        div=div1
                        break
                    while True:                       
                        pm1=input("Enter the marks obtained by the student in Physics: ")
                        if not all(char.isdigit() or char=="." for char in pm1) or pm1=="":
                            print()
                            print("❗Please enter valid marks.")
                            print("  ═══════════════════════════")
                            continue
                        if float(pm1)>100 or float(pm1)<1:
                            print()
                            print("❗Please enter valid marks.")
                            print("  ═══════════════════════════")
                        pm=float(pm1)
                        break
                    while True:                       
                        cm1=input("Enter the marks obtained by the student in Chemistry: ")
                        if not all(char.isdigit() or char=="." for char in cm1) or cm1=="":
                            print()
                            print("❗Please enter valid marks.")
                            print("  ═══════════════════════════")
                            continue
                        if float(cm1)>100 or float(cm1)<1:
                            print()
                            print("❗Please enter valid marks.")
                            print("  ═══════════════════════════")
                        cm=float(cm1)
                        break
                    while True:                       
                        bm1=input("Enter the marks obtained by the student in Biology: ")
                        if not all(char.isdigit() or char=="." for char in bm1) or bm1=="":
                            print()
                            print("❗Please enter valid marks.")
                            print("  ═══════════════════════════")
                            continue
                        if float(bm1)>100 or float(bm1)<1:
                            print()
                            print("❗Please enter valid marks.")
                            print("  ═══════════════════════════")
                        bm=float(bm1)
                        break
                    while True:                       
                        em1=input("Enter the marks obtained by the student in English: ")
                        if not all(char.isdigit() or char=="." for char in em1) or em1=="":
                            print()
                            print("❗Please enter valid marks.")
                            print("  ═══════════════════════════")
                            continue
                        if float(em1)>100 or float(em1)<1:
                            print()
                            print("❗Please enter valid marks.")
                            print("  ═══════════════════════════")
                        em=float(em1)
                        break
                    while True:                       
                        mm1=input("Enter the marks obtained by the student in Mathematics: ")
                        if not all(char.isdigit() or char=="." for char in mm1) or mm1=="":
                            print()
                            print("❗Please enter valid marks.")
                            print("  ═══════════════════════════")
                            continue
                        if float(mm1)>100 or float(mm1)<1:
                            print()
                            print("❗Please enter valid marks.")
                            print("  ═══════════════════════════")
                        mm=float(mm1)
                        break
                    while True:                       
                        sm1=input("Enter the marks obtained by the student in Social Science: ")
                        if not all(char.isdigit() or char=="." for char in sm1) or sm1=="":
                            print()
                            print("❗Please enter valid marks.")
                            print("  ═══════════════════════════")
                            continue
                        if float(sm1)>100 or float(sm1)<1:
                            print()
                            print("❗Please enter valid marks.")
                            print("  ═══════════════════════════")
                        sm=float(sm1)
                        break                 
                    dt=date(y,m,d)
                    Q1="Insert into Student values({},'{}','{}','{}',{},'{}','{}',{},{},{},{},{},{})".format(gr,nm,gen,dt,bno,cl,div,pm,cm,bm,em,mm,sm)
                    NewRec=[["G.R."+"\n no.", "Name", "Gender", "D.O.B.","Bus"+"\n No.", "Class", "Division", "Physics"+"\n marks","Chemistry"+"\n marks","Biology"+"\n marks","English"+"\n marks","Mathematics"+"\n marks","Social"+"\n Science"+"\n marks"],[gr,nm,gen,dt,bno,cl,div,pm,cm,bm,em,mm,sm]]
                    print(tabulate(NewRec, headers='firstrow', tablefmt='fancy_grid'))
                    print()
                    cnfrm1=input("Are you sure you would like to Add this record to the Student Table? (Yes(Y)/No(N)): ").lower()
                    if cnfrm1 in ["yes","y","true", ""]:
                        cur.execute(Q1)
                        con.commit()
                        print("_________________________________")
                        print("Student Record Sucessfully added!")
                        print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    else:
                        print("__________________")
                        print("Process Cancelled.")
                        print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    cend1=input("Do you want to enter more records? (Yes(Y)/No(N)):").lower()
                    if cend1 not in ["yes","y","true",""]:
                        break                                                                                      
            NewAdm()
        if choice==2:
            def ViewRec():
                while True:
                    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
                    print("\t \t \t \t \t     ____________________")
                    print("\t \t \t \t \t  👁 VIEW STUDENT RECORDS")
                    print("\t \t \t \t \t     ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    while True:
                        print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
                        print()
                        print("► How would you like to view Student Records?")
                        print("  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        print("A. By G.R. Number")
                        print("B. By Name Of Student / Resemblance to Name of Student")
                        print("C. By Bus Number")
                        print("D. By Class and/or Division [Leave criterias blank to see all students]")
                        print("E. Return To Main Menu")
                        print()
                        c2=input("Enter choice: ").upper()
                        if c2 not in ["A","B","C","D","E"]:
                            print()
                            print("❗Please enter a valid option by the alphabet from the above list!")
                            print("  ══════════════════════════════════════════════════════════════════")
                            print()
                            continue
                        break
                    if c2=="A":
                        while True:
                            print()
                            ingr1=input("Enter the G.R. number of the student: ")
                            if len(ingr1)!=4 or not ingr1.isdigit():
                                print()
                                print("❗Please enter a valid G.R. Number consisting of 4 digits.")
                                print("  ══════════════════════════════════════════════════════════")
                                continue
                            ingr=int(ingr1)
                            break
                        Q2="Select * from student where GRno={}".format(ingr)
                        cur.execute(Q2)
                        of2=cur.fetchall()
                        if not of2:
                            print()
                            print("❗No Student record with the given specifications exists.")
                            print("  ═════════════════════════════════════════════════════════")
                            print()
                        else:
                            of2.insert(0,("G.R."+"\n no.", "Name", "Gender", "D.O.B.","Bus"+"\n No.", "Class", "Division", "Physics"+"\n marks","Chemistry"+"\n marks","Biology"+"\n marks","English"+"\n marks","Mathematics"+"\n marks","Social"+"\n Science"+"\n marks"))
                            print(tabulate(of2, headers='firstrow', tablefmt='fancy_grid'))
                            print()
                            
                                                    
                    if c2=="B":
                        while True:
                            print()
                            nm1=input("Enter the name of the Student: ")
                            if not all(char.isalpha() or char.isspace() for char in nm1): 
                                print()
                                print("❗Please enter the legal and full name of the student")
                                print("  ═════════════════════════════════════════════════════")
                                continue
                            nm=nm1
                            break
                        Q2="Select * from student where Name like '%{}%'".format(nm)
                        cur.execute(Q2)
                        of2=cur.fetchall()
                        if not of2:
                            print()
                            print("❗No Student record with the given specifications exists.")
                            print("  ═════════════════════════════════════════════════════════")
                            print()
                        else:
                            of2.insert(0,("G.R."+"\n no.", "Name", "Gender", "D.O.B.","Bus"+"\n No.", "Class", "Division", "Physics"+"\n marks","Chemistry"+"\n marks","Biology"+"\n marks","English"+"\n marks","Mathematics"+"\n marks","Social"+"\n Science"+"\n marks"))
                            print(tabulate(of2, headers='firstrow', tablefmt='fancy_grid'))
                            print()                           
                    if c2=="C":
                        while True:
                            print()
                            bno1=input("Enter the Bus number of the student: ")
                            if not bno1.isdigit():
                                print()
                                print("❗Please enter a valid bus number.")
                                print("  ══════════════════════════════════")
                                continue
                            bno=int(bno1)
                            break
                        Q2="Select * from student where BusNo={}".format(bno)
                        cur.execute(Q2)
                        of2=cur.fetchall()
                        if not of2:
                            print()
                            print("❗No Student record with the given specifications exists.")
                            print("  ═════════════════════════════════════════════════════════")
                            print()
                        else:
                            of2.insert(0,("G.R."+"\n no.", "Name", "Gender", "D.O.B.","Bus"+"\n No.", "Class", "Division", "Physics"+"\n marks","Chemistry"+"\n marks","Biology"+"\n marks","English"+"\n marks","Mathematics"+"\n marks","Social"+"\n Science"+"\n marks"))
                            print(tabulate(of2, headers='firstrow', tablefmt='fancy_grid'))
                            print()
                    if c2=="D":
                        while True:
                            print()
                            cl1=input("Enter the class (grade only) of the Student in roman numerals [Leave blank to see all classes]: ").upper()
                            if not cl1 in ['I','II','III','IV','V','VI','VII','VIII',"X","IX",""] and not cl1 in ["XI","XII"]:
                                print()
                                print("❗Please enter a valid grade in the roman numeral format")
                                print("  ════════════════════════════════════════════════════════")
                                continue
                            if cl1 in ["XI","XII"]:
                                print()
                                print("❗Sorry, we do not store data of students above the 10th grade.")
                                print("  ═══════════════════════════════════════════════════════════════")
                                continue
                            cl=cl1
                            break
                        while True:
                            print()
                            div1=input("Enter the class division of the Student [Leave blank to see all divisions]: ").upper()
                            if len(div1)>1 or not div1.isalpha() and div1!="":
                                print()
                                print("❗Please enter a valid class division.")
                                print("  ══════════════════════════════════════")
                                continue
                            div=div1
                            break
                        if cl1!="" and div1!="":
                            Q2="Select * from student where class='{}' and division='{}'".format(cl1, div1)
                        if cl1=="" and div1!="":
                            Q2="Select * from student where division='{}'".format(div1)
                        if cl1!="" and div1=="":
                            Q2="Select * from student where class='{}'".format(cl1)
                        if cl1=="" and div1=="":
                            Q2="Select * from student"
                        cur.execute(Q2)
                        of2=cur.fetchall()                    
                        if not of2:
                            print()
                            print("❗No Student record with the given specifications exists.")
                            print("  ═════════════════════════════════════════════════════════")
                            print()
                        else:
                            of2.insert(0,("G.R."+"\n no.", "Name", "Gender", "D.O.B.","Bus"+"\n No.", "Class", "Division", "Physics"+"\n marks","Chemistry"+"\n marks","Biology"+"\n marks","English"+"\n marks","Mathematics"+"\n marks","Social"+"\n Science"+"\n marks"))
                            print(tabulate(of2, headers='firstrow', tablefmt='fancy_grid'))
                            print()
                    if c2=="E":
                        break
                    print()                
                    cend2=input("Do you want to view more student records? (Yes(Y)/No(N)):").lower()
                    if cend2 not in ["yes","y","true",""]:
                        break           
            ViewRec()
        if choice==3:
            def ViewStat():
                while True:
                    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
                    print("\t \t \t \t \t    _______________________") 
                    print("\t \t \t \t \t  ░ VIEW STUDENT STATISTICS")
                    print("\t \t \t \t \t    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    while True:
                        print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
                        print()
                        print("► What Statistic Would You Like To View?")
                        print("  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        print("A. Display Highest, Lowest and Average marks for a Subject in a grade")
                        print("B. Display Progress Report of a particular student")
                        print("C. Display Percentage Rankings for a grade.")
                        print("D. Return To Main Menu")
                        print()
                        c3=input("Enter choice: ").upper()
                        if c3 not in ["A","B","C","D"]:
                                print()
                                print("❗Please enter a valid option by the alphabet from the above list!")
                                print("  ══════════════════════════════════════════════════════════════════")
                                print()
                                continue
                        break
                    if c3=="A":
                        while True:
                                print()
                                cl1=input("Enter the grade in roman numerals [Leave blank to see data grouped by classes]: ").upper()
                                if not cl1 in ['I','II','III','IV','V','VI','VII','VIII',"X","IX",""] and not cl1 in ["XI","XII"]:
                                    print()
                                    print("❗Please enter a valid grade in the roman numeral format")
                                    print("  ════════════════════════════════════════════════════════")
                                    continue
                                if cl1 in ["XI","XII"]:
                                    print()
                                    print("❗Sorry, we do not store data of students above the 10th grade.")
                                    print("  ═══════════════════════════════════════════════════════════════")
                                    continue
                                cl=cl1
                                break
                        while True:
                            print()
                            print("► Which Subject's Statistics Would You Like To View?")
                            print("  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾") 
                            print("1. Physics")
                            print("2. Chemistry")
                            print("3. Biology")
                            print("4. English")
                            print("5. Mathematics")
                            print("6. Social Science")
                            print("7. All")
                            print()
                            c3sub1=input("Enter your choice: ")
                            if c3sub1 not in ("1","2", "3", "4", "5", "6","7"):
                                print()
                                print("❗Please enter a valid option by its number from the above list!")
                                print("  ════════════════════════════════════════════════════════════════")
                                print()
                                continue
                            if c3sub1=='1':
                                c3sub="phymk"
                            if c3sub1=="2":
                                c3sub="chemmk"
                            if c3sub1=="3":
                                c3sub1="biomk"
                            if c3sub1=="4":
                                c3sub="engmk"
                            if c3sub1=="5":
                                c3sub="mathmk"
                            if c3sub1=="6":
                                c3sub="ssmk"
                            if c3sub1=="7":
                                c3sub=7
                            break
                        print("♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠")
                        print("_____________")
                        print("HIGHEST MARKS")
                        print("‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        if cl!="" and c3sub!=7:
                            Q3="select class, max({}) from student where class='{}'".format(c3sub,cl)
                            cur.execute(Q3)
                            of31=cur.fetchall()                  
                            of31.insert(0,("Class", "{}".format(c3sub)+"\n marks"))
                            print(tabulate(of31, headers='firstrow', tablefmt='fancy_grid'))
                            print()
                        if cl=="" and c3sub!=7:
                            Q3="select class, max({}) from student group by class".format(c3sub)
                            cur.execute(Q3)
                            of31=cur.fetchall()                  
                            of31.insert(0,("Class", "{}".format(c3sub)+"\n marks"))
                            print(tabulate(of31, headers='firstrow', tablefmt='fancy_grid'))
                            print()
                        if cl!="" and c3sub==7:
                            Q3="select class, max(phymk) as 'Physics marks', max(chemmk) as 'Chemistry marks', max(biomk) as 'Biology marks',max(engmk) as 'English marks',max(mathmk) as 'Mathematics marks',max(ssmk) as 'Social Science marks'  from student where class='{}'".format(cl)
                            cur.execute(Q3)
                            of31=cur.fetchall()                  
                            of31.insert(0,("Class", "Physics"+"\n marks","Chemistry"+"\n marks","Biology"+"\n marks","English"+"\n marks","Mathematics"+"\n marks","Social"+"\n Science"+"\n marks" ))
                            print(tabulate(of31, headers='firstrow', tablefmt='fancy_grid'))
                            print()
                        if cl=="" and c3sub==7:
                            Q3="select class, max(phymk) as 'Physics marks', max(chemmk) as 'Chemistry marks', max(biomk) as 'Biology marks',max(engmk) as 'English marks',max(mathmk) as 'Mathematics marks',max(ssmk) as 'Social Science marks'  from student group by class"
                            cur.execute(Q3)
                            of31=cur.fetchall()                  
                            of31.insert(0,("Class", "Physics"+"\n marks","Chemistry"+"\n marks","Biology"+"\n marks","English"+"\n marks","Mathematics"+"\n marks","Social"+"\n Science"+"\n marks" ))
                            print(tabulate(of31, headers='firstrow', tablefmt='fancy_grid'))
                            print()
                        print("♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠")
                        print("_____________")
                        print("LOWEST MARKS")
                        print("‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        if cl!="" and c3sub!=7:
                            Q3="select class, min({}) from student where class='{}'".format(c3sub,cl)
                            cur.execute(Q3)
                            of32=cur.fetchall()                  
                            of32.insert(0,("Class", "{}".format(c3sub)+"\n marks"))
                            print(tabulate(of32, headers='firstrow', tablefmt='fancy_grid'))
                            print()
                        if cl=="" and c3sub!=7:
                            Q3="select class, min({}) from student group by class".format(c3sub)
                            cur.execute(Q3)
                            of32=cur.fetchall()                  
                            of32.insert(0,("Class", "{}".format(c3sub)+"\n marks"))
                            print(tabulate(of32, headers='firstrow', tablefmt='fancy_grid'))
                            print()
                        if cl!="" and c3sub==7:
                            Q3="select class, min(phymk) as 'Physics marks', min(chemmk) as 'Chemistry marks', min(biomk) as 'Biology marks',min(engmk) as 'English marks',min(mathmk) as 'Mathematics marks',min(ssmk) as 'Social Science marks'  from student where class='{}'".format(cl)
                            cur.execute(Q3)
                            of32=cur.fetchall()                  
                            of32.insert(0,("Class", "Physics"+"\n marks","Chemistry"+"\n marks","Biology"+"\n marks","English"+"\n marks","Mathematics"+"\n marks","Social"+"\n Science"+"\n marks" ))
                            print(tabulate(of32, headers='firstrow', tablefmt='fancy_grid'))
                            print()
                        if cl=="" and c3sub==7:
                            Q3="select class, min(phymk) as 'Physics marks', min(chemmk) as 'Chemistry marks', min(biomk) as 'Biology marks',min(engmk) as 'English marks',min(mathmk) as 'Mathematics marks',min(ssmk) as 'Social Science marks'  from student group by class"
                            cur.execute(Q3)
                            of32=cur.fetchall()                  
                            of32.insert(0,("Class", "Physics"+"\n marks","Chemistry"+"\n marks","Biology"+"\n marks","English"+"\n marks","Mathematics"+"\n marks","Social"+"\n Science"+"\n marks" ))
                            print(tabulate(of32, headers='firstrow', tablefmt='fancy_grid'))
                            print()
                        print("♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠")
                        print("_____________")
                        print("AVERAGE MARKS")
                        print("‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        if cl!="" and c3sub!=7:
                            Q3="select class, avg({}) from student where class='{}'".format(c3sub,cl)
                            cur.execute(Q3)
                            of33=cur.fetchall()                  
                            of33.insert(0,("Class", "{}".format(c3sub)+"\n marks"))
                            print(tabulate(of33, headers='firstrow', tablefmt='fancy_grid'))
                            print()
                        if cl=="" and c3sub!=7:
                            Q3="select class, avg({}) from student group by class".format(c3sub)
                            cur.execute(Q3)
                            of33=cur.fetchall()                  
                            of33.insert(0,("Class", "{}".format(c3sub)+"\n marks"))
                            print(tabulate(of33, headers='firstrow', tablefmt='fancy_grid'))
                            print()
                        if cl!="" and c3sub==7:
                            Q3="select class, avg(phymk) as 'Physics marks', avg(chemmk) as 'Chemistry marks', avg(biomk) as 'Biology marks',avg(engmk) as 'English marks',avg(mathmk) as 'Mathematics marks',avg(ssmk) as 'Social Science marks'  from student where class='{}'".format(cl)
                            cur.execute(Q3)
                            of33=cur.fetchall()                  
                            of33.insert(0,("Class", "Physics"+"\n marks","Chemistry"+"\n marks","Biology"+"\n marks","English"+"\n marks","Mathematics"+"\n marks","Social"+"\n Science"+"\n marks" ))
                            print(tabulate(of33, headers='firstrow', tablefmt='fancy_grid'))
                            print()
                        if cl=="" and c3sub==7:
                            Q3="select class, avg(phymk) as 'Physics marks', avg(chemmk) as 'Chemistry marks', avg(biomk) as 'Biology marks',avg(engmk) as 'English marks',avg(mathmk) as 'Mathematics marks',avg(ssmk) as 'Social Science marks'  from student group by class"
                            cur.execute(Q3)
                            of33=cur.fetchall()                  
                            of33.insert(0,("Class", "Physics"+"\n marks","Chemistry"+"\n marks","Biology"+"\n marks","English"+"\n marks","Mathematics"+"\n marks","Social"+"\n Science"+"\n marks" ))
                            print(tabulate(of33, headers='firstrow', tablefmt='fancy_grid'))
                            print()
                    if c3=="B":
                        while True:
                            print()
                            ingr1=input("Enter the G.R. number of the student: ")
                            if len(ingr1)!=4 or not ingr1.isdigit():
                                print()
                                print("❗Please enter a valid G.R. Number consisting of 4 digits.")
                                print("  ══════════════════════════════════════════════════════════")
                                continue
                            ingr=int(ingr1)
                            break
                        Q3="select grno, name, class, division, phymk, chemmk, biomk, engmk, mathmk, ssmk, ((phymk+chemmk+biomk+engmk+mathmk+ssmk)/6) as 'Total Percentage' from student where grno={}".format(ingr)
                        cur.execute(Q3)
                        of3b=cur.fetchall()
                        if not of3b:
                            print()
                            print("❗A student with that G.R. number does not exist.")
                            print("  ════════════════════════════════════════════════")
                            print()
                        else:
                            of3b.insert(0, ("G.R."+"\n n.o", "Name", "Class", "Division", "Physics"+"\n marks","Chemistry"+"\n marks","Biology"+"\n marks","English"+"\n marks","Mathematics"+"\n marks","Social"+"\n Science"+"\n marks", "Total"+"\n Percentage"))
                            print(tabulate(of3b, headers='firstrow', tablefmt='fancy_grid'))
                            print("Note:- Maximum Marks scorable in each subject is 100.")
                            print("‾‾‾‾")
                            print()
                    if c3=="C":
                        while True:
                            print()
                            cl1=input("Enter the grade in roman numerals: ").upper()
                            if not cl1 in ['I','II','III','IV','V','VI','VII','VIII',"X","IX"] and not cl1 in ["XI","XII"]:
                                print()
                                print("❗Please enter a valid grade in the roman numeral format")
                                print("  ════════════════════════════════════════════════════════")
                                continue
                            if cl1 in ["XI","XII"]:
                                print()
                                print("❗Sorry, we do not store data of students above the 10th grade.")
                                print("  ═══════════════════════════════════════════════════════════════")
                                continue
                            cl=cl1
                            break 
                        Q3="select rank() over (order by ((phymk+chemmk+biomk+engmk+mathmk+ssmk)/6) desc) as 'Rank', grno, name, class, division, ((phymk+chemmk+biomk+engmk+mathmk+ssmk)/6) as 'Total Percentage' from student where class='{}' order by ((phymk+chemmk+biomk+engmk+mathmk+ssmk)/6) desc".format(cl)
                        cur.execute(Q3)
                        of3c=cur.fetchall()
                        if not of3c:
                            print()
                            print("❗No records of students from that grade exists!")
                            print("  ════════════════════════════════════════════════")
                            print()
                        else:
                            print()
                            of3c.insert(0, ("Rank","G.R."+"\n n.o", "Name", "Class", "Division", "Total Percentage"))
                            print(tabulate(of3c, headers='firstrow', tablefmt='fancy_grid'))        
                            print()    
                    if c3=="D":
                        break
                    cend3=input("Do you want to view more student Statistics? (Yes(Y)/No(N)):").lower()
                    if cend3 not in ["yes","y","true",""]:
                        break
                    
            ViewStat()
        if choice==4:
            def EditRec():
                while True:
                    print("☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼")
                    print("\t \t \t \t \t    ____________")
                    print("\t \t \t \t \t  ☼ EDIT RECORDS")
                    print("\t \t \t \t \t    ‾‾‾‾‾‾‾‾‾‾‾‾")
                    while True:
                        print("☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼")
                        print()
                        print("► What Would You Like To Edit?")
                        print("  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        print("A. Edit Marks")
                        print("B. Edit Bus No.")
                        print("C. Edit Name")
                        print("D. Edit Class")
                        print("E. Return To Main Menu")
                        print()
                        c4=input("Enter choice: ").upper()
                        if c4 not in ["A","B","C","D","E"]:
                            print()
                            print("❗Please enter a valid option by the alphabet from the above list! ")
                            print("  ══════════════════════════════════════════════════════════════════")
                            print()
                            continue
                        break
                    if c4=="E":
                        break
                    while True:
                            print()
                            ingr1=input("Enter the G.R. number of the student: ")
                            if len(ingr1)!=4 or not ingr1.isdigit():
                                print()
                                print("❗Please enter a valid G.R. Number consisting of 4 digits.")
                                print("  ══════════════════════════════════════════════════════════")
                                continue
                            ingr=int(ingr1)
                            break
                    if c4=="A":
                        while True:
                            while True:
                                print()
                                print("► Which Subject's Marks would you like to change?")
                                print("  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                print("1. Physics")
                                print("2. Chemistry")
                                print("3. Biology")
                                print("4. English")
                                print("5. Mathematics")
                                print("6. Social Science")
                                print()
                                c4sub1=input("Enter your choice: ")
                                if c4sub1 not in ("1","2", "3", "4", "5", "6"):
                                    print()
                                    print("❗Please enter a valid option by its number from the above list!")
                                    print("  ════════════════════════════════════════════════════════════════")
                                    print()
                                    continue
                                if c4sub1=='1':
                                    c4sub="phymk"
                                if c4sub1=="2":
                                    c4sub="chemmk"
                                if c4sub1=="3":
                                    c4sub1="biomk"
                                if c4sub1=="4":
                                    c4sub="engmk"
                                if c4sub1=="5":
                                    c4sub="mathmk"
                                if c4sub1=="6":
                                    c4sub="ssmk"
                                break
                            Q4aprev="select {} from student where grno={}".format(c4sub,ingr)
                            cur.execute(Q4aprev)
                            of4aprev=cur.fetchall()
                            prevmark=of4aprev[0][0]
                            print("original marks:", prevmark)
                            while True:
                                print()
                                newmk1=input("Enter the marks obtained by the student in Physics: ")
                                if not all(char.isdigit() or char=="." for char in newmk1):
                                    print()
                                    print("❗Please enter valid marks.")
                                    print("  ═══════════════════════════")
                                    continue
                                if float(newmk1)>100 or float(newmk1)<1:
                                    print()
                                    print("❗Please enter valid marks.")
                                    print("  ═══════════════════════════")
                                newmk=float(newmk1)
                                break
                            Q4="update Student set {}={} where grno={}".format(c4sub,newmk,ingr)
                            cur.execute(Q4)
                            Q4con="select * from student where grno={}".format(ingr)
                            cur.execute(Q4con)
                            of4a=cur.fetchall()
                            if not of4a:
                                print()
                                print("❗A student with that G.R. number does not exist.")
                                print("  ════════════════════════════════════════════════")
                                print()
                            else:
                                of4a.insert(0,("G.R."+"\n no.", "Name", "Gender", "D.O.B.","Bus"+"\n No.", "Class", "Division", "Physics"+"\n marks","Chemistry"+"\n marks","Biology"+"\n marks","English"+"\n marks","Mathematics"+"\n marks","Social"+"\n Science"+"\n marks"))
                                print()
                                print(tabulate(of4a, headers='firstrow', tablefmt='fancy_grid'))
                                print()
                                confrm=input("Is this the change you wanted? (Yes(Y)/No(N)): ").lower()
                                if confrm not in ["yes","y","true",""]:
                                    Q4cor="update Student set {}={} where grno={}".format(c4sub,prevmark,ingr)
                                    cur.execute(Q4cor)
                                    con.commit()
                                    print("__________________")
                                    print("Process Cancelled.")
                                    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                    continue
                                else:
                                    con.commit()
                                    print("___________________________")
                                    print("Record Successfully Edited!")                   
                                    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                    break
                    if c4=="B":
                        while True:
                            Q4bprev="select busno from student where grno={}".format(ingr)
                            cur.execute(Q4bprev)
                            of4bprev=cur.fetchall()
                            if not of4bprev:
                                print("❗A student with that G.R. number does not exist.")
                                print("  ════════════════════════════════════════════════")
                                continue
                            else:
                                prevbus=of4bprev[0][0]
                                print("original Bus number:", prevbus)
                            while True:
                                print()
                                bno1=input("Enter the new Bus number: ")
                                if not bno1.isdigit():
                                    print()
                                    print("❗Please enter a valid bus number.")
                                    print("  ══════════════════════════════════")
                                    continue
                                bno=int(bno1)
                                break
                            Q4="update Student set busno={} where grno={}".format(bno,ingr)
                            cur.execute(Q4)
                            Q4con="select * from student where grno={}".format(ingr)
                            cur.execute(Q4con)
                            of4b=cur.fetchall()
                            if not of4b:
                                print()
                                print("❗A student with that G.R. number does not exist.")
                                print("  ════════════════════════════════════════════════")
                                print()
                            else:
                                of4b.insert(0,("G.R."+"\n no.", "Name", "Gender", "D.O.B.","Bus"+"\n No.", "Class", "Division", "Physics"+"\n marks","Chemistry"+"\n marks","Biology"+"\n marks","English"+"\n marks","Mathematics"+"\n marks","Social"+"\n Science"+"\n marks"))
                                print()
                                print(tabulate(of4b, headers='firstrow', tablefmt='fancy_grid'))
                                print()
                                confrm=input("Is this the change you wanted? (Yes(Y)/No(N)): ").lower()
                                if confrm not in ["yes","y","true",""]:
                                    Q4cor="update Student set busno={} where grno={}".format(prevbus,ingr)
                                    cur.execute(Q4cor)
                                    con.commit()
                                    print("__________________")
                                    print("Process Cancelled.")
                                    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                    continue
                                else:
                                    con.commit()
                                    print("___________________________")
                                    print("Record Successfully Edited!")                   
                                    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ")
                                    break
                    if c4=="C":
                        while True:
                            Q4cprev="select name from student where grno={}".format(ingr)
                            cur.execute(Q4cprev)
                            of4cprev=cur.fetchall()
                            if not of4cprev:
                                print("❗A student with that G.R. number does not exist.")
                                print("  ════════════════════════════════════════════════")
                                continue
                            else:
                                prevname=of4cprev[0][0]
                                print("original name:", prevname)
                            while True:
                                print()
                                nm1=input("Enter the new name of the Student: ")
                                if not all(char.isalpha() or char.isspace() for char in nm1): 
                                    print()
                                    print("❗Please enter the legal and full name of the student")
                                    print("  ═════════════════════════════════════════════════════")
                                    continue
                                nm=nm1
                                break
                            Q4="update Student set name='{}' where grno={}".format(nm,ingr)
                            cur.execute(Q4)
                            Q4con="select * from student where grno={}".format(ingr)
                            cur.execute(Q4con)
                            of4c=cur.fetchall()
                            if not of4c:
                                print()
                                print("❗A student with that G.R. number does not exist.")
                                print("  ════════════════════════════════════════════════")
                                print()
                            else:
                                of4c.insert(0,("G.R."+"\n no.", "Name", "Gender", "D.O.B.","Bus"+"\n No.", "Class", "Division", "Physics"+"\n marks","Chemistry"+"\n marks","Biology"+"\n marks","English"+"\n marks","Mathematics"+"\n marks","Social"+"\n Science"+"\n marks"))
                                print()
                                print(tabulate(of4c, headers='firstrow', tablefmt='fancy_grid'))
                                print()
                                confrm=input("Is this the change you wanted? (Yes(Y)/No(N)): ").lower()
                                if confrm not in ["yes","y","true",""]:
                                    Q4cor="update Student set name='{}' where grno={}".format(prevname,ingr)
                                    cur.execute(Q4cor)
                                    con.commit()
                                    print("__________________")
                                    print("Process Cancelled.")
                                    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                    continue
                                else:
                                    con.commit()
                                    print("___________________________")
                                    print("Record Successfully Edited!")                   
                                    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                    break
                    if c4=="D":
                         while True:
                            Q4dprev="select class, division from student where grno={}".format(ingr)
                            cur.execute(Q4dprev)
                            of4dprev=cur.fetchall()
                            if not of4dprev:
                                print("❗A student with that G.R. number does not exist.")
                                print("  ═════════════════════════════════════════════════")
                                continue
                            else:
                                prevclass=of4dprev[0][0]
                                prevdiv=of4dprev[0][1]
                                print("original class:", prevclass)
                                print("original division:", prevdiv)
                            while True:
                                print()
                                cl1=input("Enter the new grade in roman numerals: ").upper()
                                if not cl1 in ['I','II','III','IV','V','VI','VII','VIII',"X","IX"] and not cl1 in ["XI","XII"]:
                                    print()
                                    print("❗Please enter a valid grade in the roman numeral format")
                                    print("  ════════════════════════════════════════════════════════")
                                    continue
                                if cl1 in ["XI","XII"]:
                                    print()
                                    print("❗Sorry, we do not store data of students above the 10th grade.")
                                    print("  ═══════════════════════════════════════════════════════════════")
                                    continue
                                cl=cl1
                                break
                            while True:
                                div1=input("Enter the new class division: ").upper()
                                if len(div1)!=1 or not div1.isalpha():
                                    print()
                                    print("❗Please enter a valid class division.")
                                    print("  ══════════════════════════════════════")
                                    continue
                                div=div1
                                break
                            Q4="update Student set class='{}', division='{}' where grno={}".format(cl,div,ingr)
                            cur.execute(Q4)
                            Q4don="select * from student where grno={}".format(ingr)
                            cur.execute(Q4don)
                            of4d=cur.fetchall()
                            if not of4d:
                                print()
                                print("❗A student with that G.R. number does not exist.")
                                print("  ════════════════════════════════════════════════")
                                print()
                            else:
                                of4d.insert(0,("G.R."+"\n no.", "Name", "Gender", "D.O.B.","Bus"+"\n No.", "Class", "Division", "Physics"+"\n marks","Chemistry"+"\n marks","Biology"+"\n marks","English"+"\n marks","Mathematics"+"\n marks","Social"+"\n Science"+"\n marks"))
                                print()
                                print(tabulate(of4d, headers='firstrow', tablefmt='fancy_grid'))
                                print()
                                confrm=input("Is this the change you wanted? (Yes(Y)/No(N)): ").lower()
                                if confrm not in ["yes","y","true",""]:
                                    Q4dor="update Student set name={} where grno={}".format(prevname,ingr)
                                    cur.execute(Q4dor)
                                    con.commit()
                                    print("__________________")
                                    print("Process Cancelled.")
                                    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                    continue
                                else:
                                    con.commit()
                                    print("___________________________")
                                    print("Record Successfully Edited!")                   
                                    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                    break
                    cend4=input("Do you want to Edit more Student Records? (Yes(Y)/No(N)):").lower()
                    if cend4 not in ["yes","y","true",""]:
                        break               
            EditRec()
        if choice==5:
            def DelRec():
                while True:
                    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
                    print("\t \t \t \t \t    ______________________")
                    print("\t \t \t \t \t  × DELETE STUDENT RECORDS")
                    print("\t \t \t \t \t    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                    while True:
                        print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
                        print()
                        print("► What Would You Like To Delete?")
                        print("  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                        print("A. Delete Student Record by G.R. number")
                        print("B. Delete all Student Records")
                        print("C. Return To Main Menu")
                        c5=input("Enter choice: ").upper()
                        if c5 not in ["A","B","C"]:
                            print()
                            print("❗Please enter a valid option by the alphabet from the above list!")
                            print("  ══════════════════════════════════════════════════════════════════")
                            print()
                            continue
                        break
                    if c5=="A":
                        while True:
                            while True:
                                print()
                                ingr1=input("Enter the G.R. number of the student: ")
                                if len(ingr1)!=4 or not ingr1.isdigit():
                                    print()
                                    print("❗Please enter a valid G.R. Number consisting of 4 digits.")
                                    print("  ══════════════════════════════════════════════════════════")
                                    continue
                                ingr=int(ingr1)
                                break
                            Q5prev="select * from student where grno={}".format(ingr)
                            cur.execute(Q5prev)
                            of5prev=cur.fetchall()
                            if not of5prev:
                                print("❗A student with that G.R. number does not exist.")
                                print("  ═════════════════════════════════════════════════")
                                continue
                            else:
                                of5prev.insert(0,("G.R."+"\n no.", "Name", "Gender", "D.O.B.","Bus"+"\n No.", "Class", "Division", "Physics"+"\n marks","Chemistry"+"\n marks","Biology"+"\n marks","English"+"\n marks","Mathematics"+"\n marks","Social"+"\n Science"+"\n marks"))
                                print(tabulate(of5prev, headers='firstrow', tablefmt='fancy_grid'))
                                print()
                                c5con=input("Are you sure you want to delete this record? (Yes(Y)/No(N)): ").lower()
                                if c5con in ["yes","y","true"]:
                                    Q5="Delete from Student where grno={}".format(ingr)
                                    cur.execute(Q5)
                                    con.commit()
                                    print("____________________________")
                                    print("Record Successfully Deleted!")                   
                                    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                    break
                                else:
                                    print("__________________")
                                    print("Process Cancelled.")
                                    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                    break
                        cend5=input("Do you want to Delete more Student Records? (Yes(Y)/No(N)):").lower()
                        if cend5 not in ["yes","y","true",""]:
                            break
                    if c5=="B":
                        while True:
                            Q5bprev="select * from student"
                            cur.execute(Q5bprev)
                            of5bprev=cur.fetchall()
                            if not of5bprev:
                                print("❗There is no data in the Table to be deleted.")
                                print("  ══════════════════════════════════════════════")
                                continue
                            else:
                                of5bprev.insert(0,("G.R."+"\n no.", "Name", "Gender", "D.O.B.","Bus"+"\n No.", "Class", "Division", "Physics"+"\n marks","Chemistry"+"\n marks","Biology"+"\n marks","English"+"\n marks","Mathematics"+"\n marks","Social"+"\n Science"+"\n marks"))
                                print(tabulate(of5bprev, headers='firstrow', tablefmt='fancy_grid'))
                                print("_____________________________________________________________")
                                c5bcon=input("❗ARE YOU SURE YOU WANT TO DELETE ALL THE RECORDS OF THIS TABLE? (Yes(Y)/No(N)): ").lower()
                                print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                print()
                                if c5bcon in ["yes","y","true"]:
                                    Q5="Delete from Student"
                                    cur.execute(Q5)
                                    con.commit()
                                    print("_____________________________")
                                    print("Records Successfully Deleted!")                   
                                    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                    break
                                else:
                                    print("__________________")
                                    print("Process Cancelled.")
                                    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                                    break
                    if c5=="C":
                        break
                    break
            DelRec()    
        if choice==6:
            break
exit()
