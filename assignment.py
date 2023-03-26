def home_page(): 
      print("--------------Malaysia Bank Online Loan Management System (MBOLMS)-------------")  
      print("1.ADMIN")
      print("2.NEW CUSTOMER")
      print("3.REGISTERED CUSTOMER")

def main_menu():
      option1=input("enter your option :")
      if(option1=="1"):
            cls()
            admin_login()
      if(option1=="2"):
            cls()
            second_services()
      if(option1=="3"):
            cls()
            third_services()
      else:
            cls()
            main_menu()

def admin_login():
      adminid=input("Enter the admin id :")
      adminpw=input("Enter the admin password :")
      if (adminid=="admin" and adminpw=="admin88"):
            print("log in successful.Welcome admin")
            first_service()
      else:
            print("try again")
            home_page()

def first_service():
      cls()
      print("Here are the services for Admins")
      print("1.Verify New Customer")
      print("2.View transaction of bank")
      print("3.View transaction of specific user")
      print("4.view user of certain loan type")
      print("5.Exit") 
      admin_service()

def admin_service():
      service=input("Which service do you want? ")
      if (service=="1"):
            cls()
            verify()
      if (service=="2"):
            cls()
            transaction()
      if(service=="3"):
            cls()
            specific_user()
      if(service=="4"):
            cls()
            loantype()
      if(service=="5"):
            cls()
            home_page()
      else:
            admin_service()

def verify():
      f=open("user.txt","r+")
      he=open("verifiedcustomer.txt")
      g=open("verifiedcustomer.txt","a")
      h=open("user.txt")
      l = h.readlines()
      for k in l:
         print(k)
      print("Here are the verified users")
      for m in he:
         print(m)
      name=input("Enter the username you want to verify ")
      c=False
      for i in f:
            for j in i.split():
                  if (j==name):
                        c=True          
            if (c==True):
                  v=i.replace("NR","R")
                  g.writelines(v)
                  break 
      f.close()
      g.close()
      h.close()
      loanid=input("Enter the loan id ")
      date=input("Enter the loan payment day for every month ")
      print("user has been verified")
      dataofuser(name,loanid,date)

def dataofuser(name,loanid,date):
      f1= open("verifiedcustomer.txt","r")
      f2=open("details.txt","a")
      f2.write(loanid+' ')
      c= f1.readlines()
      for l in c:
            for r in l.split():
                  if (r==name):
                        c=True
            if (c==True):
                  k=l.split()
                  first=k[0]
                  second=k[1]
                  loantype=k[7]
                  username=k[12]
                  amount=int(k[8])
                  time=int(k[9])
                  if (loantype=="cl" or loantype=="CL"):
                        interest=14
                        k=(amount*time*interest)/(100*12)
                        total=k+amount
                        emi=total/time
                        f2.write(first+' '+second+' '+loantype+' '+format(amount)+' '+format(time)+' '+format(emi)+' '+date+' '+username+"\n")
                        f1.close()
                        f2.close()
                        first_service()
                  if (loantype=="el" or loantype=="EL"):
                        interest=5
                        k=(amount*time*interest)/(100*12)
                        total=k+amount
                        emi=total/time
                        f2.write(first+' '+second+' '+loantype+' '+format(amount)+' '+format(time)+' '+format(emi)+' '+date+' '+username+"\n")
                        f1.close()
                        f2.close()
                        first_service()
                  if (loantype=="hl" or loantype=="HL"):
                        interest=8
                        k=(amount*time*interest)/(100*12)
                        total=k+amount
                        emi=total/time
                        f2.write(first+' '+second+' '+loantype+' '+format(amount)+' '+format(time)+' '+format(emi)+' '+date+' '+username+"\n")
                        f1.close()
                        f2.close()
                        first_service()
                  if (loantype=="pl" or loantype=="PL"):
                        interest=5
                        k=(amount*time*interest)/(100*12)
                        total=k+amount
                        emi=total/time
                        f2.write(first+' '+second+' '+loantype+' '+format(amount)+' '+format(time)+' '+format(emi)+' '+date+' '+username+"\n")
                        f1.close()
                        f2.close()
                        first_service()

def transaction():
      f1=open("transaction.txt","r")
      print("emi--date--amount deposit--amount remaining")
      l = f1.readlines()
      for k in l:
         print(k)
      first_service()

