from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime

class LibraryManagementSystem():
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1350x800+0+0")

        # *********************Variable********************************************
        self.Member_Type_var=StringVar()
        self.Roll_No_var=StringVar()
        self.ID_No_var=StringVar()
        self.FirstName_var=StringVar()
        self.Surname_var=StringVar()
        self.Loc_Address_var=StringVar()
        self.Perm_Address_var=StringVar()
        self.Pin_Code_var=StringVar()
        self.Mobile_No_var=StringVar()
        self.Book_Id_var=StringVar()
        self.Book_Title_var=StringVar()
        self.Auther_Name_var=StringVar()
        self.Date_Borrowed_var=StringVar()
        self.Date_Due_var=StringVar()
        self.Days_On_Book_var=StringVar()
        self.Late_Return_Fine_var=StringVar()
        self.Date_Over_Due_var=StringVar()
        self.Actual_Price_var=StringVar()





        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",
                       bg="powder blue",
                       fg="green",
                       bd=20,
                       relief=RIDGE,
                       font=("Times New Roman",50,"bold"),
                       padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)


        frame=Frame(self.root,
                    bd=12,
                    relief=RIDGE,
                    padx=20,
                    bg="powder blue")
        frame.place(x=0,y=130,width=1350,height=380)

         # *****************DataFrameLeft *********************
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",
                       bg="powder blue",
                       fg="black",
                       bd=12,
                       relief=RIDGE,
                       font=("Times New Roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=720,height=350)

        Member_Type=Label(DataFrameLeft,
                        font=("Times New Roman",12,"bold"),
                        text="Member Type :",
                        bg="powder blue",
                        padx=2,pady=6)
        Member_Type.grid(row=0,column=0,sticky=W)

        comboMember_Type=ttk.Combobox(DataFrameLeft,
                                     font=("Times New Roman",12,"bold"),
                                     width=25,
                                     state="readonly",
                                    textvariable=self.Member_Type_var)
        comboMember_Type["value"]=("Admin Staf","Student","Lecturer")
        comboMember_Type.current(0)
        comboMember_Type.grid(row=0,column=1)


        Roll_No=Label(DataFrameLeft,text="Roll No :",
                        font=("Times New Roman",12,"bold"),
                        bg="powder blue",
                        padx=2,pady=6)
        Roll_No.grid(row=1,column=0,sticky=W)
        txtRoll_No=Entry(DataFrameLeft,
                        font=("Times New Roman",12,"bold"),
                        textvariable=self.Roll_No_var,
                        width=27)
        txtRoll_No.grid(row=1,column=1)

        ID_No=Label(DataFrameLeft,text="ID No :",
                        font=("Times New Roman",12,"bold"),
                        bg="powder blue",
                        padx=2,pady=6)
        ID_No.grid(row=2,column=0,sticky=W)
        txtID_No=Entry(DataFrameLeft,
                        font=("Times New Roman",12,"bold"),
                        textvariable=self.ID_No_var,
                        width=27)
        txtID_No.grid(row=2,column=1)

        FirstName=Label(DataFrameLeft,text="FirstName :",
                        font=("Times New Roman",12,"bold"),
                        bg="powder blue",
                        padx=2,pady=6)
        FirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,
                        font=("Times New Roman",12,"bold"),
                        textvariable=self.FirstName_var,
                        width=27)
        txtFirstName.grid(row=3,column=1)

        Surname=Label(DataFrameLeft,text="Surname :",
                        font=("Times New Roman",12,"bold"),
                        bg="powder blue",
                        padx=2,pady=6)
        Surname.grid(row=4,column=0,sticky=W)
        txtSurname=Entry(DataFrameLeft,
                        font=("Times New Roman",12,"bold"),
                        textvariable=self.Surname_var,
                        width=27)
        txtSurname.grid(row=4,column=1)

        Loc_Address=Label(DataFrameLeft,text="Loc Address :",
                        font=("Times New Roman",12,"bold"),
                        bg="powder blue",
                        padx=2,pady=6)
        Loc_Address.grid(row=5,column=0,sticky=W)
        txtLoc_Address=Entry(DataFrameLeft,
                        font=("Times New Roman",12,"bold"),
                        textvariable=self.Loc_Address_var,
                        width=27)
        txtLoc_Address.grid(row=5,column=1)

        Perm_Address=Label(DataFrameLeft,text="Perm Address :",
                        font=("Times New Roman",12,"bold"),
                        bg="powder blue",
                        padx=2,pady=6)
        Perm_Address.grid(row=6,column=0,sticky=W)
        txtPerm_Address=Entry(DataFrameLeft,
                        font=("Times New Roman",12,"bold"),
                        textvariable=self.Perm_Address_var,
                        width=27)
        txtPerm_Address.grid(row=6,column=1)

        Pin_Code=Label(DataFrameLeft,text="Pin Code :",
                        font=("Times New Roman",12,"bold"),
                        bg="powder blue",
                        padx=2,pady=6)
        Pin_Code.grid(row=7,column=0,sticky=W)
        txtPin_Code=Entry(DataFrameLeft,
                        font=("Times New Roman",12,"bold"),
                        textvariable=self.Pin_Code_var,
                        width=27)
        txtPin_Code.grid(row=7,column=1)

        Mobile_No=Label(DataFrameLeft,text="Mobile No :",
                        font=("Times New Roman",12,"bold"),
                        bg="powder blue",
                        padx=2,pady=6)
        Mobile_No.grid(row=8,column=0,sticky=W)
        txtMobile_No=Entry(DataFrameLeft,
                        font=("Times New Roman",12,"bold"),
                        textvariable=self.Mobile_No_var,
                        width=27)
        txtMobile_No.grid(row=8,column=1)

        Book_Id=Label(DataFrameLeft,text="Book Id :",
                        font=("Times New Roman",12,"bold"),
                        bg="powder blue",
                        padx=2,pady=6)
        Book_Id.grid(row=0,column=2,sticky=W)
        txtBook_Id=Entry(DataFrameLeft,
                        font=("Times New Roman",12,"bold"),
                        textvariable=self.Book_Id_var,
                        width=27)
        txtBook_Id.grid(row=0,column=3)

        Book_Title=Label(DataFrameLeft,text="Book Title :",
                        font=("Times New Roman",12,"bold"),
                        bg="powder blue",
                        padx=2,pady=6)
        Book_Title.grid(row=1,column=2,sticky=W)
        txtBook_Title=Entry(DataFrameLeft,
                        font=("Times New Roman",12,"bold"),
                        textvariable=self.Book_Title_var,
                        width=27)
        txtBook_Title.grid(row=1,column=3)

        Auther_Name=Label(DataFrameLeft,text="AutherName :",
                        font=("Times New Roman",12,"bold"),
                        bg="powder blue",
                        padx=2,pady=6)
        Auther_Name.grid(row=2,column=2,sticky=W)
        txtAuther_Name=Entry(DataFrameLeft,
                        font=("Times New Roman",12,"bold"),
                        textvariable=self.Auther_Name_var,
                        width=27)
        txtAuther_Name.grid(row=2,column=3)

        Date_Borrowed=Label(DataFrameLeft,text="Date Borrowed :",
                        font=("Times New Roman",12,"bold"),
                        bg="powder blue",
                        padx=2,pady=6)
        Date_Borrowed.grid(row=3,column=2,sticky=W)
        txtDate_Borrowed=Entry(DataFrameLeft,
                        font=("Times New Roman",12,"bold"),
                        textvariable=self.Date_Borrowed_var,
                        width=27)
        txtDate_Borrowed.grid(row=3,column=3)

        Date_Due=Label(DataFrameLeft,text="Date Due :",
                        font=("Times New Roman",12,"bold"),
                        bg="powder blue",
                        padx=2,pady=6)
        Date_Due.grid(row=4,column=2,sticky=W)
        txtDate_Due=Entry(DataFrameLeft,
                        font=("Times New Roman",12,"bold"),
                        textvariable=self.Date_Due_var,
                        width=27)
        txtDate_Due.grid(row=4,column=3)

        Days_On_Book=Label(DataFrameLeft,text="Days On Book :",
                        font=("Times New Roman",12,"bold"),
                        bg="powder blue",
                        padx=2,pady=6)
        Days_On_Book.grid(row=5,column=2,sticky=W)
        txtDays_On_Book=Entry(DataFrameLeft,
                        font=("Times New Roman",12,"bold"),
                        textvariable=self.Days_On_Book_var,
                        width=27)
        txtDays_On_Book.grid(row=5,column=3)

        Late_Return_fine=Label(DataFrameLeft,text="Late Return fine :",
                        font=("Times New Roman",12,"bold"),
                        bg="powder blue",
                        padx=2,pady=6)
        Late_Return_fine.grid(row=6,column=2,sticky=W)
        txtLate_Return_fine=Entry(DataFrameLeft,
                        font=("Times New Roman",12,"bold"),
                        textvariable=self.Late_Return_Fine_var,
                        width=27)
        txtLate_Return_fine.grid(row=6,column=3)

        Date_Over_Due=Label(DataFrameLeft,text="Date Over Due :",
                        font=("Times New Roman",12,"bold"),
                        bg="powder blue",
                        padx=2,pady=6)
        Date_Over_Due.grid(row=7,column=2,sticky=W)
        txtDate_Over_Due=Entry(DataFrameLeft,
                        font=("Times New Roman",12,"bold"),
                        textvariable=self.Date_Over_Due_var,
                        width=27)
        txtDate_Over_Due.grid(row=7,column=3)

        Actual_Price=Label(DataFrameLeft,text="Actual Price :",
                        font=("Times New Roman",12,"bold"),
                        bg="powder blue",
                        padx=2,pady=6)
        Actual_Price.grid(row=8,column=2,sticky=W)
        txtActual_Price=Entry(DataFrameLeft,
                        font=("Times New Roman",12,"bold"),
                        textvariable=self.Actual_Price_var,
                        width=27)
        txtActual_Price.grid(row=8,column=3)


         # *****************DataFrameRight*********************
        DataFrameRight=LabelFrame(frame,text="Book Details",
                       bg="powder blue",
                       fg="black",
                       bd=12,
                       relief=RIDGE,
                       font=("Times New Roman",12,"bold"))
        DataFrameRight.place(x=730,y=5,width=560,height=350)

        self.txtBox=Text(DataFrameRight,
                         font=("arial",12,"bold"),
                         width=32,height=15,
                         padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listscrollbar=Scrollbar(DataFrameRight)
        listscrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=["DBMS","Python Programming","Data Structure",
                 "Soft Skills","C Programming","DSTL",
                 "Java Programming","Machine Learning","DAA",
                 "Computer Network","Operating System","RER",
                 "Data Warehouse","MongoDB","SQL",
                 "Math I","Math II","Math IV","IOT",
                 "QUANT","PDP","Python OOP","DSA","Physics",
                 "Chemistry","English","Urdu","Social Science",
                 "Sanskrit","Arabic","Math"]


        def selectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x = value
            if (x == "DBMS"):
                self.Book_Id_var.set("BKID05454")
                self.Book_Title_var.set("Knowledge about Relation of Database")
                self.Auther_Name_var.set("Meraj Khan")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.Date_Borrowed_var.set(d1)
                self.Date_Due_var.set(d3)
                self.Days_On_Book_var.set(15)
                self.Late_Return_Fine_var.set("Rs.50")
                self.Date_Over_Due_var.set("No")
                self.Actual_Price_var.set("Rs.1200")

            elif (x == "Python Programming"):
                self.Book_Id_var.set("BKID05455")
                self.Book_Title_var.set("Python Programming Language")
                self.Auther_Name_var.set("Saba Khan")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.Date_Borrowed_var.set(d1)
                self.Date_Due_var.set(d3)
                self.Days_On_Book_var.set(15)
                self.Late_Return_Fine_var.set("Rs.50")
                self.Date_Over_Due_var.set("No")
                self.Actual_Price_var.set("Rs.1000")

            elif (x == "Data Structure"):
                self.Book_Id_var.set("BKID05456")
                self.Book_Title_var.set("Knowledge about the data")
                self.Auther_Name_var.set("Sarfaraz Khan")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.Date_Borrowed_var.set(d1)
                self.Date_Due_var.set(d3)
                self.Days_On_Book_var.set(15)
                self.Late_Return_Fine_var.set("Rs.50")
                self.Date_Over_Due_var.set("No")
                self.Actual_Price_var.set("Rs.1300")
            
            elif (x == "Soft Skills"):
                self.Book_Id_var.set("BKID05457")
                self.Book_Title_var.set("Knowledge about the Grammar")
                self.Auther_Name_var.set("Asif Khan")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.Date_Borrowed_var.set(d1)
                self.Date_Due_var.set(d3)
                self.Days_On_Book_var.set(15)
                self.Late_Return_Fine_var.set("Rs.50")
                self.Date_Over_Due_var.set("No")
                self.Actual_Price_var.set("Rs.400")
                

        listBox=Listbox(DataFrameRight,
                        font=("arial",12,"bold"),
                         width=20,height=15)
        listBox.bind("<<ListboxSelect>>",selectBook)
        listBox.grid(row=0,column=0,padx=4)
        listscrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)



        # *****************Button Frame********************************************
        Framebutton=Frame(self.root,
                    bd=12,
                    relief=RIDGE,
                    padx=20,
                    bg="powder blue")
        Framebutton.place(x=0,y=510,width=1350,height=60)

        btnAddData=Button(Framebutton,
                          command=self.add_data,
                          text="Add Data",
                          font=("arial",12,"bold"),
                          width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,
                          command=self.showData,
                          text="Show Data",
                          font=("arial",12,"bold"),
                          width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,
                          command=self.update,
                          text="Update",
                          font=("arial",12,"bold"),
                          width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,
                          command=self.delete,
                          text="Delete",
                          font=("arial",12,"bold"),
                          width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text="Reset",
                          font=("arial",12,"bold"),
                          width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,
                          command=self.iExit,
                          text="Exit",
                          font=("arial",12,"bold"),
                          width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)





        # *****************Database Information Frame**********
        FrameDetails=Frame(self.root,
                    bd=12,
                    relief=RIDGE,
                    padx=20,
                    bg="powder blue")
        FrameDetails.place(x=0,y=570,width=1350,height=110)

        table_frame=Frame(FrameDetails,
                    bd=6,
                    relief=RIDGE,
                    bg="powder blue")
        table_frame.place(x=0,y=1,width=1300,height=85)
        xscroll=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.library_table=ttk.Treeview(table_frame,columns=("Member_Type",
                                                             "Roll_No","ID_No",
                                                             "FirstName","Surname",
                                                             "Loc_Address",
                                                             "Perm_Address",
                                                             "Pin_Code","Mobile_No",
                                                             "Book_Id","Book_Title",
                                                             "Auther_Name",
                                                             "Date_Borrowed",
                                                             "Date_Due",
                                                             "Days_On_Book",
                                                             "Late_Return_Fine",
                                                             "Date_Over_Due",
                                                             "Actual_Price"),
                                                             xscrollcommand=xscroll.set,
                                                             yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("Member_Type",text="Member Type")
        self.library_table.heading("Roll_No",text="Roll No")
        self.library_table.heading("ID_No",text="ID No")
        self.library_table.heading("FirstName",text="FirstName")
        self.library_table.heading("Surname",text="Surname")
        self.library_table.heading("Loc_Address",text="LocAddress")
        self.library_table.heading("Perm_Address",text="PermAddress")
        self.library_table.heading("Pin_Code",text="PinCode")
        self.library_table.heading("Mobile_No",text="MobileNo")
        self.library_table.heading("Book_Id",text="BookId")
        self.library_table.heading("Book_Title",text="BookTitle")
        self.library_table.heading("Auther_Name",text="AutherName")
        self.library_table.heading("Date_Borrowed",text="DateBorrowed")
        self.library_table.heading("Date_Due",text="DateDue")
        self.library_table.heading("Days_On_Book",text="DaysOnBook")
        self.library_table.heading("Late_Return_Fine",text="LateReturnFine")
        self.library_table.heading("Date_Over_Due",text="DateOverDue")
        self.library_table.heading("Actual_Price",text="ActualPrice")


        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)


        self.library_table.column("Member_Type",width=100)
        self.library_table.column("Roll_No",width=100)
        self.library_table.column("ID_No",width=100)
        self.library_table.column("FirstName",width=100)
        self.library_table.column("Surname",width=100)
        self.library_table.column("Loc_Address",width=100)
        self.library_table.column("Perm_Address",width=100)
        self.library_table.column("Pin_Code",width=100)
        self.library_table.column("Mobile_No",width=100)
        self.library_table.column("Book_Id",width=100)
        self.library_table.column("Book_Title",width=100)
        self.library_table.column("Auther_Name",width=100)
        self.library_table.column("Date_Borrowed",width=100) 
        self.library_table.column("Date_Due",width=100)
        self.library_table.column("Days_On_Book",width=100)
        self.library_table.column("Late_Return_Fine",width=100)
        self.library_table.column("Date_Over_Due",width=100)
        self.library_table.column("Actual_Price",width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)


    def add_data(self):
        # creating the mysql object
        conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Meraj7070@",
                    database="mydata"
                )
        # Creating a cursor object
        my_cursor = conn.cursor()

        # Executing a query
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                          (self.Member_Type_var.get(),
                           self.Roll_No_var.get(),
                           self.ID_No_var.get(),
                           self.FirstName_var.get(),
                           self.Surname_var.get(),
                           self.Loc_Address_var.get(),
                           self.Perm_Address_var.get(),
                           self.Pin_Code_var.get(),
                           self.Mobile_No_var.get(),
                           self.Book_Id_var.get(),
                           self.Book_Title_var.get(),
                           self.Auther_Name_var.get(),
                           self.Date_Borrowed_var.get(),
                           self.Date_Due_var.get(),
                           self.Days_On_Book_var.get(),
                           self.Late_Return_Fine_var.get(),
                           self.Date_Over_Due_var.get(),
                           self.Actual_Price_var.get()))


        # Closing the connection
        # my_cursor.close()
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success","Member has benn inserted successfully")

    def update(self):
        conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Meraj7070@",
                    database="mydata"
                )
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member_Type=%s,ID_No=%s,FirstName=%s,Surname=%s,Loc_Address=%s,Perm_Address=%s,Pin_Code=%s,Mobile_No=%s,Book_Id=%s,Book_Title=%s,Auther_Name=%s,Date_Borrowed=%s,Date_Due=%s,Days_On_Book=%s,Late_Return_Fine=%s,Date_Over_Due=%s,Actual_Price=%s where Roll_No=%s",(
                          self.Member_Type_var.get(),
                          self.ID_No_var.get(),
                          self.FirstName_var.get(),
                          self.Surname_var.get(),
                          self.Loc_Address_var.get(),
                          self.Perm_Address_var.get(),
                          self.Pin_Code_var.get(),
                          self.Mobile_No_var.get(),
                          self.Book_Id_var.get(),
                          self.Book_Title_var.get(),
                          self.Auther_Name_var.get(),
                          self.Date_Borrowed_var.get(),
                          self.Date_Due_var.get(),
                          self.Days_On_Book_var.get(),
                          self.Late_Return_Fine_var.get(),
                          self.Date_Over_Due_var.get(),
                          self.Actual_Price_var.get(),
                          self.Roll_No_var.get(),
                          ))

        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        
        messagebox.showinfo("Success","Member has benn Updated")




    def fetch_data(self):
        conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Meraj7070@",
                    database="mydata"
                )
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows = my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
                conn.commit()
            conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content["values"]

        self.Member_Type_var.set(row[0]),
        self.Roll_No_var.set(row[1]),
        self.ID_No_var.set(row[2]),
        self.FirstName_var.set(row[3]),
        self.Surname_var.set(row[4]),
        self.Loc_Address_var.set(row[5]),
        self.Perm_Address_var.set(row[6]),
        self.Pin_Code_var.set(row[7]),
        self.Mobile_No_var.set(row[8]),
        self.Book_Id_var.set(row[9]),
        self.Book_Title_var.set(row[10]),
        self.Auther_Name_var.set(row[11]),
        self.Date_Borrowed_var.set(row[12]),
        self.Date_Due_var.set(row[13]),
        self.Days_On_Book_var.set(row[14]),
        self.Late_Return_Fine_var.set(row[15]),
        self.Date_Over_Due_var.set(row[16]),
        self.Actual_Price_var.set(row[17])

    def showData(self):
        self.txtBox.insert(END,"Member Type :\t\t"+self.Member_Type_var.get()+"\n")
        self.txtBox.insert(END,"Roll No :\t\t"+self.Roll_No_var.get()+"\n")
        self.txtBox.insert(END,"ID No :\t\t"+self.ID_No_var.get()+"\n")
        self.txtBox.insert(END,"FirstName :\t\t"+self.FirstName_var.get()+"\n")
        self.txtBox.insert(END,"Surname :\t\t"+self.Surname_var.get()+"\n")
        self.txtBox.insert(END,"Loc Address :\t\t"+self.Loc_Address_var.get()+"\n")
        self.txtBox.insert(END,"perm Address :\t\t"+self.Perm_Address_var.get()+"\n")
        self.txtBox.insert(END,"Pin Code :\t\t"+self.Pin_Code_var.get()+"\n")
        self.txtBox.insert(END,"Mobile No :\t\t"+self.Mobile_No_var.get()+"\n")
        self.txtBox.insert(END,"Book Id :\t\t"+self.Book_Id_var.get()+"\n")
        self.txtBox.insert(END,"Book Title :\t\t"+self.Book_Title_var.get()+"\n")
        self.txtBox.insert(END,"Auther Name :\t\t"+self.Auther_Name_var.get()+"\n")
        self.txtBox.insert(END,"Date Borrowed :\t\t"+self.Date_Borrowed_var.get()+"\n")
        self.txtBox.insert(END,"Date Due :\t\t"+self.Date_Due_var.get()+"\n")
        self.txtBox.insert(END,"Days On Book :\t\t"+self.Days_On_Book_var.get()+"\n")
        self.txtBox.insert(END,"Late Return Fine :\t\t"+self.Late_Return_Fine_var.get()+"\n")
        self.txtBox.insert(END,"Date Over Due :\t\t"+self.Date_Over_Due_var.get()+"\n")
        self.txtBox.insert(END,"Actual Price :\t\t"+self.Actual_Price_var.get()+"\n")


    def reset(self):
        self.Member_Type_var.set(""),
        self.Roll_No_var.set(""),
        self.ID_No_var.set(""),
        self.FirstName_var.set(""),
        self.Surname_var.set(""),
        self.Loc_Address_var.set(""),
        self.Perm_Address_var.set(""),
        self.Pin_Code_var.set(""),
        self.Mobile_No_var.set(""),
        self.Book_Id_var.set(""),
        self.Book_Title_var.set(""),
        self.Auther_Name_var.set(""),
        self.Date_Borrowed_var.set(""),
        self.Date_Due_var.set(""),
        self.Days_On_Book_var.set(""),
        self.Late_Return_Fine_var.set(""),
        self.Date_Over_Due_var.set(""),
        self.Actual_Price_var.set(""),
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Libraray Management System","Do want to exit")
        if iExit>0:
            self.root.destroy()
            return 
    

    def delete(self):
        if self.Roll_No_var.get()=="" or self.ID_No_var.get()=="":
            messagebox.showerror("Error","First select the member")
        else:
            # creating the mysql object
            conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="Meraj7070@",
                        database="mydata"
                    )
            # Creating a cursor object
            my_cursor = conn.cursor()

            query="delete from library where Roll_No=%s"
            value=(self.Roll_No_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been deleted")

if __name__ =="__main__":
    root= Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
