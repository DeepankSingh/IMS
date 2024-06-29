import mysql.connector
from tkinter import *
from tkinter import ttk, messagebox
import datetime

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("UPES Infirmary")
        self.root.geometry("1540x800+0+0")
        self.root.configure(background="powder blue")

        # Variables
        self.Choose = StringVar()
        self.SapID = StringVar()
        self.Name = StringVar()
        self.AgeSex = StringVar()
        self.Course = StringVar()
        self.Issuedate = StringVar()
        self.Time = StringVar()
        self.ChronicAilment = StringVar()
        self.Allergies = StringVar()
        self.FurtherInformation = StringVar()

        self.create_widgets()
        self.fatch_data()

    def create_widgets(self):
        # Data Frame
        DataFrame = Frame(self.root, bd=20, padx=20, relief=RIDGE)
        DataFrame.place(x=0, y=0, width=1530, height=400)
        
        DataFrameLeft = LabelFrame(DataFrame, bd=10, padx=20, relief=RIDGE, font=("arial", 12, "bold"), text="Patient Information")
        DataFrameLeft.place(x=0, y=5, width=980, height=350)
        
        DataFrameRight = LabelFrame(DataFrame, bd=10, padx=20, relief=RIDGE, font=("arial", 12, "bold"), text="Prescription")
        DataFrameRight.place(x=990, y=5, width=460, height=350)

        # Button Frame
        ButtonFrame = Frame(self.root, bd=20, padx=20, pady=5, relief=RIDGE)
        ButtonFrame.place(x=0, y=393, width=1530, height=85)

        # Frame Details
        FrameDetails = Frame(self.root, bd=20, padx=20, pady=20, relief=RIDGE)
        FrameDetails.place(x=0, y=470, width=1530, height=700)

        # Widgets in DataFrameLeft
        self.create_label_entry(DataFrameLeft, "Choose", self.Choose, 0, ["Day Scholar", "Hostel Boarding", "Faculty", "Staff"])
        self.create_label_entry(DataFrameLeft, "SapID:", self.SapID, 1)
        self.create_label_entry(DataFrameLeft, "Name:", self.Name, 2)
        self.create_label_entry(DataFrameLeft, "Age/Sex:", self.AgeSex, 3)
        self.create_label_entry(DataFrameLeft, "Course:", self.Course, 4)
        self.create_label_entry(DataFrameLeft, "Issue Date:", self.Issuedate, 5)
        self.create_label_entry(DataFrameLeft, "Time:", self.Time, 6)
        self.create_label_entry(DataFrameLeft, "Chronic Ailment:", self.ChronicAilment, 7)
        self.create_label_entry(DataFrameLeft, "Allergies:", self.Allergies, 8)
        self.create_label_entry(DataFrameLeft, "Further Information", self.FurtherInformation, 9)

        # Widgets in DataFrameRight
        self.txtPrescription = Text(DataFrameRight, font=("arial", 12, "bold"), width=45, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # Buttons
        self.create_button(ButtonFrame, "Prescription", self.iPrescription, 0)
        self.create_button(ButtonFrame, "Add Entry", self.iPrescriptionData, 1)
        self.create_button(ButtonFrame, "Update", self.update_data, 2)
        self.create_button(ButtonFrame, "Delete", self.iDelete, 3)
        self.create_button(ButtonFrame, "Reset", self.iReset, 4)
        self.create_button(ButtonFrame, "Exit", self.iExit, 5)

        # Scrollbars and Table
        self.create_table(FrameDetails)

    def create_label_entry(self, frame, label_text, variable, row, values=None):
        label = Label(frame, font=("arial", 12, "bold"), text=label_text, padx=2, pady=6)
        label.grid(row=row, column=0, sticky=W)
        
        if values:
            entry = ttk.Combobox(frame, textvariable=variable, state="readonly", font=("arial", 12, "bold"), width=33)
            entry['values'] = values
            entry.current(0)
        else:
            entry = Entry(frame, font=("arial", 13, "bold"), textvariable=variable, width=35)
        
        entry.grid(row=row, column=1)

    def create_button(self, frame, text, command, column):
        button = Button(frame, text=text, command=command, font=("arial", 12, "bold"), width=23, bg="green", fg="white")
        button.grid(row=0, column=column)

    def create_table(self, frame):
        scroll_x = ttk.Scrollbar(frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(frame, orient=VERTICAL)
        
        self.hospital_table = ttk.Treeview(frame, columns=("Choose", "SapID", "Name", "AgeSex", "Course", "Issuedate", "Time", "ChronicAilment", "Allergies", "FurtherInformation"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)
        
        self.hospital_table.heading("Choose", text="Choose")
        self.hospital_table.heading("SapID", text="SapID")
        self.hospital_table.heading("Name", text="Name")
        self.hospital_table.heading("AgeSex", text="AgeSex")
        self.hospital_table.heading("Course", text="Course")
        self.hospital_table.heading("Issuedate", text="Issue Date")
        self.hospital_table.heading("Time", text="Time")
        self.hospital_table.heading("ChronicAilment", text="Chronic Ailment")
        self.hospital_table.heading("Allergies", text="Allergies")
        self.hospital_table.heading("FurtherInformation", text="Further Information")
        
        self.hospital_table["show"] = "headings"
        
        self.hospital_table.column("Choose", width=100)
        self.hospital_table.column("SapID", width=100)
        self.hospital_table.column("Name", width=100)
        self.hospital_table.column("AgeSex", width=100)
        self.hospital_table.column("Course", width=100)
        self.hospital_table.column("Issuedate", width=100)
        self.hospital_table.column("Time", width=100)
        self.hospital_table.column("ChronicAilment", width=100)
        self.hospital_table.column("Allergies", width=100)
        self.hospital_table.column("FurtherInformation", width=100)
        
        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)

    def get_cursor(self, event=""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
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

    def iPrescription(self):
        self.txtPrescription.insert(END, f"Choose: {self.Choose.get()}\n")
        self.txtPrescription.insert(END, f"SapID: {self.SapID.get()}\n")
        self.txtPrescription.insert(END, f"Name: {self.Name.get()}\n")
        self.txtPrescription.insert(END, f"Age/Sex: {self.AgeSex.get()}\n")
        self.txtPrescription.insert(END, f"Course: {self.Course.get()}\n")
        self.txtPrescription.insert(END, f"Issue Date: {self.Issuedate.get()}\n")
        self.txtPrescription.insert(END, f"Time: {self.Time.get()}\n")
        self.txtPrescription.insert(END, f"Chronic Ailment: {self.ChronicAilment.get()}\n")
        self.txtPrescription.insert(END, f"Allergies: {self.Allergies.get()}\n")
        self.txtPrescription.insert(END, f"Further Information: {self.FurtherInformation.get()}\n")

    def iPrescriptionData(self):
        if self.SapID.get() == "" or self.Name.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                con = mysql.connector.connect(host="localhost", username="root", password="password", database="mydata")
                cur = con.cursor()
                cur.execute("INSERT INTO hospital (Choose, SapID, Name, AgeSex, Course, Issuedate, Time, ChronicAilment, Allergies, FurtherInformation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                            (self.Choose.get(), self.SapID.get(), self.Name.get(), self.AgeSex.get(), self.Course.get(), self.Issuedate.get(), self.Time.get(), self.ChronicAilment.get(), self.Allergies.get(), self.FurtherInformation.get()))
                con.commit()
                self.fatch_data()
                con.close()
                messagebox.showinfo("Success", "Record has been inserted")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Something went wrong: {err}")

    def update_data(self):
        if self.SapID.get() == "" or self.Name.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                con = mysql.connector.connect(host="localhost", username="root", password="password", database="mydata")
                cur = con.cursor()
                cur.execute("UPDATE hospital SET Choose=%s, Name=%s, AgeSex=%s, Course=%s, Issuedate=%s, Time=%s, ChronicAilment=%s, Allergies=%s, FurtherInformation=%s WHERE SapID=%s", 
                            (self.Choose.get(), self.Name.get(), self.AgeSex.get(), self.Course.get(), self.Issuedate.get(), self.Time.get(), self.ChronicAilment.get(), self.Allergies.get(), self.FurtherInformation.get(), self.SapID.get()))
                con.commit()
                self.fatch_data()
                con.close()
                messagebox.showinfo("Success", "Record has been updated")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Something went wrong: {err}")

    def iDelete(self):
        if self.SapID.get() == "":
            messagebox.showerror("Error", "SapID is required")
        else:
            try:
                con = mysql.connector.connect(host="localhost", username="root", password="password", database="mydata")
                cur = con.cursor()
                cur.execute("DELETE FROM hospital WHERE SapID=%s", (self.SapID.get(),))
                con.commit()
                self.fatch_data()
                con.close()
                messagebox.showinfo("Success", "Record has been deleted")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Something went wrong: {err}")

    def iReset(self):
        self.Choose.set("Day Scholar")
        self.SapID.set("")
        self.Name.set("")
        self.AgeSex.set("")
        self.Course.set("")
        self.Issuedate.set("")
        self.Time.set("")
        self.ChronicAilment.set("")
        self.Allergies.set("")
        self.FurtherInformation.set("")
        self.txtPrescription.delete("1.0", END)

    def iExit(self):
        self.root.destroy()

    def fatch_data(self):
        try:
            con = mysql.connector.connect(host="localhost", username="root", password="password", database="mydata")
            cur = con.cursor()
            cur.execute("SELECT * FROM hospital")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.hospital_table.delete(*self.hospital_table.get_children())
                for row in rows:
                    self.hospital_table.insert("", END, values=row)
                con.commit()
            con.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Something went wrong: {err}")

if __name__ == "__main__":
    root = Tk()
    app = Hospital(root)
    root.mainloop()

