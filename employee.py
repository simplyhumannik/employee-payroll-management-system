from tkinter import *
from tkinter import messagebox,ttk
import pymysql 
import time
import os
import tempfile
class EmployeeSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Payroll Management System")
        self.root.geometry("1360x700+0+0")
        self.root.config(bg="white")
        title = Label(self.root, text="Employee Payroll Management System", font=("times new roman", 30, "bold"), bg="#262626", fg="white", anchor="w", padx=10)
        title.place(x=0, y=0, relwidth=1)
        btn_emp=Button(self.root,text="All Employees",command=self.employee_frame, font=("times new roman", 13), bg="gray", fg="white")
        btn_emp.place(x=1100, y=10, height=35,width=120)

        #-----------------------Frame1----------------------
        #-----------------Frame1 Variables------------------
        self.var_emp_code=StringVar()
        self.var_designation=StringVar()
        self.var_name=StringVar()
        self.var_age=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_hr_location=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_proof_id=StringVar() #----Adhaar Card---
        self.var_contact=StringVar()
        self.var_status=StringVar()
        self.var_experience=StringVar()

        Frame1=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=70,width=750,height=620)
        title2 = Label(Frame1,text="Employee Details", font=("times new roman", 20), bg="lightgray", fg="black", anchor="w", padx=10)
        title2.place(x=0, y=0, relwidth=1)

        lbl_code=Label(Frame1,text="Employee Code", font=("times new roman", 20), bg="white", fg="black")
        lbl_code.place(x=10, y=70)
        self.txt_code=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_emp_code, bg="lightyellow", fg="black")
        self.txt_code.place(x=220, y=74,width=200)
        btn_search=Button(Frame1,text="Search",command=self.search, font=("times new roman", 20), bg="lightblue", fg="black")
        btn_search.place(x=440, y=72, height=30)

        # ----------------------Frame1 Row1 Col1---------------------------
        lbl_designation=Label(Frame1,text="Designation:", font=("times new roman", 20), bg="white", fg="black")
        lbl_designation.place(x=10, y=120)

        txt_designation=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_designation, bg="lightyellow", fg="black")
        txt_designation.place(x=170, y=125,width=200)
        # ----------------------Frame1 Row1 Col2---------------------------
        lbl_dob=Label(Frame1,text="D.O.B:", font=("times new roman", 20), bg="white", fg="black")
        lbl_dob.place(x=390, y=120)

        txt_dob=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_dob, bg="lightyellow", fg="black")
        txt_dob.place(x=520, y=125)

        # ----------------------Frame1 Row2 Col1---------------------------
        lbl_Name=Label(Frame1,text="Name:", font=("times new roman", 20), bg="white", fg="black")
        lbl_Name.place(x=10, y=170)

        txt_Name=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_name, bg="lightyellow", fg="black")
        txt_Name.place(x=170, y=175,width=200)
        # ----------------------Frame1 Row2 Col2---------------------------
        lbl_doj=Label(Frame1,text="D.O.J:", font=("times new roman", 20), bg="white", fg="black")
        lbl_doj.place(x=390, y=170)

        txt_doj=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_doj, bg="lightyellow", fg="black")
        txt_doj.place(x=520, y=175)

        # ----------------------Frame1 Row3 Col1---------------------------
        lbl_age=Label(Frame1,text="Age:", font=("times new roman", 20), bg="white", fg="black")
        lbl_age.place(x=10, y=220)

        txt_age=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_age, bg="lightyellow", fg="black")
        txt_age.place(x=170, y=225,width=200)
        # ----------------------Frame1 Row3 Col2---------------------------
        lbl_experience=Label(Frame1,text="Experience:", font=("times new roman", 20), bg="white", fg="black")
        lbl_experience.place(x=390, y=220)

        txt_experience=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_experience, bg="lightyellow", fg="black")
        txt_experience.place(x=520, y=225)

        # ----------------------Frame1 Row4 Col1---------------------------
        lbl_gender=Label(Frame1,text="Gender:", font=("times new roman", 20), bg="white", fg="black")
        lbl_gender.place(x=10, y=270)

        txt_gender=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_gender, bg="lightyellow", fg="black")
        txt_gender.place(x=170, y=275,width=200)
        # ----------------------Frame1 Row4 Col2---------------------------
        lbl_proof=Label(Frame1,text="Proof ID:", font=("times new roman", 20), bg="white", fg="black")
        lbl_proof.place(x=390, y=270)

        txt_proof=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_proof_id, bg="lightyellow", fg="black")
        txt_proof.place(x=520, y=275)

        # ----------------------Frame1 Row5 Col1---------------------------
        lbl_email=Label(Frame1,text="Email:", font=("times new roman", 20), bg="white", fg="black")
        lbl_email.place(x=10, y=320)

        txt_email=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_email, bg="lightyellow", fg="black")
        txt_email.place(x=170, y=325,width=200)
        # ----------------------Frame1 Row5 Col2---------------------------
        lbl_contact=Label(Frame1,text="Contact:", font=("times new roman", 20), bg="white", fg="black")
        lbl_contact.place(x=390, y=320)

        txt_contact=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_contact, bg="lightyellow", fg="black")
        txt_contact.place(x=520, y=325)

        # ----------------------Frame1 Row6 Col1---------------------------
        lbl_hired=Label(Frame1,text="Hired Location:", font=("times new roman", 18), bg="white", fg="black")
        lbl_hired.place(x=10, y=372)

        txt_hired=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_hr_location, bg="lightyellow", fg="black")
        txt_hired.place(x=170, y=375,width=200)
        # ----------------------Frame1 Row6 Col2---------------------------
        lbl_status=Label(Frame1,text="Status:", font=("times new roman", 20), bg="white", fg="black")
        lbl_status.place(x=390, y=370)

        txt_status=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_status, bg="lightyellow", fg="black")
        txt_status.place(x=520, y=375)

        # ----------------------Frame1 Row7---------------------------
        lbl_address=Label(Frame1,text="Address:", font=("times new roman", 20), bg="white", fg="black")
        lbl_address.place(x=10, y=420)
        self.txt_address=Text(Frame1,font=("times new roman", 15), bg="lightyellow", fg="black")
        self.txt_address.place(x=170, y=425,width=550,height=150)


        #-----------------------Frame2----------------------
        #-----------------Frame1 Variables------------------
        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_salary=StringVar()
        self.var_t_days=StringVar()
        self.var_absent=StringVar()
        self.var_medical=StringVar()
        self.var_pf=StringVar()
        self.var_convence=StringVar()
        self.var_net_salary=StringVar()
        
        Frame2=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame2.place(x=770,y=70,width=580,height=300)
        title3 = Label(Frame2,text="Employee Salary Details", font=("times new roman", 20), bg="lightgray", fg="black", anchor="w", padx=10)
        title3.place(x=0, y=0, relwidth=1)

        lbl_month=Label(Frame2,text="Month", font=("times new roman", 18), bg="white", fg="black")
        lbl_month.place(x=10, y=60)
        txt_month=Entry(Frame2,font=("times new roman", 15),textvariable=self.var_month, bg="lightyellow", fg="black")
        txt_month.place(x=90, y=62,width=100)

        lbl_year=Label(Frame2,text="Year", font=("times new roman", 18), bg="white", fg="black")
        lbl_year.place(x=200, y=60)
        txt_year=Entry(Frame2,font=("times new roman", 15),textvariable=self.var_year, bg="lightyellow", fg="black")
        txt_year.place(x=260, y=62,width=100)

        lbl_salary=Label(Frame2,text="Basic Sal", font=("times new roman", 18), bg="white", fg="black")
        lbl_salary.place(x=365, y=60)
        txt_salary=Entry(Frame2,font=("times new roman", 15),textvariable=self.var_salary, bg="lightyellow", fg="black")
        txt_salary.place(x=465, y=62,width=100)
       

        # ----------------------Frame2 Row1 Col1---------------------------
        lbl_days=Label(Frame2,text="Total Days:", font=("times new roman", 20), bg="white", fg="black")
        lbl_days.place(x=10, y=120)

        txt_days=Entry(Frame2,font=("times new roman", 15),textvariable=self.var_t_days, bg="lightyellow", fg="black")
        txt_days.place(x=170, y=125,width=100)
        # ----------------------Frame2 Row1 Col2---------------------------
        lbl_absent=Label(Frame2,text="Absents:", font=("times new roman", 20), bg="white", fg="black")
        lbl_absent.place(x=300, y=120)

        txt_absent=Entry(Frame2,font=("times new roman", 15),textvariable=self.var_absent, bg="lightyellow", fg="black")
        txt_absent.place(x=430, y=125,width=100)

        # ----------------------Frame2 Row2 Col1---------------------------
        lbl_medical=Label(Frame2,text="Medical:", font=("times new roman", 20), bg="white", fg="black")
        lbl_medical.place(x=10, y=150)

        txt_medical=Entry(Frame2,font=("times new roman", 15),textvariable=self.var_medical, bg="lightyellow", fg="black")
        txt_medical.place(x=170, y=155,width=100)
        # ----------------------Frame2 Row2 Col2---------------------------
        lbl_pf=Label(Frame2,text="PF:", font=("times new roman", 20), bg="white", fg="black")
        lbl_pf.place(x=300, y=150)

        txt_pf=Entry(Frame2,font=("times new roman", 15),textvariable=self.var_pf, bg="lightyellow", fg="black")
        txt_pf.place(x=430, y=155,width=100)

        # ----------------------Frame2 Row3 Col1---------------------------
        lbl_convence=Label(Frame2,text="Convence:", font=("times new roman", 20), bg="white", fg="black")
        lbl_convence.place(x=10, y=180)

        txt_convence=Entry(Frame2,font=("times new roman", 15),textvariable=self.var_convence, bg="lightyellow", fg="black")
        txt_convence.place(x=170, y=185,width=100)
        # ----------------------Frame2 Row3 Col2---------------------------
        lbl_netsalary=Label(Frame2,text="Net Salary:", font=("times new roman", 20), bg="white", fg="black")
        lbl_netsalary.place(x=300, y=180)

        txt_netsalary=Entry(Frame2,font=("times new roman", 15),textvariable=self.var_net_salary, bg="lightyellow", fg="black")
        txt_netsalary.place(x=430, y=185,width=100)

        # -----------------------Frame2 Button Row-----------------------
        btn_calcualte=Button(Frame2,text="Calculate",command=self.calculate, font=("times new roman", 20), bg="pink", fg="black")
        btn_calcualte.place(x=100, y=235, height=50,width=120)

        self.btn_save=Button(Frame2,text="Save",command=self.add, font=("times new roman", 20), bg="lime", fg="black")
        self.btn_save.place(x=230, y=225, height=30,width=120)
        
        btn_clear=Button(Frame2,text="Clear",command=self.clear, font=("times new roman", 20), bg="orange", fg="black")
        btn_clear.place(x=360, y=225, height=30,width=120)

        self.btn_update=Button(Frame2,text="Update",state=DISABLED,command=self.update, font=("times new roman", 20), bg="yellow", fg="black")
        self.btn_update.place(x=230, y=260, height=30,width=120)

        self.btn_delete=Button(Frame2,text="Delete",state=DISABLED,command=self.delete, font=("times new roman", 20), bg="red", fg="black")
        self.btn_delete.place(x=360, y=260, height=30,width=120)

        #-----------------------Frame3----------------------
        Frame3=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame3.place(x=770,y=380,width=580,height=310)

        #------------------Frame3 Part1 Calculator Frame------------------
        self.var_txt=StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_txt.set(self.var_operator)

        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator=''

        def clear_cal():
            self.var_txt.set('')
            self.var_operator=''

        Cal_Frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        Cal_Frame.place(x=2,y=2,width=247,height=300)

        txt_Result=Entry(Cal_Frame,bg="lightyellow",textvariable=self.var_txt,font=("times now roman",20,"bold"),justify=RIGHT)
        txt_Result.place(x=0,y=0,relwidth=1,height=50)

        #----------------Frame3 Part1 Calculator Row1------------------
        btn_7=Button(Cal_Frame,text='7',command=lambda:btn_click(7),relief=FLAT,bg="lightgray",font=("times new roman",15,"bold"))
        btn_7.place(x=0.5,y=53,w=60,h=60)

        btn_8=Button(Cal_Frame,text='8',command=lambda:btn_click(8),relief=FLAT,bg="lightgray",font=("times new roman",15,"bold"))
        btn_8.place(x=61.5,y=53,w=60,h=60)

        btn_9=Button(Cal_Frame,text='9',command=lambda:btn_click(9),relief=FLAT,bg="lightgray",font=("times new roman",15,"bold"))
        btn_9.place(x=122.5,y=53,w=60,h=60)

        btn_div=Button(Cal_Frame,text='/',command=lambda:btn_click('/'),relief=FLAT,bg="lightgray",font=("times new roman",15,"bold"))
        btn_div.place(x=183.5,y=53,w=60,h=60)

        #----------------Frame3 Part1 Calculator Row2------------------
        btn_4=Button(Cal_Frame,text='4',command=lambda:btn_click(4),relief=FLAT,bg="lightgray",font=("times new roman",15,"bold"))
        btn_4.place(x=0.5,y=114,w=60,h=60)

        btn_5=Button(Cal_Frame,text='5',command=lambda:btn_click(5),relief=FLAT,bg="lightgray",font=("times new roman",15,"bold"))
        btn_5.place(x=61.5,y=114,w=60,h=60)

        btn_6=Button(Cal_Frame,text='6',command=lambda:btn_click(6),relief=FLAT,bg="lightgray",font=("times new roman",15,"bold"))
        btn_6.place(x=122.5,y=114,w=60,h=60)

        btn_mul=Button(Cal_Frame,text='*',command=lambda:btn_click('*'),relief=FLAT,bg="lightgray",font=("times new roman",15,"bold"))
        btn_mul.place(x=183.5,y=114,w=60,h=60)

        #----------------Frame3 Part1 Calculator Row3------------------
        btn_1=Button(Cal_Frame,text='1',command=lambda:btn_click(1),relief=FLAT,bg="lightgray",font=("times new roman",15,"bold"))
        btn_1.place(x=0.5,y=175,w=60,h=60)

        btn_2=Button(Cal_Frame,text='2',command=lambda:btn_click(2),relief=FLAT,bg="lightgray",font=("times new roman",15,"bold"))
        btn_2.place(x=61.5,y=175,w=60,h=60)

        btn_3=Button(Cal_Frame,text='3',command=lambda:btn_click(3),relief=FLAT,bg="lightgray",font=("times new roman",15,"bold"))
        btn_3.place(x=122.5,y=175,w=60,h=60)

        btn_min=Button(Cal_Frame,text='-',command=lambda:btn_click('-'),relief=FLAT,bg="lightgray",font=("times new roman",15,"bold"))
        btn_min.place(x=183.5,y=175,w=60,h=60)

        #----------------Frame3 Part1 Calculator Row4------------------
        btn_0=Button(Cal_Frame,text='0',command=lambda:btn_click(0),relief=FLAT,bg="lightgray",font=("times new roman",15,"bold"))
        btn_0.place(x=0.5,y=236,w=48,h=60)

        btn_dot=Button(Cal_Frame,text='.',command=lambda:btn_click('.'),relief=FLAT,bg="lightgray",font=("times new roman",15,"bold"))
        btn_dot.place(x=49.5,y=236,w=48,h=60)

        btn_clr=Button(Cal_Frame,text='C',command=clear_cal,relief=FLAT,bg="lightgray",font=("times new roman",15,"bold"))
        btn_clr.place(x=98.5,y=236,w=48,h=60)

        btn_sum=Button(Cal_Frame,text='+',command=lambda:btn_click('+'),relief=FLAT,bg="lightgray",font=("times new roman",15,"bold"))
        btn_sum.place(x=147.5,y=236,w=48,h=60)

        btn_equal=Button(Cal_Frame,text='=',command=result,relief=FLAT,bg="lightgray",font=("times new roman",15,"bold"))
        btn_equal.place(x=196.5,y=236,w=48,h=60)

        #----------------Frame3 Part2 Salary Frame------------------
        sal_Frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        sal_Frame.place(x=251,y=2,width=320,height=300)
        title_sal = Label(sal_Frame,text="Salary Receipt", font=("times new roman", 20), bg="lightgray", fg="black", anchor="w", padx=10)
        title_sal.place(x=0, y=0, relwidth=1)

        sal_Frame2=Frame(sal_Frame,bg="white",bd=2,relief=RIDGE)
        sal_Frame2.place(x=0,y=30,relwidth=1,height=230)
        self.sample=f'''\tCompany Name, XYZ\n\tAddress: Xyz, Floor4
------------------------------------------------
Employee ID\t\t:  
Salary Of\t\t  Mon-YYYY
Generated on\t\t:  DD-MM-YYYY
------------------------------------------------
Total Days\t\t:  DD
Total Present\t\t:  DD
Total Absent\t\t:  DD
Convence\t\t:  Rs.-----
Medical\t\t:  Rs.-----
PF\t\t:  Rs,-----
Gross Paymnet\t\t:  Rs.---------
Net Salary\t\t:  RS.---------
------------------------------------------------
This is computer generated slip, not 
required any signature
'''

        scroll_y=Scrollbar(sal_Frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)

        self.txt_salary_receipt=Text(sal_Frame2,font=("times new roman",13),bg="lightyellow",yscrollcommand=scroll_y.set)
        self.txt_salary_receipt.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_receipt.yview)
        self.txt_salary_receipt.insert(END,self.sample)

        self.btn_print=Button(sal_Frame,text="Print",state=DISABLED,command=self.print, font=("times new roman", 20), bg="grey", fg="black")
        self.btn_print.place(x=180, y=262, height=30,width=120)

        self.check_connection()
    
