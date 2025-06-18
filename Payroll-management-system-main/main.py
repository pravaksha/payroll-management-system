import random
import time

import sv_ttk
import tkinter as tkr
import tkinter.ttk as tkrtk
from tkinter import ttk
import tkinter.messagebox
import datetime
from tkinter import *
import psycopg2


class PayrollManagementSystem:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Payroll Management System")
        self.root.geometry("1380x750+0+0")
        self.root.resizable(0,0)



############################################### Variables ##############################################
        EmployeeName = StringVar()
        Address =StringVar()
        Reference = StringVar()
        EmployerName = StringVar()
        CityWeighting = StringVar()
        BasicSalary = StringVar()
        OverTime = StringVar()
        OtherPaymentDue = StringVar()
        GrossPay = StringVar()
        Tax = StringVar()
        Pension = StringVar()
        StudentLoan = StringVar()
        NIPayment = StringVar()
        Deductions = StringVar()
        PostCode = StringVar()
        Gender = StringVar()
        Payday = StringVar()
        TaxPeriod = StringVar()
        TaxCode = StringVar()
        NINumber = StringVar()
        NICode = StringVar()
        TaxablePay = StringVar()
        PensionablePay = StringVar()
        NetPay = StringVar()

        text_Input = StringVar()
        global operator
        operator = ""

        CityWeighting.set("")
        BasicSalary.set("")


############################################## Functionalities of the Payroll Management System###############################################################################################

####################################### calculator Functions ##########################################

        def btnClick(numbers):
            global operator
            operator = operator + str(numbers)
            text_Input.set(operator)

        def clear():
            global operator
            operator = ""
            text_Input.set("0")

        def equal():
            global operator
            if operator != "0" or operator != "":
                operator = str(eval(operator))
                text_Input.set(operator)
            else:
                operator = "0"
                text_Input.set(operator)
#################################### Action Buttons ###########################################

        def iExit():
            iExit = tkinter.messagebox.askyesno("Payroll Management System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        def Reset():
            EmployeeName.set("")
            Address.set("")
            Reference.set("")
            EmployerName.set("")
            CityWeighting.set("")
            BasicSalary.set("")
            OverTime.set("")
            OtherPaymentDue.set("")
            GrossPay.set("")
            Tax.set("")
            Pension.set("")
            StudentLoan.set("")
            NIPayment.set("")
            Deductions.set("")
            PostCode.set("")
            Gender.set("")
            Payday.set("")
            TaxPeriod.set("")
            TaxCode.set("")
            NINumber.set("")
            NICode.set("")
            TaxablePay.set("")
            PensionablePay.set("")
            NetPay.set("")

#################################### Pay Functions ###############################################

        def PayRef():
            Payday.set(time.strftime("%Y-%m-%d"))
            Refpay = random.randint(15000, 909878)
            Refpaid = ("PR" + str(Refpay))
            Reference.set(Refpaid)

            NIpay = random.randint(15000, 909878)
            NInumber = ("NI" + str(NIpay))
            NINumber.set(NInumber)

            iTaxCode = random.randint(15000, 909878)
            iTaxCoded = ("TCode" + str(iTaxCode))
            TaxCode.set(iTaxCoded)

            NICodepay = random.randint(15000, 909878)
            NICoded = ("NIC" + str(NICodepay))
            NICode.set(NICoded)

            iDate = datetime.datetime.now()
            TaxPeriodpay = iDate.month
            TaxPeriod.set(str(TaxPeriodpay))

        def Payment():
            PayRef()
            BS = float(BasicSalary.get())
            OT = float(OverTime.get())
            CW = float(CityWeighting.get())

            MTax = ((BS + OT + CW)*0.3)
            TTax = str('$%.2f' % (MTax))
            Tax.set(TTax)

            MPension = ((BS + OT + CW)*0.1)
            TPension = str('$%.2f' % (MPension))
            Pension.set(TPension)

            MSLoan = ((BS + OT + CW)*0.05)
            TLoan = str('$%.2f' % (MSLoan))
            StudentLoan.set(TLoan)

            MNIPayment = ((BS + OT + CW)*0.05)
            TNIPayment = str('$%.2f' % (MNIPayment))
            NIPayment.set(TNIPayment)


            MDeductions = (MTax + MPension + MSLoan + MNIPayment)
            TDeductions = str('$%.2f' % (MDeductions))
            Deductions.set(TDeductions)

            MNetPay = (BS + OT + CW) - (MDeductions)
            TNetPay = str('$%.2f' % (MNetPay))
            NetPay.set(TNetPay)

            MGrossPay = (BS + OT + CW)
            TGrossPay = str('$%.2f' % (MGrossPay))
            GrossPay.set(TGrossPay)


            TaxablePay.set(TTax)
            PensionablePay.set(TPension)
            OtherPaymentDue.set("$0.00")


################################# data base  connection ###################################################################

################################# data add   ###################################################################

        def AddData():
            if EmployeeName.get() == "" or Address.get() == "" or EmployerName.get() == "" or CityWeighting.get() == "" or BasicSalary.get() == "":
                tkinter.messagebox.showinfo("Payroll Management System", "Please complete the required field")
            else:
                conn = psycopg2.connect(database="payroll", user="postgres", password="2727", host="localhost", port="5432")
                cur = conn.cursor()
                cur.execute("insert into payment values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    Reference.get(),
                    EmployeeName.get(),
                    Address.get(),
                    EmployerName.get(),
                    CityWeighting.get(),
                    BasicSalary.get(),
                    OverTime.get(),
                    GrossPay.get(),
                    Tax.get(),
                    Pension.get(),
                    NIPayment.get(),
                    Deductions.get(),
                    PostCode.get(),
                    Gender.get(),
                    Payday.get(),
                    TaxPeriod.get(),
                    TaxCode.get(),
                    NINumber.get(),
                    NetPay.get(),
                ))
                conn.commit()
                DisplayData()
                conn.close()
                tkinter.messagebox.showinfo("Payroll Management System", "Record has been successfully saved")

