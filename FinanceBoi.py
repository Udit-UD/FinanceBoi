# A program to manage your monthly expenses     - By Udit

import csv
import datetime

pocmon= 5000            #Enter your Pocket Money here

def add_data():
    with open('June.csv','a', newline= "") as f:
        thewriter=csv.writer(f, delimiter=',')
        ans='y'
        while(ans=='y'):
            name=input("\nEnter description of product: ")
            price=int(input("Enter price of this purchase: "))
            date=datetime.date.today()
            info=[name,price,date]
            thewriter.writerow(info)    
            print("Record saved Successfully!!!\n")
            ans=input("Enter 'y' if you want to add more purchases else enter 'n': ")
            print("\n")
    f.close()

def today():
    with open('June.csv','r',newline="") as f:
        thereader=csv.reader(f, delimiter=',')
        rows=[]
        sum=0
        for row in thereader:
            rows.append(row)
        for day in rows:
            if (day[2]==str(datetime.date.today())):
                sum=sum+int(day[1])
        print("Your Today's Expenditure is: ", sum,'Rs\n')
    f.close()

def exp():
    with open('June.csv','r',newline="") as f:
        thereader=csv.reader(f, delimiter=',')
        rows=[]
        sum=0
        string=input("\nEnter date: ")
        date='2022-06-'+string              #Change According to the month
        for row in thereader:
            rows.append(row)
        for day in rows:
            if (day[2]==str(date)):
                sum=sum+int(day[1])
        if sum!=0:
            print("Your Expenditure on ", date," is: ", sum,'Rs\n')
        elif sum==0:
            print("Sorry! No record found on this date kindly change it.\n")
            exp()
    f.close()
                
def print_data():
    with open('June.csv','r', newline="") as f:
        thereader=csv.reader(f, delimiter=',')
        rows=[]
        print('\n')
        for row in thereader:
            rows.append(row)
        for item in rows:
            if(len(item[0])<=6):
                print(item[0],"\t\t|",item[1],"\t|",item[2])
            elif(len(item[0])>=15):
                print(item[0],"|",item[1],"\t|",item[2])
            else:
                print(item[0],"\t|",item[1],"\t|",item[2])
    f.close()

def balance():
    pocmon=5000
    print("\nYour monthly Pocket Money is:" ,pocmon, "Rs")
    with open('June.csv','r') as f:
        sum=0
        thereader=csv.reader(f)
        rows=[]
        for row in thereader:
            rows.append(row)
            sum=sum+int(row[1])
    f.close()
    print("Done!!\nYour total expenditure till now is : ",sum)
    print("You have left with", pocmon-sum ,"Rs. only!")
    today()

def main():
    print("\n1. Add Expenses\n2. View Expenses\n3. Check your remaining balance\n4. To find Expenditure of particular date\n5. Exit\n")
    choice=int(input())
    if choice==1:
        add_data()
        today()
        main()
    elif choice==2:
        print_data()
        main()
    elif choice==3:
        balance()
        main()
    elif choice==4:
        exp()
        main()
    elif choice==5:
        print("\nThanks for maintaing your record, see you soon sir!\n")
    else:
        print("Wrong choice sir!")
        choice=int(input("Enter your choice again:"))
        main()
        
# Main: Program will run from here...

print("WELCOME TO FINANCEBOI\n")
def cred():
    lid=input("Enter your Login ID: ")
    password=input("Enter password: ")
    if (lid=='udit' and password=='Jarvis@3'):              #Create your credentials here
        print("Welcome Udit!")
    else:
        print("Access Denied!!\nEnter credentials again...\n")
        cred()
    
cred()
print("What do you want to do here Sir?")
main()
