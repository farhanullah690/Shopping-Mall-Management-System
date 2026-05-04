count=0
ch=chr='y'
while ch=='y':
    #Manu of All Modules
    print("******Shopping Mall******")
    print("*************************")
    print("Press 1 for inventry module")
    print("Press 2 for point of sale module")
    print("Press 3 for Customer Module")
    print("Press 4 for Employee Module")
    print("Press 5 for Security Module")
    print("")
    print("Enter your choice")
    choice=int(input(""))
    #Inventry Module
    if(choice==1):
        print("*************************")
        print("")
        print("Here is the inventry module")
        print("")
        print("1 for add product")
        print("")
        print("2 for view product")
        print("")
        print("3 for search product")
        print("")
        print("Enter your choice")
        choic=int(input(""))
        #Add Product 
        if(choic==1):
            #Add Product Name
            print("Enter product name")
            proname=input("")
            #Addd Product ID
            print("Enter product ID")
            proid=input("")
            print("")
            print("Added product succesfully")
            print("Complete table of this product")
            print("Name     ID")
            print( proname, proid)
        #View Product
        elif (choic==2):
            print("Showing all stock")
            print("")
            print("Complete Table of Stocks")
            print("  Name     Rupees     Quantity")
            print("1 dress     3000         4")
            print("2 Trouser   1500         3")
            print("3 Shirt     1500         5")
            print("Do Yoy Want To Buy Something or Not")
            print("Press 1 for Yes And 2 for No")
            bol=int(input())
            if(bol==1):
                print("ohh you enter 1 ")
                print("")
                print("Now what the thing do you want to purchase")
                print("Press 1 for dress 2 for trouser 3 for shirt")
                buy=int(input())
                if(buy==1):
                    print("you selected dress also type its quantity")
                    quan=int(input())
                    total=0
                    total=int(quan*3000)
                    print("Here is your bill",total)
                elif (buy==2):
                    print("You selected trouser also type its quantity")
                    quant=int(input())
                    tota=0
                    tota=quant*1500
                    print("You bill is",tota)
                elif (buy==3):
                    print("You enter 3 for shirt also type its quantity")
                    quantity=int(input())
                    tot=0
                    tot=quantity*1500
                    print("Here is your bill",tot)
                else:
                    print("You entered invalid choice")
            print("Thanks for visiting")
        #Search Product    
        elif (choic==3):
            print("Enter product name")
            prod=str(input())
            print("Product found! Rs999/ And Also this product is on 50% off")
        else:
            print("")
            print("You entered Invalid Choice")
    #Point of Sale Module
    elif (choice== 2):
        print("*********************")
        print("")
        print("Here is the point of sale module")
        print("")
        print("*********************")
        print("")
        print("Press 1 for new bill")
        print("Press 2 for return product")
        print("Press 3 for Payment Module")
        print("Enter your choice")
        cho=int(input(""))
        #New Bill
        if  cho== 1:
            #Add New Bill
            print("Enter you bill ANd if your bill is greater then 2000 Then you will get 10% discount")
            bill=int(input())
            #Added Discount
            dis=0
            if(dis>2000):
                dis=bill*10/100
                print("You get a discount of 10% So your final bill is=",dis)
            else:
                print("your bill is=",bill)
            print("New bill added")
        #Return Product
        elif(cho==2):
            print("Enter product Name: But remember if you need to returns product your deduction from your bill is -100Rs")
            pronamee=str(input(""))
            print("Press 1 for yes and 2 for no")
            rp=int(input())
            if(rp==1):
                print("Enter your item amount")
                i_a=int(input())
                totall=0
                #Calculate Discont
                totall=i_a-100
                print("Here is your final bill",totall)
            else:
                print("Thanks for visiting")
        #Payment Module
        elif(cho==3):
            print("Only Cash payment available")
        else:
            print("You Entered Invalid Choice")
    #Customer Module
    elif(choice==3):
        print("****************************")
        print("")
        print("Here is the customer Module")
        print("")
        print("*****************************")
        print("")
        print("Press 1 for add new customer")
        print("Press 2 for customer history")
        print("Press 3 for check customer loyalty poinys")
        print("Enter your choice")
        ch=int(input(""))
        #Add New Customer
        if(ch==1):
            #Add Customer Name
            print("Enter customer name")
            c_n=str(input(""))
            #Add Customer Age
            print("Enter customer age")
            c_a=int(input(""))
            #Add Customer ID
            print("Enter customer id")
            c_id=int(input(""))
            print("")
            print("Customer Added Succesfully")
            print("")
            print("Here is the complete table of the new customer")
            print("Name     Age     ID")
            print( c_n,     c_a,    c_id)
        #Check Customer History
        elif(ch==2):
            print("Here is the customer history since last 2 days")
            print("")
            print("Last puschases 2 days ago")
        #Check Customer Loyalty Points
        elif(ch==3):
            print("Enter Customer name")
            C_pts=str(input(""))
            print("")
            print("This customer has 450 pts")
        else:
            print("You entered invalid choice")
    #Employee Module
    elif(choice==4):
        print("******************************")
        print("")
        print("Here is the Employee Module")
        print("")
        print("******************************")
        print("")
        print("Press 1 for add new employee")
        print("Press 2 for check Employee sallary")
        print("Press 3 for mark attendence")
        print("Enter your choice")
        m_ch=int(input(""))
        #Add New Employee
        if(m_ch==1):
            #Add Employee Name
            print("ENter employee name")
            e_n=str(input(""))
            #Check Employee Salary
            print("Enter employee Age")
            e_a=int(input(""))
            
            print("ENter employee ID")
            e_id=int(input(""))
            print("")
            print("Employee Added Succesfully")
            print("")
            print("Here is the complete table of new Employee")
            print("")
            print("Name     Age     ID")
            print( e_n,     e_a,    e_id)
        #Check Employee Salary
        elif(m_ch==2):
            #Per Days Rs/500
            print("Enter duty Days")
            e_d=int(input(""))
            #Count Monthly Salary
            Total=e_d*500
            #Count Yearly Salary
            total=e_d*500*12
            print("Here is the Employee sallary of the typed days",Total)
            print("And Here is the yearly sallary of the Employee",total)
        #Mark Employee Attendence
        elif(m_ch==3):
            print("If the Employee is present the press 1 and 2 for Absent")
            e_p=int(input(""))
            if(e_p==1):
                print("Your Presence Has been counted")
                print("")
            else:
                print("This Employee is absent")
        else:
            print("You enetered invalid choice")
    #Security Module
    elif(choice==5):
        print("*******************************")
        print("")
        print("Here is the Security Module")
        print("")
        print("*******************************")
        print("")
        print("Press 1 for view CCTV")
        print("Press 2 for Access log")
        print("Press 3 for Emergency Allerts")
        print("Enter your choice")
        s_ch=int(input(""))
        #View CCTV
        if(s_ch==1):
            print("")
            print("CCTV LIVE! 12 Cameras Active")
        #Access Log
        elif(s_ch==2):
            print("")
            print("Press any num to Access log")
            anum=int(input(""))
            print("Last Entry at 12 am")
        #Emergency Allerts
        elif(s_ch==3):
            print("Press any num to allert emergency allarms")
            anumm=int(input(""))
            print("Aller! Fire Allarns Trriggered")
        else:
            print("You entered invalid choice")
    else:
        print("You Entered invalid choice")
    #For Repeating Manu Again
    print("DO YOU WANT TO SEE THE MANU AGAIN")
    print("Then Enter Y : No for Any key Except Y")
    ch=(input(""))
    count=count+1