################################# display data  ###################################################################

        def DisplayData():
            conn = psycopg2.connect(database="payroll", user="postgres", password="2727", host="localhost", port="5432")
            cur = conn.cursor()
            cur.execute("select * from payment")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.PMS_Table.delete(*self.PMS_Table.get_children())
                for i in rows:
                    self.PMS_Table.insert("", END, values=i)
                conn.commit()
            conn.close()

        def WagesInfo(ev):
            viewinfo = self.PMS_Table.focus()
            info = self.PMS_Table.item(viewinfo)
            row = info["values"]
            Reference.set(row[0])
            EmployeeName.set(row[1])
            Address.set(row[2])
            EmployerName.set(row[3])
            CityWeighting.set(row[4])
            BasicSalary.set(row[5])
            OverTime.set(row[6])
            GrossPay.set(row[7])
            Tax.set(row[8])
            Pension.set(row[9])
            NIPayment.set(row[10])
            Deductions.set(row[11])
            PostCode.set(row[12])
            Gender.set(row[13])
            Payday.set(row[14])
            TaxPeriod.set(row[15])
            TaxCode.set(row[16])
            NINumber.set(row[17])
            NetPay.set(row[18])

################################# data delete   ###################################################################

################################# data update   ###################################################################
        def UpdateData():
            conn = psycopg2.connect(database="payroll", user="postgres", password="2727", host="localhost", port="5432")
            cur = conn.cursor()
            cur.execute(
                "update payment set fullname=%s,address=%s,employername=%s,cityweighting=%s,basicsalary=%s,overtime=%s,grosspay=%s,tax=%s,pension=%s,nipayment=%s,deductions=%s,postcode=%s,gender=%s, payday=%s, taxperiod=%s, ninumber=%s, netpay=%s where ref=%s",(
                    EmployeeName.get(),
                    Address.get(),
                    EmployerName.get(),
                    CityWeighting.get(),
                    BasicSalary.get(),
                    OverTime.get(),
                    GrossPay.get(),
                    Tax.get(),
                    Pension.get(),
                    NIPayment.get(),
                    Deductions.get(),
                    PostCode.get(),
                    Gender.get(),
                    Payday.get(),
                    TaxPeriod.get(),
                    NINumber.get(),
                    NetPay.get(),
                    Reference.get()
                ))
            conn.commit()
            DisplayData()
            conn.close()
            tkinter.messagebox.showinfo("Payroll Management System", "Record has been successfully updated")

