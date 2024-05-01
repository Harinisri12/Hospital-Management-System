from tkinter import *
from tkinter import ttk
import random
import time 
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        
        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.Expdate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()

        lbltitle = Label(self.root, bd=15, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="darkorchid4", bg="white",font=("times new roman", 30, "bold"))
        lbltitle.pack(side=TOP, fill=X)
        
        #-------------------------DATAFRAME---------------------------------
        Dataframe = Frame(self.root, bd=15, relief=RIDGE)
        Dataframe.place(x=0, y=70, width=1280, height=375)
        
        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"), text="Patient Information")
        DataframeLeft.place(x=0, y=-2, width=850, height=345)
        
        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"),text="Prescription")
        DataframeRight.place(x=860, y=-2, width=390, height=345)
        
        #-----------------------Buttons frame--------------------------------
        Buttonframe = Frame(self.root, bd=15, relief=RIDGE)
        Buttonframe.place(x=0, y=445, width=1280, height=70)

        #----------------- Details frame--------------
        Detailsframe = Frame(self.root, bd=15, relief=RIDGE)
        Detailsframe.place(x=0, y=510, width=1280, height=137)

        #-----------------DataframeLeft---------------
        lblNameTablet = Label(DataframeLeft, font=("arial", 11, "bold"), text="Names Of Tablet", padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0, sticky=W)
        
        comNametablet = ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets,state="readonly",font=("times new roman", 11, "bold"), width=30)
        comNametablet["values"] = ("Nice", "corona Vaccine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        comNametablet.grid(row=0, column=1)
        
        lblref=Label(DataframeLeft,font=("arial",11,"bold"),text="Refence No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)
        
        lblDose=Label(DataframeLeft,font=("arial",11,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)
        
        lblNoOftablets=Label(DataframeLeft,font=("arial",11,"bold"),text="No Of Tablets:",padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.NumberofTablets,width=35)
        txtNoOftablets.grid(row=3,column=1)
        
        lblLot=Label(DataframeLeft,font=("arial",11,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.Lot,width=35)
        txtLot.grid(row=4,column=1)
        
        lblissueDate=Label(DataframeLeft,font=("arial",11,"bold"),text="Issue Date:",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.Issuedate,width=35)
        txtissueDate.grid(row=5,column=1)
        
        lblExpDate=Label(DataframeLeft,font=("arial",11,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.Expdate,width=35)
        txtExpDate.grid(row=6,column=1)
        
        lblDailyDose=Label(DataframeLeft,font=("arial",11,"bold"),text="Daily Dose:",padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7,column=1)
        
        lblSideEffect=Label(DataframeLeft,font=("arial",11,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.sideEffect,width=35)
        txtSideEffect.grid(row=8,column=1)
        
        lblFurtherinfo=Label(DataframeLeft,font=("arial",11,"bold"),text="Further Information",padx=2)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFutherinfo=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.FurtherInformation,width=35)
        txtFutherinfo.grid(row=0,column=3)
        
        lblDrivingMachine=Label(DataframeLeft,font=("arial",11,"bold"),text="Blood Pressure",padx=2,pady=6)
        lblDrivingMachine.grid(row=1,column=2,sticky=W)
        txtDrivingMachine=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.DrivingUsingMachine,width=35)
        txtDrivingMachine.grid(row=1,column=3)
        
        lblStorage=Label(DataframeLeft,font=("arial",11,"bold"),text="Storage Advice:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.StorageAdvice,width=35)
        txtStorage.grid(row=2,column=3)
        
        lblMedicine=Label(DataframeLeft,font=("arial",11,"bold"),text="Medication:",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.HowToUseMedication,width=35)
        txtMedicine.grid(row=3,column=3)
        
        lblPatientId=Label(DataframeLeft,font=("arial",11,"bold"),text="Patient Id:",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.PatientId,width=35)
        txtPatientId.grid(row=4,column=3)
        
        lblNhsNumber=Label(DataframeLeft,font=("arial",11,"bold"),text="NHS Number:",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.nhsNumber,width=35)
        txtNhsNumber.grid(row=5,column=3)
        
        lblPatientName=Label(DataframeLeft,font=("arial",11,"bold"),text="Patient Name:",padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.PatientName,width=35)
        txtPatientName.grid(row=6,column=3)
        
        lblDateofBirth=Label(DataframeLeft,font=("arial",11,"bold"),text="Date Of Birth:",padx=2,pady=6)
        lblDateofBirth.grid(row=7,column=2,sticky=W)
        txtDateofBirth=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.DateOfBirth,width=35)
        txtDateofBirth.grid(row=7,column=3)
        
        lblPatientAddress=Label(DataframeLeft,font=("arial",11,"bold"),text="Patient Address:",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataframeLeft,font=("arial",11,"bold"),textvariable=self.PatientAddress,width=35)
        txtPatientAddress.grid(row=8,column=3)
        
        # --------------------------DataframeRight--------------------------------
        self.txtPrescription=Text(DataframeRight,font=("arial",12,"bold"),width=38,height=15,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)
        
        # --------------------------------Buttons----------------------------------
        btnPrescription=Button(Buttonframe,command=self.iPrectioption,text="Presciption",bg="orchid4",fg="white",font=("arial",12,"bold"),width=20,height=1,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)
        
        btnPrescriptionData=Button(Buttonframe,text="Presciption Data",bg="orchid4",fg="white",font=("arial",12,"bold"),width=20,height=1,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=1)
        btnPrescriptionData.config(command=self.iPrescriptionData) 
        
        btnUpdate=Button(Buttonframe,command=self.update,text="Update",bg="orchid4",fg="white",font=("arial",12,"bold"),width=20,height=1,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)
        
        btnDelete=Button(Buttonframe,command=self.idelete,text="Delete",bg="orchid4",fg="white",font=("arial",12,"bold"),width=19,height=1,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)
        btnClear=Button(Buttonframe,command=self.clear,text="Clear",bg="orchid4",fg="white",font=("arial",12,"bold"),width=20,height=1,padx=2,pady=6)
        btnClear.grid(row=0,column=4)
        
        btnExit=Button(Buttonframe,command=self.iExit,text="Exit",bg="orchid4",fg="white",font=("arial",12,"bold"),width=19,height=1,padx=2,pady=6)
        btnExit.grid(row=0,column=5)
        
        #--------------------------Table--------------------------
        #------------------------Scrollbar------------------------
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftablets","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
        
        self.hospital_table.heading("nameoftablets",text="Name Of Tablets")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")
        self.hospital_table["show"]="headings"        
        self.hospital_table.pack(fill=BOTH,expand=1)  
        
        self.hospital_table.column('nameoftablets',width=80)
        self.hospital_table.column('ref',width=80)
        self.hospital_table.column('dose',width=80)
        self.hospital_table.column('nooftablets',width=80)
        self.hospital_table.column('lot',width=80)
        self.hospital_table.column('issuedate',width=80)
        self.hospital_table.column('expdate',width=80)
        self.hospital_table.column('dailydose',width=80)
        self.hospital_table.column('storage',width=80)
        self.hospital_table.column('nhsnumber',width=80)
        self.hospital_table.column('pname',width=80)
        self.hospital_table.column('dob',width=80)
        self.hospital_table.column('address',width=80)
        
        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        self.fatch_data()
        
        # ---------------------- Functionality Declration ----------------------
    def iPrescriptionData(self):
        print("Prescription Data button clicked")  

        if self.Nameoftablets.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            self.insert_into_database()
    
    def insert_into_database(self):
        print("Inserting data into the database") 

        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="root123", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO hospital VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.Nameoftablets.get(),
                self.ref.get(),
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Lot.get(),
                self.Issuedate.get(),
                self.Expdate.get(),
                self.DailyDose.get(),
                self.StorageAdvice.get(),
                self.nhsNumber.get(),
                self.PatientName.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get()))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success", "Record has been inserted")
        except Exception as e:
            print("Error:", e)
            messagebox.showerror("Error", "An error occurred while inserting the data into the database.")
    def update(self):
            conn = mysql.connector.connect(host="localhost", username="root", password="root123", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE hospital SET Nameoftablets=%s, Dose=%s, NumberofTablets=%s, Lot=%s, Issuedate=%s, Expdate=%s, DailyDose=%s, StorageAdvice=%s, nhsNumber=%s, PatientName=%s, DateOfBirth=%s, PatientAddress=%s WHERE Reference_Number=%s", (
                self.Nameoftablets.get(),
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Lot.get(),
                self.Issuedate.get(),
                self.Expdate.get(),
                self.DailyDose.get(),
                self.StorageAdvice.get(),
                self.nhsNumber.get(),
                self.PatientName.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get(),
                self.ref.get(),))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success", "Record has been updated")

    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root123", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
            
    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.Expdate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])
        
    def iPrectioption(self):
        self.txtPrescription.insert(END,"Name of Tablets:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END,"Reference No:\t\t\t"+self.ref.get()+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"Number Of Tablets:\t\t\t"+self.NumberofTablets.get()+"\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t"+self.Lot.get()+"\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t"+self.Issuedate.get()+"\n")
        self.txtPrescription.insert(END,"Exp Date:\t\t\t"+self.Expdate.get()+"\n")
        self.txtPrescription.insert(END,"daliy Dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END,"Side Effect:\t\t\t"+self.sideEffect.get()+"\n")
        self.txtPrescription.insert(END,"Further Information:\t\t\t"+self.FurtherInformation.get()+"\n")
        self.txtPrescription.insert(END,"StorageAdvice:\t\t\t"+self.StorageAdvice.get()+"\n")
        self.txtPrescription.insert(END,"DrivingUsingMachine:\t\t\t"+self.DrivingUsingMachine.get()+"\n")
        self.txtPrescription.insert(END,"PatientId:\t\t\t"+self.PatientId.get()+"\n")
        self.txtPrescription.insert(END,"NHSNumber:\t\t\t"+self.nhsNumber.get()+"\n")
        self.txtPrescription.insert(END,"PatientName:\t\t\t"+self.PatientName.get()+"\n")
        self.txtPrescription.insert(END,"DateOfBirth:\t\t\t"+self.DateOfBirth.get()+"\n")
        self.txtPrescription.insert(END,"PatientAddress:\t\t\t"+self.PatientAddress.get()+"\n")

    def idelete(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root123", database="mydata")
        my_cursor = conn.cursor()
        query="Delete from hospital where Reference_Number=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)
        
        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("Delete","Patient has been deleted successfully")
        
    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.Expdate.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")        
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0",END)
        
    def iExit(self):
        iExit=messagebox.askyesno("Hospital management system","Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return
            
root = Tk()
ob = Hospital(root)
root.mainloop()