def specific_user():
      f1=open("transaction.txt","r")
      id=input("Enter the id of user you want to search ")
      l=f1.readlines()
      print("emi--date--amount deposit--amount remaining")
      for k in l:
            for j in k.split():
                  if(j==id):
                        print(k)
                  else:
                        pass
      first_service()
def loantype():
      f1=open("details.txt","r")
      f2=open("transaction.txt","r")
      loanty=input("Enter the loan type ")
      c= f1.readlines()
      d=f2.readlines()
      if(loanty=="cl" or loanty=="CL"):
            for l in c:
                  k=l.split()
                  loantype=k[3]
                  id=k[0]
                  if(loantype=="CL" or loantype=="cl"):
                        for m in d:
                              for e in m.split():
                                    if(e==id):
                                          print(m)
      if(loanty=="hl" or loanty=="HL"):
            for l in c:
                  k=l.split()
                  loantype=k[3]
                  id=k[0]
                  if(loantype=="hl" or loantype=="HL"):
                        for m in d:
                              for e in m.split():
                                    if(e==id):
                                          print(m)
      if(loanty=="el" or loanty=="EL"):
            for l in c:
                  k=l.split()
                  loantype=k[3]
                  id=k[0]
                  if(loantype=="EL" or loantype=="el"):
                        for m in d:
                              for e in m.split():
                                    if(e==id):
                                          print(m)
      if(loanty=="pl" or loanty=="PL"):
            for l in c:
                  k=l.split()
                  loantype=k[3]
                  id=k[0]
                  if(loantype=="pl" or loantype=="PL"):
                        for m in d:
                              for e in m.split():
                                    if(e==id):
                                          print(m)
      first_service()

def second_services():
      print("Here are the services for New Customers")
      print("1.Loan details")
      print("2.Loan calculator")
      print("3.Register new customer")
      print("4.Exit")   
      newuser_service()

def newuser_service():
      service=input("enter the service that you want :")
      if (service=="1"):
            cls()
            loandetails()
      elif (service=="2"):
            cls()
            loancalculator()
      elif (service=="3"):
            cls()
            new_customer_registration()
      elif (service=="4"):
            cls()
            home_page()
      else :
            cls()
            newuser_service()

def loandetails():
      print("----------------LOAN DETAILS---------------")
      print("1. We provide educational loan at only 5percent intrest rate")
      print("2. We provide car loan at 14percent intrest rate")
      print("3. We provide home loan at 8percent intrest rate")
      print("4. We provide personal loan at 5percent intrest rate")
      gomenu()

def gomenu():
      go=input("Do you want to go the menu(y)? :")
      if (go=="y"):
            cls()
            second_services()
      else:
             gomenu()

def loancalculator():
      print("----------------LOAN CALCULATOR---------------")
      p=int(input("Enter the principal :"))    
      t=int(input("Enter the time(in months) :"))
      r=float(input("Enter the rate :"))   
      intrest=(p*t*r)/(100*12)
      total=p+intrest
      monthlypayment=total/t
      print("You should pay",monthlypayment,"monthly")  
      calculator_use_again()  

def calculator_use_again():
      calculator =input("Do you want to use loan calculator again?(y/n) :")
      if(calculator=="y"):
            cls()
            loancalculator()
      elif(calculator=="n"):
            cls()
            second_services()
      else:
            calculator_use_again()
newuser=[] 
def new_customer_registration(): 
      print("--------NEW CUSTOMER REGISTRATION---------")
      del newuser[:]
      fname=input("Enter your first name :")
      newuser.append (fname)
      sname=input("Enter your surname :")
      newuser.append(sname)
      adress=input("Enter your adress :")
      newuser.append(adress)
      email=input("Enter your mail :")
      newuser.append(email)
      number=input("Enter your phone number :")
      newuser.append(number)
      gender=input("Enter your gender(m | f) :")
      newuser.append(gender)
      Date_Of_Birth=input("Enter your date of birth(yyyy-mm-dd) :")
      newuser.append(Date_Of_Birth)
      loan_type=input("Enter the loan type(CL | HL |EL | PL) :")
      newuser.append(loan_type)
      loan_amount=input("Enter loan amount: ")
      newuser.append(loan_amount)
      loan_terms=input("Enter the loan terms in years :")
      newuser.append(loan_terms)
      citizenshipno=input("Enter the citizenship numbers :")
      newuser.append(citizenshipno)
      newuser.append("NR")
      register()
      