################################# data delete   ###################################################################

        def DeleteData():
            conn = psycopg2.connect(database="payroll", user="postgres", password="2727", host="localhost", port="5432")
            cur = conn.cursor()
            cur.execute("delete from payment where ref=%s", (Reference.get(),))
            conn.commit()
            DisplayData()
            conn.close()
            tkinter.messagebox.showinfo("Payroll Management System", "Record has been successfully deleted")

########################################### Frame Structure ###########################################

########################################### Tab Controls ###########################################

        notebook = ttk.Notebook(self.root)
        self.TabControl1 = ttk.Frame(notebook)
        self.TabControl2 = ttk.Frame(notebook)
        self.TabControl3 = ttk.Frame(notebook)
        notebook.add(self.TabControl1, text="Payroll System")
        notebook.add(self.TabControl2, text="View Payroll")
        notebook.add(self.TabControl3, text="Notes")
        notebook.grid()

########################################### First Tab payroll management ui ###########################################

        Tab1Frame = Frame(self.TabControl1, bd=10,width=1350, height=700, relief=RIDGE)
        Tab1Frame.grid()
        Tab2Frame = Frame(self.TabControl2, bd=10,width=1350, height=700, relief=RIDGE)
        Tab2Frame.grid()
        Tab3Frame = Frame(self.TabControl3, bd=10,width=1350, height=700, relief=RIDGE)
        Tab3Frame.grid()

########################################TopFrame########################################

        TopFrame1 = Frame(Tab1Frame, bd=10,width=1340, height=100, relief=RIDGE)
        TopFrame1.grid(row=0, column=0)
        TopFrame2 = Frame(Tab1Frame, bd=10,width=1340, height=100, relief=RIDGE)
        TopFrame2.grid(row=1, column=0)
        TopFrame3 = Frame(Tab1Frame, bd=10,width=1340, height=100, relief=RIDGE)
        TopFrame3.grid(row=2, column=0)

########################################LeftFrame########################################

        LeftFrame = Frame(TopFrame3,bd=5,width=1340,height=400,padx=2,bg="cadetblue4",relief=RIDGE)
        LeftFrame.pack(side=RIGHT)
        LeftFrame1 = Frame(LeftFrame,bd=5,width=600,height=180,padx=2,relief=RIDGE)
        LeftFrame1.pack(side=TOP)

        LeftFrame2 =Frame(LeftFrame,bd=5,width=600,height=180,padx=2,bg="cadetblue4",relief=RIDGE)
        LeftFrame2.pack(side=TOP)
        LeftFrame2Left = Frame(LeftFrame2,bd=5,width=300,height=170,padx=2,relief=RIDGE)
        LeftFrame2Left.pack(side=LEFT)
        LeftFrame2Right = Frame(LeftFrame2,bd=5,width=300,height=170,padx=2,relief=RIDGE)
        LeftFrame2Right.pack(side=RIGHT)

        LeftFrame3Left = Frame(LeftFrame,bd=5,width=320,height=50,padx=2,bg="cadetblue4",relief=RIDGE)
        LeftFrame3Left.pack(side=LEFT)
        LeftFrame3Right = Frame(LeftFrame,bd=5,width=320,height=50,padx=2,bg="cadetblue4",relief=RIDGE)
        LeftFrame3Right.pack(side=RIGHT)

########################################RightFrame########################################
        RightFrame1 = Frame(TopFrame3,bd=5,width=320,height=400,padx=2,bg="cadetblue4",relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1,bd=5,width=310,height=300,padx=2,relief=RIDGE)
        RightFrame1a.pack(side=TOP)
        RightFrame1b = Frame(RightFrame1,bd=5,width=310,height=100,padx=2,relief=RIDGE)
        RightFrame1b.pack(side=TOP)

        RightFrame2 = Frame(TopFrame3,bd=5,width=300,height=400,padx=2,bg="cadetblue4",relief=RIDGE)
        RightFrame2.pack(side=LEFT)
        RightFrame2a = Frame(RightFrame2,bd=5,width=280,height=50,padx=2,relief=RIDGE)
        RightFrame2a.pack(side=TOP)
        RightFrame2b = Frame(RightFrame2,bd=5,width=280,height=180,padx=2,relief=RIDGE)
        RightFrame2b.pack(side=TOP)
        RightFrame2c = Frame(RightFrame2,bd=5,width=280,height=100,padx=2,relief=RIDGE)
        RightFrame2c.pack(side=TOP)
        RightFrame2d = Frame(RightFrame2,bd=5,width=280,height=50,padx=2,bg="cadetblue4",relief=RIDGE)
        RightFrame2d.pack(side=TOP)

