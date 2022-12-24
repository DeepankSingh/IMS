from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("UPES Infirmary")
        self.root.geometry("1540x800+0+0")
        self.root.configure(background="powder blue")

        self.Choose=StringVar()
        self.SapID=StringVar()
        self.Name=StringVar()
        self.AgeSex=StringVar()
        self.Course=StringVar()
        self.Issuedate=StringVar()
        self.Time=StringVar()
        self.ChronicAilment=StringVar()
        self.Allergies=StringVar()
        self.FurtherInformation=StringVar()


        # =============================================Dataframe==============================================
        DataFrame=Frame(self.root,bd=20,padx=20,relief=RIDGE)
        DataFrame.place(x=0,y=0,width=1530,height=400)
        
        DataFrameLeft=LabelFrame(DataFrame,bd=10,padx=20,relief=RIDGE,
                                                font=("arial",12,"bold"),text="Patient Information")
        DataFrameLeft.place(x=0,y=5,width=980,height=350)

        DataFrameRight=LabelFrame(DataFrame,bd=10,padx=20,relief=RIDGE,
                                            font=("arial",12,"bold"),text="Prescription")
        DataFrameRight.place(x=990,y=5,width=460,height=350)

        # ===========Buttonframe================================================================================
        ButtonFrame=Frame(self.root,bd=20,padx=20,pady=5,relief=RIDGE)
        ButtonFrame.place(x=0,y=393,width=1530,height=85)

        # =======Framedetails===================================================================================
        FrameDetails=Frame(self.root,bd=20,padx=20,pady=20,relief=RIDGE)
        FrameDetails.place(x=0,y=470,width=1530,height=700)

        # ===============================DataFrame Left==========================================================
      
        lblNameTablet=Label(DataFrameLeft,font=("arial",12,"bold"),text="Choose",padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNameTablet=ttk.Combobox(DataFrameLeft,textvariable=self.Choose,state="readonly",
                                                        font=("arial",12,"bold"),width=33)
        comNameTablet['value']=("Day Scholar", "Hostel Boarding","Faculty","Staff")
        comNameTablet.current(0)
        comNameTablet.grid(row=0,column=1)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="SapID:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.SapID,width=35)
        txtref.grid(row=1,column=1)

        lblName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Name:",padx=2,pady=4)
        lblName.grid(row=2,column=0,sticky=W)
        txtName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Name,width=35)
        txtName.grid(row=2,column=1)

        lblagesex=Label(DataFrameLeft,font=("arial",12,"bold"),text="Age/Sex:",padx=2,pady=6)
        lblagesex.grid(row=3,column=0,sticky=W)
        txtagesex=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.AgeSex,width=35)
        txtagesex.grid(row=3,column=1)

        lblcourse=Label(DataFrameLeft,font=("arial",12,"bold"),text="Course:",padx=2,pady=6)
        lblcourse.grid(row=4,column=0,sticky=W)
        txtcourse=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Course,width=35)
        txtcourse.grid(row=4,column=1)

        lblissueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Issuedate,width=35)
        txtissueDate.grid(row=5,column=1)

        lbltime=Label(DataFrameLeft,font=("arial",12,"bold"),text="Time:",padx=2,pady=6)
        lbltime.grid(row=6,column=0,sticky=W)
        txttime=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Time,width=35)
        txttime.grid(row=6,column=1)

        lblDailyDose=Label(DataFrameLeft,font=("arial",12,"bold"),text="Chronic Ailment:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.ChronicAilment,width=35)
        txtDailyDose.grid(row=7,column=1)

        lblallergies=Label(DataFrameLeft,font=("arial",12,"bold"),text="Allergies:",padx=2,pady=6)
        lblallergies.grid(row=8,column=0,sticky=W)
        txtallergies=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Allergies,width=35)
        txtallergies.grid(row=8,column=1)

        lblFurtherinfo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Further Information",padx=2)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.FurtherInformation,width=35)
        txtFurtherinfo.grid(row=0,column=3)

        
        # ===================================DataframeRight====================================

        self.txtPrescription=Text(DataFrameRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        # ===================================ButtonFrame=====================================
        btnPrescription=Button(ButtonFrame,text="Prescription",command=self.iPrescription,font=("arial",12,"bold"),width=23,bg="green",fg="white")
        btnPrescription.grid(row=0,column=0)

        btnReceipt=Button(ButtonFrame,text="Add Entry",command=self.iPrescriptionData,font=("arial",12,"bold"),width=23,bg="green",fg="white")
        btnReceipt.grid(row=0,column=1)

        btnExit=Button(ButtonFrame,text="Update",command=self.update_data,font=("arial",12,"bold"),width=23,bg="green",fg="white")
        btnExit.grid(row=0,column=2)

        btnDelete=Button(ButtonFrame,text="Delete",command=self.iDelete,font=("arial",12,"bold"),width=23,bg="green",fg="white")
        btnDelete.grid(row=0,column=3)

        btnReset=Button(ButtonFrame,text="Reset",command=self.iReset,font=("arial",12,"bold"),width=23,bg="green",fg="white")
        btnReset.grid(row=0,column=4)

        btnExit=Button(ButtonFrame,text="Exit",command=self.iExit,font=("arial",12,"bold"),width=23,bg="green",fg="white")
        btnExit.grid(row=0,column=5)

        # =======Scrollbar=====================================================================================
        scroll_x=ttk.Scrollbar(FrameDetails,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(FrameDetails,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(FrameDetails,column=("Choose","SapID","Name","AgeSex","Course","Issuedate","Time","ChronicAilment","Allergies","FurtherInformation"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)


        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("Choose",text="Choose")
        self.hospital_table.heading("SapID",text="SapID")
        self.hospital_table.heading("Name",text="Name")
        self.hospital_table.heading("AgeSex",text="AgeSex")
        self.hospital_table.heading("Course",text="Course")
        self.hospital_table.heading("Issuedate",text="Issue Date")
        self.hospital_table.heading("Time",text="Time")
        self.hospital_table.heading("ChronicAilment",text="Chronic Ailment")
        self.hospital_table.heading("Allergies",text="Allergies")
        self.hospital_table.heading("FurtherInformation",text="FurtherInformation")
        
        self.hospital_table["show"]="headings"
   
        self.hospital_table.column("Choose",width=100)
        self.hospital_table.column("SapID",width=100)
        self.hospital_table.column("Name",width=100)
        self.hospital_table.column("AgeSex",width=100)
        self.hospital_table.column("Course",width=100)
        self.hospital_table.column("Issuedate",width=100)
        self.hospital_table.column("Time",width=100)
        self.hospital_table.column("ChronicAilment",width=100)
        self.hospital_table.column("Allergies",width=100)
        self.hospital_table.column("FurtherInformation",width=100)
        

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch_data()

    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Choose.set(row[0])
        self.SapID.set(row[1])
        self.Name.set(row[2])
        self.AgeSex.set(row[3])
        self.Course.set(row[4])
        self.Issuedate.set(row[5])
        self.Time.set(row[6])
        self.ChronicAilment.set(row[7])
        self.Allergies.set(row[8])
        self.FurtherInformation.set(row[9])
       

  # ======================================Function Declaration=============================================

    def iPrescriptionData(self):
        if self.Choose.get()=="" or self.SapID.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='qGTGp53z@12',database='mydatabase')
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.Choose.get(),
                                                                                                        self.SapID.get(),
                                                                                                        self.Name.get(),
                                                                                                        self.AgeSex.get(),
                                                                                                        self.Course.get(),
                                                                                                        self.Issuedate.get(),
                                                                                                        self.Time.get(),
                                                                                                        self.ChronicAilment.get(),
                                                                                                        self.Allergies.get(),
                                                                                                        self.FurtherInformation.get()
                                                                                                       
                                                                                                      
                                                                                                            ))
            conn.commit()
            self.fatch_data()
            self.iReset()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted")

    def update_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='qGTGp53z@12',database='mydatabase')
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set Choose=%s,SapID=%s,Name=%s,AgeSex=%s,Course=%s,Issuedate=%s,Time=%s,ChronicAilment=%s,Allergies=%s,FurtherInformation=%s where SapID=%s",(
                                                                                
                                                                                                        self.Choose.get(),
                                                                                                        self.SapID.get(),
                                                                                                        self.Name.get(),
                                                                                                        self.AgeSex.get(),
                                                                                                        self.Course.get(),
                                                                                                        self.Issuedate.get(),
                                                                                                        self.Time.get(),
                                                                                                        self.ChronicAilment.get(),
                                                                                                        self.Allergies.get(),
                                                                                                        self.FurtherInformation.get()

                                                                                                       
                                                                                                     ))
        conn.commit()
        self.fatch_data()
        self.iReset()
        conn.close()
        messagebox.showinfo("UPDATE","Record has been updated successfully")

    def fatch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='qGTGp53z@12',database='mydatabase')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()
                                                                                           
    
    def iExit(self):
        iExit=messagebox.askyesno("Hospital Management System","Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return


#  self.Student.get(),
#                                                                                                         



    def iPrescription(self):
        self.txtPrescription.insert(END,"Choose:\t\t\t" + self.Choose.get() + "\n")
        self.txtPrescription.insert(END,"SapID:\t\t\t" +self.SapID.get()+ "\n")
        self.txtPrescription.insert(END,"Name:\t\t\t" + self.Name.get()+ "\n")
        self.txtPrescription.insert(END,"Age/Sex:\t\t\t" +   self.AgeSex.get() + "\n")
        self.txtPrescription.insert(END,"Course:\t\t\t" + self.Course.get() + "\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t" + self.Issuedate.get() + "\n")
        self.txtPrescription.insert(END,"Time:\t\t\t" +  self.Time.get()+ "\n")
        self.txtPrescription.insert(END,"Chronic Ailment:\t\t\t" +  self.ChronicAilment.get() + "\n")
        self.txtPrescription.insert(END,"Allergies:\t\t\t" +self.Allergies.get() + "\n")
        self.txtPrescription.insert(END,"Further Information:\t\t\t" + self.FurtherInformation.get() + "\n")
    

    def iDelete(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='qGTGp53z@12',database='mydatabase')
        my_cursor=conn.cursor()
        query="delete from hospital where SapID=%s"
        value=(self.SapID.get(),)
        my_cursor.execute(query,value)
                
        conn.commit()
        conn.close()
        self.fatch_data()
        self.iReset() 
        messagebox.showinfo("DELETE","Patient has been Deleted successfully")
                 
    def iReset(self):
        self.Choose.set("")
        # self.comNameTablet.current(0)
        self.SapID.set("")
        self.Name.set("")
        self.AgeSex.set("")
        self.Course.set("")
        self.Issuedate.set("")
        self.Time.set("")
        self.ChronicAilment.set("")
        self.Allergies.set("")
        self.FurtherInformation.set("")
        
        self.txtPrescription.delete("1.0",END)


if __name__ == "__main__":
    root=Tk()
    application=Hospital(root)
    root.mainloop()