#--------------------------------All Functions---------------------------
    def search(self):
        try:
            con=pymysql.connect(host="localhost",user="root",password="",db="ems")
            cur=con.cursor()
            cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
            row=cur.fetchone()
            #print(rows)
            if row==None:
                messagebox.showerror("Error","Invalid Employee ID, please try with another emploee ID",parent=self.root)
            else:
                self.var_emp_code.set(row[0])
                self.var_designation.set(row[1])
                self.var_name.set(row[2])
                self.var_age.set(row[3])
                self.var_gender.set(row[4])
                self.var_email.set(row[5])
                self.var_hr_location.set(row[6])
                self.var_doj.set(row[7])
                self.var_dob.set(row[8])
                self.var_experience.set(row[9])
                self.var_proof_id.set(row[10]) 
                self.var_contact.set(row[11])
                self.var_status.set(row[12])
                self.txt_address.delete('1.0',END)
                self.txt_address.insert(END,row[13])
                self.var_month.set(row[14])
                self.var_year.set(row[15])
                self.var_salary.set(row[16])
                self.var_t_days.set(row[17])
                self.var_absent.set(row[18])
                self.var_medical.set(row[19])
                self.var_pf.set(row[20])
                self.var_convence.set(row[21])
                self.var_net_salary.set(row[22])
                file_=open('Salary_receipt/'+str(row[23]),'r')
                self.txt_salary_receipt.delete('1.0',END)
                for i in file_:
                    self.txt_salary_receipt.insert(END,i)
                file_.close()
                self.btn_save.config(state=DISABLED)
                self.btn_update.config(state=NORMAL)
                self.btn_delete.config(state=NORMAL)
                self.txt_code.config(state='readonly')
                self.btn_print.config(state=NORMAL)
                
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to: {str(ex)}')
    
    def clear(self):
        self.btn_save.config(state=NORMAL)
        self.btn_update.config(state=DISABLED)
        self.btn_delete.config(state=DISABLED)
        self.btn_print.config(state=DISABLED)
        self.txt_code.config(state=NORMAL)
        self.var_emp_code.set('')
        self.var_designation.set('')
        self.var_name.set('')
        self.var_age.set('')
        self.var_gender.set('')
        self.var_email.set('')
        self.var_hr_location.set('')
        self.var_doj.set('')
        self.var_dob.set('')
        self.var_experience.set('')
        self.var_proof_id.set('') 
        self.var_contact.set('')
        self.var_status.set('')
        self.txt_address.delete('1.0',END)

        self.var_month.set('')
        self.var_year.set('')
        self.var_salary.set('')
        self.var_t_days.set('')
        self.var_absent.set('')
        self.var_medical.set('')
        self.var_pf.set('')
        self.var_convence.set('')
        self.var_net_salary.set('')
        self.txt_salary_receipt.delete('1.0',END)
        self.txt_salary_receipt.insert(END,self.sample)
                

    def delete(self):
        if self.var_emp_code.get()=='':
            messagebox.showerror("Error","Employee ID must be required")
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",db="ems")
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
                #print(rows)
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID, please try with another emploee ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?")
                    if op==True:
                        cur.execute("delete from emp_salary where e_id=%s",(self.var_emp_code.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success","Record Deleted Successfully",parent=self.root)
                        self.clear()
                        
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')


    def add(self):
        if self.var_emp_code.get()=='' or self.var_net_salary.get()=='' or self.var_name.get()=='':
            messagebox.showerror("Error","Employee details are required")
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",db="ems")
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
                #print(rows)
                if row!=None:
                    messagebox.showerror("Error","This Employee ID has already avaialable in our record,try again with another ID",parent=self.root)
                else:
                    cur.execute("insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_emp_code.get(),
                        self.var_designation.get(),
                        self.var_name.get(),
                        self.var_age.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_hr_location.get(),
                        self.var_doj.get(),
                        self.var_dob.get(),
                        self.var_experience.get(),
                        self.var_proof_id.get(), 
                        self.var_contact.get(),
                        self.var_status.get(),
                        self.txt_address.get('1.0',END),
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_salary.get(),
                        self.var_t_days.get(),
                        self.var_absent.get(),
                        self.var_medical.get(),
                        self.var_pf.get(),
                        self.var_convence.get(),
                        self.var_net_salary.get(),
                        self.var_emp_code.get()+'.txt'
                    )                      
                    )
                    con.commit()
                    con.close()
                    file_=open('Salary_receipt/'+str(self.var_emp_code.get())+'.txt','w')
                    file_.write(self.txt_salary_receipt.get('1.0',END))
                    file_.close()

                    messagebox.showinfo("Success","Record added succesfully")
                    self.btn_print.config(state=NORMAL)

            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')

    def update(self):
        if self.var_emp_code.get()=='' or self.var_net_salary.get()=='' or self.var_name.get()=='':
            messagebox.showerror("Error","Employee details are required")
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",db="ems")
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
                #print(rows)
                if row==None:
                    messagebox.showerror("Error","This Employee ID is invalid,try again with valid Employee ID",parent=self.root)
                else:
                    cur.execute("UPDATE `emp_salary` SET ,`designation`='%s',`name`='%s',`age`='%s',`gender`='%s',`email`='%s',`hr_location`='%s',`doj`='%s',`dob`='%s',`experience`='%s',`proof_id`='%s',`contact`='%s',`status`='%s',`address`='%s',`month`='%s',`year`='%s',`basic_Salary`='%s',`t_days`='%s',`absent_days`='%s',`medical`='%s',`pf`='%s',`convence`='%s',`net_salary`='%s',`salary_receipt`='%s' WHERE `e_id`='%s'",
                    (
                        self.var_designation.get(),
                        self.var_name.get(),
                        self.var_age.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_hr_location.get(),
                        self.var_doj.get(),
                        self.var_dob.get(),
                        self.var_experience.get(),
                        self.var_proof_id.get(), 
                        self.var_contact.get(),
                        self.var_status.get(),
                        self.txt_address.get('1.0',END),
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_salary.get(),
                        self.var_t_days.get(),
                        self.var_absent.get(),
                        self.var_medical.get(),
                        self.var_pf.get(),
                        self.var_convence.get(),
                        self.var_net_salary.get(),
                        self.var_emp_code.get()+'.txt',
                        self.var_emp_code.get()
                    )                      
                    )
                    con.commit()
                    con.close()
                    file_=open('Salary_receipt/'+str(self.var_emp_code.get())+'.txt','w')
                    file_.write(self.txt_salary_receipt.get('1.0',END))
                    file_.close()

                    messagebox.showinfo("Success","Record updated succesfully")

            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')      
            
    def calculate(self):
        if self.var_month.get()=='' or  self.var_year.get()=='' or  self.var_salary.get()=='' or self.var_t_days.get()=='' or self.var_absent.get()=='' or self.var_emp_code.get()=='' or  self.var_name.get()=='' or self.var_status.get()=='':
            messagebox.showerror('Error','All fields are required')
        else:
            # self.var_net_salary.set("RESULT")
            # 35000/31==1752
            # 31-10=21*1752
            per_day=int(self.var_salary.get())/int(self.var_t_days.get())
            work_day=int(self.var_t_days.get())-int(self.var_absent.get())
            sal_=per_day*work_day
            deduct=int(self.var_medical.get())+int(self.var_pf.get())
            addition=int(self.var_convence.get())
            net_sal=sal_-deduct+addition
            self.var_net_salary.set(str(round(net_sal,2)))
            #-----------------Update the receipt-----------
            new_sample=f'''\tCompany Name, XYZ\n\tAddress: Xyz, Floor4
------------------------------------------------
Employee ID\t\t:  {self.var_emp_code.get()}
Salary Of\t\t  {self.var_month.get()}-{self.var_year.get()}
Generated on\t\t:  {str(time.strftime("%d:%m:%y"))}
------------------------------------------------
Total Days\t\t:  {self.var_t_days.get()}
Total Present\t\t:  {str(int(self.var_t_days.get())-int(self.var_absent.get()))}
Total Absent\t\t:  {self.var_absent.get()}
Convence\t\t:  Rs.{self.var_convence.get()}
Medical\t\t:  Rs.{self.var_medical.get()}
PF\t\t:  Rs.{self.var_pf.get()}
Gross Payment\t\t:  Rs.{self.var_salary.get()}
Net Salary\t\t:  RS.{self.var_net_salary.get()}
------------------------------------------------
This is computer generated slip, not 
required any signature
'''
            self.txt_salary_receipt.delete('1.0',END)
            self.txt_salary_receipt.insert(END,new_sample)
    
    def check_connection(self):
        try:
            con=pymysql.connect(host="localhost",user="root",password="",db="ems")
            cur=con.cursor()
            cur.execute("select * from emp_salary")
            rows=cur.fetchall()
            # print(rows)

        except Exception as ex:
            messagebox.showerror("Error",f'Error due to: {str(ex)}')
    
    def show(self):
        try:
            con=pymysql.connect(host="localhost",user="root",password="",db="ems")
            cur=con.cursor()
            cur.execute("select * from emp_salary")
            rows=cur.fetchall()
            # print(rows)
            self.employee_tree.delete(*self.employee_tree.get_children())
            for row in rows:
                self.employee_tree.insert('',END,values=row)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to: {str(ex)}')

    def employee_frame(self):
        self.root2 = Toplevel(self.root)
        self.root2.title("Employee Payroll Management System")
        self.root2.geometry("1000x500+120+100")
        self.root2.config(bg="white")
        title = Label(self.root2, text="All Employee Details", font=("times new roman", 30, "bold"), bg="#262626", fg="white", anchor="w", padx=10)
        title.pack(side=TOP,fill=X)
        self.root2.focus_force()

        scrolly=Scrollbar(self.root2,orient=VERTICAL)
        scrollx=Scrollbar(self.root2,orient=HORIZONTAL)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=BOTTOM,fill=X)
        self.employee_tree=ttk.Treeview(self.root2,columns=('e_id', 'designation', 'name', 'age', 'gender', 'email', 'hr_location', 'doj', 'dob', 'experience', 'proof_id', 'contact', 'status', 'address', 'month', 'year', 'basic_Salary', 't_days', 'absent_days', 'medical', 'pf', 'convence', 'net_salary', 'salary_receipt'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.employee_tree.heading('e_id',text='E. ID')
        self.employee_tree.heading('designation',text='Designation')
        self.employee_tree.heading('name',text='Name')
        self.employee_tree.heading('age',text='Age')
        self.employee_tree.heading('gender',text='Gender')
        self.employee_tree.heading('email',text='Email')
        self.employee_tree.heading('hr_location',text='Hr Loc.')
        self.employee_tree.heading('doj',text='D.O.J')
        self.employee_tree.heading('dob',text='D.O.B')
        self.employee_tree.heading('experience',text='Exp.')
        self.employee_tree.heading('proof_id',text='Proof ID')
        self.employee_tree.heading('contact',text='Contact')
        self.employee_tree.heading('status',text='Status')
        self.employee_tree.heading('address',text='Address')
        self.employee_tree.heading('month',text='Month')
        self.employee_tree.heading('year',text='Year')
        self.employee_tree.heading('basic_Salary',text='Basic Sal.')
        self.employee_tree.heading('t_days',text='Days')
        self.employee_tree.heading('absent_days',text='Absent')
        self.employee_tree.heading('medical',text='Med.')
        self.employee_tree.heading('pf',text='PF')
        self.employee_tree.heading('convence',text='Convence')
        self.employee_tree.heading('net_salary',text='Net Sal.')
        self.employee_tree.heading('salary_receipt',text='Sal. Receipt')
        self.employee_tree['show']='headings'

        self.employee_tree.column('e_id',width=50)
        self.employee_tree.column('designation',width=150)
        self.employee_tree.column('name',width=100)
        self.employee_tree.column('age',width=50)
        self.employee_tree.column('gender',width=100)
        self.employee_tree.column('email',width=250)
        self.employee_tree.column('hr_location',width=100)
        self.employee_tree.column('doj',width=100)
        self.employee_tree.column('dob',width=100)
        self.employee_tree.column('experience',width=50)
        self.employee_tree.column('proof_id',width=100)
        self.employee_tree.column('contact',width=100)
        self.employee_tree.column('status',width=100)
        self.employee_tree.column('address',width=300)
        self.employee_tree.column('month',width=100)
        self.employee_tree.column('year',width=100)
        self.employee_tree.column('basic_Salary',width=100)
        self.employee_tree.column('t_days',width=100)
        self.employee_tree.column('absent_days',width=50)
        self.employee_tree.column('medical',width=100)
        self.employee_tree.column('pf',width=100)
        self.employee_tree.column('convence',width=100)
        self.employee_tree.column('net_salary',width=100)
        self.employee_tree.column('salary_receipt',width=100)
        scrollx.config(command=self.employee_tree.xview)
        scrolly.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH,expand=1)
        self.show()
 
        self.root2.mainloop()
    
    def print(self):
        file_=tempfile.mktemp(".txt")
        open(file_,'w').write(self.txt_salary_receipt.get('1.0',END))
        os.startfile(file_,'print')   

root = Tk()
obj = EmployeeSystem(root)
root.mainloop()