########################################Labels########################################

        self.lblTitle = Label(TopFrame1,text="\tPayroll Management System\t",font=("Arial",40,"bold"),justify=CENTER)
        self.lblTitle.grid(padx=300)

        self.lblEmployeeName = Label(TopFrame2,text="Employee Name",font=("Arial",12,"bold"),justify=CENTER)
        self.lblEmployeeName.grid(row=0,column=0,sticky=W)
        self.txtEmployeeName = Entry(TopFrame2,textvariable=EmployeeName,font=("Arial",12,"bold"),bd=5,width=82,justify=LEFT)
        self.txtEmployeeName.grid(row=0,column=1,sticky=W)

        self.lblAddress = Label(TopFrame2,text="Address",font=("Arial",12,"bold"),justify=CENTER)
        self.lblAddress.grid(row=1,column=0,sticky=W)
        self.txtAddress = Entry(TopFrame2,textvariable=Address,font=("Arial",12,"bold"),bd=5,width=82,justify=LEFT)
        self.txtAddress.grid(row=1,column=1,sticky=W)

        self.lblPostCode = Label(TopFrame2,text="Post Code",font=("Arial",12,"bold"),justify=CENTER)
        self.lblPostCode.grid(row=0,column=2,sticky=W)
        self.txtPostCode = Entry(TopFrame2,textvariable=PostCode,font=("Arial",12,"bold"),bd=5,width=82,justify=LEFT)
        self.txtPostCode.grid(row=0,column=3,sticky=W)

        self.lblGender = Label(TopFrame2,text="Gender",font=("Arial",12,"bold"),justify=CENTER)
        self.lblGender.grid(row=1,column=2,sticky=W)
        self.cboGender = ttk.Combobox(TopFrame2,textvariable=Gender,font=("Arial",14,"bold"),width=19,state="readonly")
        self.cboGender["values"] = ("","Male","Female")
        self.cboGender.current(0)
        self.cboGender.grid(row=1,column=3,sticky=W)

##############################################################################
        self.lblPayday = Label(RightFrame2a,text="Payday",font=("Arial",12,"bold"),bd=10,justify=CENTER)
        self.lblPayday.grid(row=0,column=0,sticky=W)
        self.txtPayday = Entry(RightFrame2a,textvariable=Payday,font=("Arial",12,"bold"),bd=5,width=27,state=DISABLED,justify=LEFT)
        self.txtPayday.grid(row=0,column=1,sticky=W)

        self.lblTaxPeriod = Label(RightFrame2b,text="Tax Period",font=("Arial",12,"bold"),bd=10,justify=CENTER)
        self.lblTaxPeriod.grid(row=1,column=0,sticky=W)
        self.txtTaxPeriod = Entry(RightFrame2b,textvariable=TaxPeriod,font=("Arial",12,"bold"),bd=5,width=24,state=DISABLED,justify=LEFT)
        self.txtTaxPeriod.grid(row=1,column=1,sticky=W)

        self.lblTaxCode = Label(RightFrame2b,text="Tax Code",font=("Arial",12,"bold"),bd=10,justify=CENTER)
        self.lblTaxCode.grid(row=2,column=0,sticky=W)
        self.txtTaxCode = Entry(RightFrame2b,textvariable=TaxCode,font=("Arial",12,"bold"),bd=5,width=24,state=DISABLED,justify=LEFT)
        self.txtTaxCode.grid(row=2,column=1,sticky=W)

        self.lblNINumber = Label(RightFrame2b,text="NI Number",font=("Arial",12,"bold"),bd=10,justify=CENTER)
        self.lblNINumber.grid(row=3,column=0,sticky=W)
        self.txtNINumber = Entry(RightFrame2b,textvariable=NINumber,font=("Arial",12,"bold"),bd=5,width=24,state=DISABLED,justify=LEFT)
        self.txtNINumber.grid(row=3,column=1,sticky=W)

        self.lblNICode = Label(RightFrame2b,text="NI Code",font=("Arial",12,"bold"),bd=10,justify=CENTER)
        self.lblNICode.grid(row=4,column=0,sticky=W)
        self.txtNICode = Entry(RightFrame2b,textvariable=NICode,font=("Arial",12,"bold"),bd=5,width=24,state=DISABLED,justify=LEFT)
        self.txtNICode.grid(row=4,column=1,sticky=W)


        self.lblTaxablePay = Label(RightFrame2c,text="Taxable Pay",font=("Arial",12,"bold"),bd=10,justify=CENTER)
        self.lblTaxablePay.grid(row=3,column=0,sticky=W)
        self.txtTaxablePay = Entry(RightFrame2c,textvariable=TaxablePay,font=("Arial",12,"bold"),bd=5,width=19,state=DISABLED,justify=LEFT)
        self.txtTaxablePay.grid(row=3,column=1,sticky=W)

        self.lblPensionablePay = Label(RightFrame2c,text="Pensionable Pay",font=("Arial",12,"bold"),bd=10,justify=CENTER)
        self.lblPensionablePay.grid(row=4,column=0,sticky=W)
        self.txtPensionablePay = Entry(RightFrame2c,textvariable=PensionablePay,font=("Arial",12,"bold"),bd=5,width=19,state=DISABLED,justify=LEFT)
        self.txtPensionablePay.grid(row=4,column=1,sticky=W)

        self.lblNetPay = Label(RightFrame2d,text="Net Pay",font=("Arial",12,"bold"),bd=10,justify=CENTER)
        self.lblNetPay.grid(row=4,column=0,sticky=W)
        self.txtNetPay = Entry(RightFrame2d,textvariable=NetPay,font=("Arial",12,"bold"),bd=5,width=27,state=DISABLED,justify=LEFT)
        self.txtNetPay.grid(row=4,column=1,sticky=W)