def details():   
      print("These are your detail")
      for i in newuser:
            print(i)
      correct()

def correct():
      option2= input("Are these detail correct(y or n)? :")
      if (option2=="n"):
                  cls()
                  new_customer_registration()
      elif (option2=="y"):
            with open("user.txt","a") as f:
                  for j in range(len(newuser)):
                        f.write(newuser[j]+" ")
                  print("your data are written in file successfully.Your id will get verified soon ")
                  f.write("\n")  
            f.close()  
            second_services()
      elif (option2!="y" and option2!="n"):
                  correct()

def register():
      userid=input("Enter your username :")
      password=input("Enter your password.(remember password should be strong and unique) :")
      passwordcheck=input("Enter your password again :")
      if(password==passwordcheck and password !=" "):
            print("Passwords match. Welcome new user")
            newuser.append(userid)
            newuser.append(password)
            details() 
      else:
            print("Try again")
            register()

def third_services():
      uname=input(str("Enter you username "))
      pw=input(str("Enter you password "))
      f=open("verifiedcustomer.txt","r")
      u=0
      p=0
      r=0
      c= f.readlines()
      for i in c:
            k=i.split()
            status=k[11]
            name=k[12]
            password=k[13]    
            if(status=="R" and name==uname and password==pw):
                  print("Log in successful")
                  cls()
                  registered_services(uname)
                  break
      else: 
            print("Log in failed")
            main_menu()

def registered_services(uname):
      print("1.View my loan details")
      print("2.Pay loan installement")
      print("3.View transaction history")
      print("4.Exit")
      choice1=input("Enter your choice ")
      if (choice1=="1"):
            cls()
            myloandetails(uname)
      if (choice1=="2"):
            cls()
            pay_loan(uname)
      if (choice1=="3"):
            cls()
            my_history(uname)
      if (choice1=="4"):
            cls()
            home_page()
      else:
            print("Invalid choice")
            cls()
            registered_services(uname)

def myloandetails(uname):
      f1=open("details.txt","r")
      l=f1.readlines()
      for k in l:
            for j in k.split():
                  if(j==uname):
                        print("id--name--loantype--loan amount--loantime--Emi--loan date")
                        print(k)
                        cls()
                        registered_services(uname)

def pay_loan(uname):
      from datetime import date
      loanid=input("Enter your loan id ")
      loanpay=float(input("Enter the amount you are installing "))
      today = date.today()
      d1 = int(today.strftime("%d"))
      d2=  today.strftime("%m")
      d3=  today.strftime("%Y")
      f1=open("details.txt","r")
      f2=open("transaction.txt","a")
      c= f1.readlines()
      for i in c:
            k=i.split()
            id=k[0]
            name=k[8]
            total=float(k[4])
            emi=float(k[6])
            emidate=int(k[7])
            remaining=float(total-loanpay)
            if(name==uname):
                  if(loanid==id):
                        if(d1>emidate):
                                    days=d1-emidate
                                    fine=days*100
                                    print("You are late in your installement day",fine,"is your fine")

                        else:
                                  pass
                        if(emi>loanpay):
                                    print("Sorry insufficient amount")
                        else:
                                    print("Loan amount paid")
                                    f2.write(loanid+' ')
                                    f2.write(format(emi)+' '+format(d1)+"-"+format(d2)+"-"+format(d3)+' '+format(loanpay)+' '+format(remaining)+"\n")
                                    f2.close()
                                    f1.close()
                                    cls()
                                    registered_services(uname)
                  else:
                        print("Loan id doesn't match") 
                        cls()
                        registered_services(uname)

def my_history(uname):
      f1=open("transaction.txt","r")
      uid=input("Enter your loan id ")
      l=f1.readlines()
      print("emi--date--amount deposit--amount remaining")
      for k in l:
            for j in k.split():
                  if(j==uid):
                        print(k)
                        cls()
                        registered_services(uname)

def cls(): 
      from os import system
      from time import sleep 
      sleep(1) 
      system('cls') 
home_page()
main_menu()