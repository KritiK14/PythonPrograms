def menu():
    print("                                                 WELCOME TO MySQL- PYTHON INTERFACE                   ")
    print("-x-"*50)
    c=input("Do you want to initiate the program? \n'YES/NO' ")
    if c=="YES":
        print ("1. Add a Record.")
        print("2. Update a Record.")
        print("3. Delete a Record.")
        print("4. Display  Records.")
        print("5. Exit.")
        choice=int(input("Enter your Choice: "))
        if choice in range(1,6):
            if choice == 1:
                adddata()
                conti()
            elif choice==2:
                updatedata()
                conti()
            elif choice==3:
                deldata()
                conti()
            elif choice==4:
                getdata()
                conti()
            elif choice==5:
                print("Exiting...")
                
            else:
                print("Wrong choice.")

    elif c=="NO":
        print("Exiting...")
        
    else:
        print("Wrong Input.")
        conti()
        

def conti():
    c=input("Do you want to continue or not? ")
    if c=="YES":
        print("\n \n \n ")
        print("-x-"*50)
        print("\n \n \n ")
        menu()
    elif c=="NO":
        print("Exiting...")
    else:
        print("Wrong input.")
            
    
def getdata():
            import mysql.connector
            try:
                db= mysql.connector.connect(user="root",host="localhost",passwd="",database="school")
                cur=db.cursor()
                cur.execute("SELECT * FROM stu_details;")
                results=cur.fetchall()
                for x in results:
                    print(x)
            except:
                print("Error: Unable to fetch data.")
           
def adddata():
            import mysql.connector
            db= mysql.connector.connect(user="root",host="localhost",passwd="",database="school")
            cur=db.cursor()
            a=int(input("Enter Admin No. : "))
            b=input("Enter Name : ")
            c=int(input("Enter Age : "))
            d=input("Enter Class : ")
            e=input("Enter City : ")
            cur.execute("INSERT INTO stu_details VALUES(%d,%s,%d,%s,%s);" %(a,b,c,d,e))
            db.commit()
            print("Record Updated.")

def updatedata():
            import mysql.connector
            try:
                 db= mysql.connector.connect(user="root",host="localhost",passwd="",database="school")
                 cur=db.cursor()
                 x=input("Enter the Admission No. of the student whose record has to be updated: ")
                 y=input("Type the value to be updtaed:")
                 sql=("UPDATE stu_details set %s where AdminNo =%s" %(y,x))
                 cur.execute(sql)
                 print("Record Updated.")
                 db.commit()
            except Exception as f:
                 print(f)

def deldata():
            import mysql.connector
            db= mysql.connector.connect(user="root",host="localhost",passwd="",database="school")
            cursor=db.cursor()
            y=input("Enter the name of the student whose record is to be deleted: ")
            cursor.execute("DELETE FROM stu_details where name=%s" %y)
            print("Record deleted.")
            db.commit()
            
menu()
            
            
            
            
              
                
    