#########################################################################################################################################

        self.lblReference = Label(LeftFrame1,text="Reference",font=("Arial",12,"bold"),bd=10,padx=20,justify=CENTER)
        self.lblReference.grid(row=0,column=0,sticky=W)
        self.txtReference = Entry(LeftFrame1,textvariable=Reference,font=("Arial",12,"bold"),bd=5,width=62,state=DISABLED,justify=LEFT)
        self.txtReference.grid(row=0,column=1,sticky=W)

        self.lblEmployerName = Label(LeftFrame1,text="Employer Name",font=("Arial",12,"bold"),bd=10,padx=20,justify=CENTER)
        self.lblEmployerName.grid(row=1,column=0,sticky=W)
        self.txtEmployerName = Entry(LeftFrame1,textvariable=EmployerName,font=("Arial",12,"bold"),bd=5,width=62,justify=LEFT)
        self.txtEmployerName.grid(row=1,column=1,sticky=W)

        self.lblEmployeeName = Label(LeftFrame1,text="Employee Name",font=("Arial",12,"bold"),bd=10,padx=20,justify=CENTER)
        self.lblEmployeeName.grid(row=2,column=0,sticky=W)
        self.txtEmployeeName = Entry(LeftFrame1,textvariable=EmployeeName,font=("Arial",12,"bold"),bd=5,width=62,state=DISABLED,justify=LEFT)
        self.txtEmployeeName.grid(row=2,column=1,sticky=W)


        self.lblCityWeighting = Label(LeftFrame2Left,text="City Weighting",font=("Arial",12,"bold"),bd=10,justify=CENTER)
        self.lblCityWeighting.grid(row=0,column=0,sticky=W)
        self.txtCityWeighting = Entry(LeftFrame2Left,textvariable=CityWeighting,font=("Arial",12,"bold"),bd=5,width=20,justify=LEFT)
        self.txtCityWeighting.grid(row=0,column=1,sticky=W)


        self.lblBasicSalary = Label(LeftFrame2Left,text="Basic Salary",font=("Arial",12,"bold"),bd=10,justify=CENTER)
        self.lblBasicSalary.grid(row=1,column=0,sticky=W)
        self.txtBasicSalary = Entry(LeftFrame2Left,textvariable=BasicSalary,font=("Arial",12,"bold"),bd=5,width=20,justify=LEFT)
        self.txtBasicSalary.grid(row=1,column=1,sticky=W)

        self.lblOverTime = Label(LeftFrame2Left,text="Over Time",font=("Arial",12,"bold"),bd=10,justify=CENTER)
        self.lblOverTime.grid(row=2,column=0,sticky=W)
        self.txtOverTime = Entry(LeftFrame2Left,textvariable=OverTime,font=("Arial",12,"bold"),bd=5,width=20,justify=LEFT)
        self.txtOverTime.grid(row=2,column=1,sticky=W)

        self.lblOtherPaymentDue = Label(LeftFrame2Left,text="Other Payment Due",font=("Arial",12,"bold"),bd=10,justify=CENTER)
        self.lblOtherPaymentDue.grid(row=3,column=0,sticky=W)
        self.txtOtherPaymentDue = Entry(LeftFrame2Left,textvariable=OtherPaymentDue,font=("Arial",12,"bold"),bd=5,width=20,justify=LEFT)
        self.txtOtherPaymentDue.grid(row=3,column=1,sticky=W)
###############################################################################################################################################################
        self.lblTax = Label(LeftFrame2Right,text="Tax",font=("Arial",12,"bold"),bd=10,justify=CENTER)
        self.lblTax.grid(row=0,column=0,sticky=W)
        self.txtTax = Entry(LeftFrame2Right,textvariable=Tax,font=("Arial",12,"bold"),bd=5,width=20,state=DISABLED,justify=LEFT)
        self.txtTax.grid(row=0,column=1,sticky=W)

        self.lblPension = Label(LeftFrame2Right,text="Pension",font=("Arial",12,"bold"),bd=10,justify=CENTER)
        self.lblPension.grid(row=1,column=0,sticky=W)
        self.txtPension = Entry(LeftFrame2Right,textvariable=Pension,font=("Arial",12,"bold"),bd=5,width=20,state=DISABLED,justify=LEFT)
        self.txtPension.grid(row=1,column=1,sticky=W)

        self.lblStudentLoan = Label(LeftFrame2Right,text="Student Loan",font=("Arial",12,"bold"),bd=10,justify=CENTER)
        self.lblStudentLoan.grid(row=2,column=0,sticky=W)
        self.txtStudentLoan = Entry(LeftFrame2Right,textvariable=StudentLoan,font=("Arial",12,"bold"),bd=5,width=20,state=DISABLED,justify=LEFT)
        self.txtStudentLoan.grid(row=2,column=1,sticky=W)

        self.lblNIPayment = Label(LeftFrame2Right,text="NI Payment",font=("Arial",12,"bold"),bd=10,justify=CENTER)
        self.lblNIPayment.grid(row=3,column=0,sticky=W)
        self.txtNIPayment = Entry(LeftFrame2Right,textvariable=NIPayment,font=("Arial",12,"bold"),bd=5,width=20,state=DISABLED,justify=LEFT)
        self.txtNIPayment.grid(row=3,column=1,sticky=W)

#################################################################################################################

        self.lblGrossPay = Label(LeftFrame3Left,text="Gross Pay",font=("Arial",12,"bold"),padx=10,bd=10,justify=CENTER)
        self.lblGrossPay.grid(row=3,column=0,sticky=W)
        self.txtGrossPay = Entry(LeftFrame3Left,textvariable=GrossPay,font=("Arial",12,"bold"),bd=5,width=23,state=DISABLED,justify=LEFT)
        self.txtGrossPay.grid(row=3,column=1,sticky=W)

        self.lblDeductions = Label(LeftFrame3Right,text="Deductions",font=("Arial",12,"bold"),padx=10,bd=10,justify=CENTER)
        self.lblDeductions.grid(row=3,column=0,sticky=W)
        self.txtDeductions = Entry(LeftFrame3Right,textvariable=Deductions,font=("Arial",12,"bold"),bd=5,width=23,state=DISABLED,justify=LEFT)
        self.txtDeductions.grid(row=3,column=1,sticky=W)

#####################################Calculator ##############################################################

        self.txtDisplay = Entry(RightFrame1a,textvariable=text_Input,font=("Arial",18,"bold"),bd=10,insertwidth=4,justify=RIGHT)
        self.txtDisplay.grid(row=0,column=0,columnspan=4,pady=16)

        self.btnDigit7 = Button(RightFrame1a,padx=6,pady=7,bd=2,font=('arial',16,'bold'),width=4,text="7",command=lambda:btnClick(7)).grid(row=1,column=0)
        self.btnDigit8 = Button(RightFrame1a, padx=6, pady=7, bd=2, font=('arial', 16, 'bold'), width=4, text="8",command=lambda:btnClick(8)).grid(
            row=1, column=1)
        self.btnDigit9 = Button(RightFrame1a, padx=6, pady=7, bd=2, font=('arial', 16, 'bold'), width=4, text="9",command=lambda:btnClick(9)).grid(
            row=1, column=2)
        self.btnAdd = Button(RightFrame1a, padx=6, pady=7, bd=2, font=('arial', 16, 'bold'), width=4, text="+",command=lambda:btnClick("+")).grid(
            row=1, column=3)

        self.btnDigit4 = Button(RightFrame1a,padx=6,pady=7,bd=2,font=('arial',16,'bold'),width=4,text="4",command=lambda:btnClick(4)).grid(row=2,column=0)
        self.btnDigit5 = Button(RightFrame1a, padx=6, pady=7, bd=2, font=('arial', 16, 'bold'), width=4, text="5",command=lambda:btnClick(5)).grid(
            row=2, column=1)
        self.btnDigit6 = Button(RightFrame1a, padx=6, pady=7, bd=2, font=('arial', 16, 'bold'), width=4, text="6",command=lambda:btnClick(6)).grid(
            row=2, column=2)
        self.btnSub = Button(RightFrame1a, padx=6, pady=7, bd=2, font=('arial', 16, 'bold'), width=4, text="-",command=lambda:btnClick("-")).grid(
            row=2, column=3)

        self.btnDigit1 = Button(RightFrame1a,padx=6,pady=7,bd=2,font=('arial',16,'bold'),width=4,text="1",command=lambda:btnClick(1)).grid(row=3,column=0)
        self.btnDigit2 = Button(RightFrame1a, padx=6, pady=7, bd=2, font=('arial', 16, 'bold'), width=4, text="2",command=lambda:btnClick(2)).grid(
            row=3, column=1)
        self.btnDigit3 = Button(RightFrame1a, padx=6, pady=7, bd=2, font=('arial', 16, 'bold'), width=4, text="3",command=lambda:btnClick(3)).grid(
            row=3, column=2)
        self.btnMulti = Button(RightFrame1a, padx=6, pady=7, bd=2, font=('arial', 16, 'bold'), width=4, text="*",command=lambda:btnClick("*")).grid(
            row=3, column=3)

        self.btnDigit0 = Button(RightFrame1a, padx=6, pady=7, bd=2, font=('arial', 16, 'bold'), width=4, text="0",command=lambda:btnClick(0)).grid(
            row=4, column=0)
        self.btnClean = Button(RightFrame1a, padx=6, pady=7, bd=2, font=('arial', 16, 'bold'), width=4, text="C",command=clear).grid(
            row=4, column=1)
        self.btnEqual = Button(RightFrame1a, padx=6, pady=7, bd=2, font=('arial', 16, 'bold'), width=4, text="=",command=equal).grid(
            row=4, column=2)
        self.btnDivide = Button(RightFrame1a, padx=6, pady=7, bd=2, font=('arial', 16, 'bold'), width=4, text="/",command=lambda:btnClick("/")).grid(
            row=4, column=3)

################################################### Functions Buttons #############################################################
        self.btnWages = Button(RightFrame1b, padx=16, pady=5, bd=5, font=('arial', 16, 'bold'), width=4, text="Wages",command=Payment).grid(
        row=0, column=0)
        self.btnDisplay = Button(RightFrame1b, padx=16, pady=5, bd=5, font=('arial', 16, 'bold'), width=4, text="Display",command=AddData).grid(
        row=0, column=1)
        self.btnUpdate = Button(RightFrame1b, padx=16, pady=5, bd=5, font=('arial', 16, 'bold'), width=4, text="Update",command=UpdateData).grid(
        row=0, column=2)
        self.btnDelete = Button(RightFrame1b, padx=16, pady=5, bd=5, font=('arial', 16, 'bold'), width=4, text="Delete",command=DeleteData).grid(
        row=1, column=0)
        self.btnReset = Button(RightFrame1b, padx=16, pady=5, bd=5, font=('arial', 16, 'bold'), width=4, text="Reset",command=Reset).grid(
        row=1, column=1)
        self.btnExit = Button(RightFrame1b, padx=16, pady=5, bd=5, font=('arial', 16, 'bold'), width=4, text="Exit",command=iExit).grid(
        row=1, column=2)


#########################################################################################################################################

#################################################### Second tab Treeview UI #############################################################
        TopFrame11 = Frame(Tab2Frame,bd=10,width=1340,height=100,relief=RIDGE)
        TopFrame11.grid(row=0,column=0)
        TopFrame12 = Frame(Tab2Frame,bd=10,width=1340,height=100,relief=RIDGE)
        TopFrame12.grid(row=1,column=0)
###############################################################################################################################
        self.lblTitle = Label(TopFrame11,text="Payroll Management System ",font=("Arial",20,"bold"),bd=10,justify=CENTER)
        self.lblTitle.grid(padx=72)
        scroll_x = Scrollbar(TopFrame12,orient=HORIZONTAL)
        scroll_y = Scrollbar(TopFrame12,orient=VERTICAL)
        self.PMS_Table = ttk.Treeview(TopFrame12,height=22,columns=("ref","fullname","address","employername","cityweighting","basicsalary","overtime","grosspay","tax","pension","nipayment","deductions","postcode","gender","payday","taxperiod","taxcode","ninumber","netpay"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        # scroll_x.config(command=self.PMS_Table.xview)
        # scroll_y.config(command=self.PMS_Table.yview)
        self.PMS_Table.heading("ref",text="Ref")
        self.PMS_Table.heading("fullname",text="Name")
        self.PMS_Table.heading("address",text="Address")
        self.PMS_Table.heading("employername", text="Employer Name")
        self.PMS_Table.heading("cityweighting",text="City Weighting")
        self.PMS_Table.heading("basicsalary",text="Basic Salary")
        self.PMS_Table.heading("overtime",text="Overtime")
        self.PMS_Table.heading("grosspay",text="Gross Pay")
        self.PMS_Table.heading("tax",text="Tax")
        self.PMS_Table.heading("pension",text="Pension")
        self.PMS_Table.heading("nipayment",text="NI Payment")
        self.PMS_Table.heading("deductions",text="Deductions")
        self.PMS_Table.heading("postcode",text="Postcode")
        self.PMS_Table.heading("gender",text="Gender")
        self.PMS_Table.heading("payday",text="Pay Day")
        self.PMS_Table.heading("taxperiod",text="Tax Period")
        self.PMS_Table.heading("taxcode",text="Tax Code")
        self.PMS_Table.heading("ninumber",text="NI Number")
        self.PMS_Table.heading("netpay",text="Net Pay")

        self.PMS_Table['show'] = 'headings'
        self.PMS_Table.column("ref",width=70)
        self.PMS_Table.column("fullname",width=70)
        self.PMS_Table.column("address",width=80)
        self.PMS_Table.column("employername",width=70)
        self.PMS_Table.column("cityweighting",width=70)
        self.PMS_Table.column("basicsalary",width=70)
        self.PMS_Table.column("overtime",width=70)
        self.PMS_Table.column("grosspay",width=70)
        self.PMS_Table.column("tax",width=70)
        self.PMS_Table.column("pension",width=70)
        self.PMS_Table.column("nipayment",width=70)
        self.PMS_Table.column("deductions",width=70)
        self.PMS_Table.column("postcode",width=70)
        self.PMS_Table.column("gender",width=70)
        self.PMS_Table.column("payday",width=70)
        self.PMS_Table.column("taxperiod",width=70)
        self.PMS_Table.column("taxcode",width=70)
        self.PMS_Table.column("ninumber",width=70)
        self.PMS_Table.column("netpay",width=70)
        self.PMS_Table.pack(fill=BOTH,expand=1)
        self.PMS_Table.bind("<ButtonRelease-1>",WagesInfo)
        DisplayData()


#####################################################################################################################################################

##################################################################Third Tab Note Pad UI ###############################################################
        TopFrame13 = Frame(Tab3Frame,bd=10,width=1340,height=100,relief=RIDGE)
        TopFrame13.grid(row=0,column=0)
###############################################################################################################################
        self.lblNote = Label(TopFrame13, text="Payroll Note Book ", font=("Arial", 40, "bold"), bd=10,
                              justify=CENTER)
        self.lblNote.grid(padx=72)

###############################################################################################################################
        self.txtNote = Text(TopFrame13,bd=10,width=163,height=30,font=("Arial",14,"bold"),relief=RIDGE)
        self.txtNote.grid(row=1,column=0)


######################################################################################################################################################

################################### PayrollManagementSystem Class Ends Here ########################################################################################

if __name__ == '__main__':
    root = Tk()
    application = PayrollManagementSystem(root)
    sv_ttk.set_theme('light')
    root.mainloop()
