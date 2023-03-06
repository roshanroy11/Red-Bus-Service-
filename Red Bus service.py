print("Welcome Guest\n".rjust(35))
print("Please select the option with which you would like to proceed")
user_data={}
ticket_details={}
destin=[]
destin.append("1  From Philadelphia | To Michigan")
destin.append("2  From Michigan     | To Philadelphia")
destin.append("3  From Miami        | To New York")
destin.append("4  From New York     | To Miami")
total_bill=0

def getDestination(name):
    for x,y in ticket_details.items():
        if y["Name"]==name:
            #print(y["Destination"])
            temp_dest=y["Destination"].split("From")
            return int(temp_dest[0].strip())


def Payment(destination_number):
    #global total_bill

    if destination_number==1:
        #total_bill+=20
        return 20
    elif destination_number==2:
        #total_bill+=30
        return 30
    elif destination_number==3:
        #total_bill+=40
        return 40
    elif destination_number==4:
        #total_bill+=50
        return 50


def Display():
    print("\n")
    print("//////////////////////////////////////////////////////////")
    print("Booked Ticket and Bill Details".rjust(35))
    if ticket_details:
        global total_bill
        for x,y in ticket_details.items():
            print("\n")
            print("//////////////////////////////////////////////////////////")
            print("Name :. ".ljust(15),y["Name"])
            print("Gender : ".ljust(15),y["Gender"])
            print("Age : ".ljust(15),y["Age"])
            print("Destination : ".ljust(15),y["Destination"])
            print("Bill : ".ljust(15),y["Bill"])
            print("//////////////////////////////////////////////////////////")
        print("total bill".ljust(15),total_bill)
        print("\n")
    else:
        print("Sorry no tickets have been booked by you yet!")




def Destination():
    for x in destin:
        print(x)
    destination=int(input())
    return destination



def Modify(temp,name,new_detail):
    for x,y in ticket_details.items():
        if y["Name"]==name:
            y[temp]=new_detail
            #y["Gender"]="Female"
    #print(ticket_details)



def bookTicket():
    print("\n")
    print("//////////////////////////////////////////////////////////")
    print("Book Tickets".rjust(35))
    global total_bill
    global ticket_details
    while True:
        try:
            no_tickets = int(input("How many bus tickets do you want: "))
            if type(no_tickets)==int:
                break
        except:
            print("The enter value is not right! Please enter a integer")
    for t in range(no_tickets):
        while True:
            name = input("Enter the name : ").capitalize()
            if any(i.isdigit()for i in name):
                print("\nPlease enter a proper name with only alphabets")
                continue
            gender=input("Enter the Gender :").capitalize()
            if any(i.isdigit() for i in gender):
                print("\nPlease enter the Gender as 'Male' or 'Female' with only alphabets")
                continue
            try:
                age=int(input("Enter the age :"))
                if type(age)==int:
                    break
            except:
                print("Please enter your age in numeric")

        print("Choose the Destination you want to go below:")
        dest=Destination()
        bill=Payment(dest)
        total_bill=total_bill+bill
        #len(ticket_details)
        #ticket_details={0:{"Name"}
        ticket_details[t]={"Name":name,"Gender":gender,"Age":age,"Destination":destin[dest-1],"Bill":bill}
    #print("Total Bill :",total_bill)
    #print(ticket_details)
    Display()


def modify_details():
    temp=1
    print("\n")
    print("//////////////////////////////////////////////////////////")
    print("Modify Service".rjust(35))
    if ticket_details:
        global total_bill
        get_info=0
        print("Whose details would you like to modify")
        name=input().capitalize()
        #see if such a user exists
        for x,y in ticket_details.items():
            if name in y["Name"]:
                temp=0
                print("\nPlease select which of the following details would you like to modify")

                while True:
                    while True:
                        print("1.Name")
                        print("2.Gender")
                        print("3.Age")
                        print("4.Destination")
                        print("5.View Modified Details")
                        print("6.Exit")
                        print("Please choose the option Number")
                        #get_info=int(input())
                        try:
                            get_info=int(input())
                            if type(get_info)==int:
                                break
                        except:
                            print('Please enter the choice "number"')
                            print("\nThe choice you entered is incorrect\n")
                            continue

                        #print(get_info)
                    if get_info==1:
                        new_detail=input("please enter the correct name").capitalize()
                        Modify("Name",name,new_detail)
                        name=new_detail
                        print("\nPlease select the option number for which you wish to make more correction")
                        print("If not press '6'\n")
                    elif get_info==2:
                        new_detail=input("please enter the correct Gender").capitalize()
                        Modify("Gender",name,new_detail)
                        print("\nPlease select the option number for which you wish to make more correction")
                        print("If not press '6'\n")
                    elif get_info==3:
                        new_detail=input("please enter the correct Age")
                        Modify("Age",name,new_detail)
                        print("\nPlease select the option number for which you wish to make more correction")
                        print("If not press '6'\n")
                    elif get_info==4:
                        print("\nPlease enter the correct Destination")
                        previous_destination=getDestination(name)
                        previous_destination_bill=Payment(previous_destination)
                        #print("previous_destination",previous_destination)
                        #print("previous_destination_bill",previous_destination_bill)
                        #print(type(previous_destination_bill))
                        #print(total_bill)
                        total_bill=total_bill-previous_destination_bill
                        #print(total_bill)
                        new_detail=Destination()
                        bill=Payment(new_detail)
                        total_bill=total_bill+bill

                        Modify("Destination",name,destin[new_detail-1])
                        Modify("Bill",name,bill)
                        print("\nPlease select the option number for which you wish to make more correction")
                        print("If not press '6'\n")
                        #Display()
                    elif get_info==5:
                        print("\nModified Details\n".rjust(35))
                        Display()
                    elif get_info==6:
                        break
                    else:
                        print("Please select appropriate option")
        if temp==1:
            print("Sorry, there is no such Customers available! Kindly view the tickets booked!\n")
            print("The ticket is booked for following Customers :\n")
            for x,y in ticket_details.items():
                print(y["Name"])



    else:
        print("\n Sorry no Details exists to be Modified \n ")



def Book_Menu(name):
    print("\n")
    print("//////////////////////////////////////////////////////////")
    print("Red Bus Services".rjust(35))
    get_info=0
    print("\n")
    print(f"Hello {name},Select the Service Number you would like to avail.")
    while True:
        while True:
            print("\n")
            print("1.Book Bus ticket")
            print("2.Change Details of the Booked Ticket")
            print("3.Show Booked Tickets")
            print("4.Exit\n")
            try:
                get_info=int(input("Please select your choice number\n"))
                if type(get_info)==int:
                    break
            except:
                print("\nThe choice you entered is incorrect\n")
                print("Please enter an 'Integer'")
                continue

            #print(get_info)
        if get_info==1:
            bookTicket()
            #pass
            #login()
        elif get_info==2:
            modify_details()
            #signUp()
            #pass
        elif get_info==3:
            Display()
        elif get_info==4:
            break
        else:
            print("Please select appropriate option\n")





def signUp():
    print("\n")
    print("//////////////////////////////////////////////////////////")
    print("SignUp".rjust(35))
    print("\nHello user, please enter a username".ljust(45))
    name=input()
    while True:
        password=input("Please enter a password".ljust(35))
        password2=input("Please re-enter your password".ljust(35))
        if password==password2:
            user_data[name]=password
            break

        else:
            print("The passwords did not match!!Please try again\n")
            continue
    #print(user_data)



def login():
    temp=1
    print("\n")
    print("//////////////////////////////////////////////////////////")
    print("Login".rjust(35))
    if user_data:
        count=3
        print("Please enter your Username and Password")
        name=input("Username :".ljust(15))
        #print("Please enter your password")
        pwd=input("Password :".ljust(15))
        for username,password in user_data.items():
            if username==name:
                temp=0
                if password==pwd:
                    #print("Welcome ",name)
                    Book_Menu(name)
                    break
                else:
                    while count>1:
                        count-=1
                        print("Sorry! The password entered is incorrect")
                        print(f"please try again! You have more {count} tries!")
                        print("username : ".ljust(15),name)
                        pwd=input("password : ".ljust(15))
                        if password==pwd:
                            #print("Welcome ",name)
                            Book_Menu(name)
                            break

            if count==1:
                print("Sorry! your account has been locked, Try again Later!")

        if temp==1:
            print("Sorry! the username does not exist. Please create an account.")

    else:
        print("Please create a ID before you can Login!!")



def Menu():

    get_info=0
    while True:
        while True:
            print("\n")
            print("//////////////////////////////////////////////////////////")
            print("\n1.Login")
            print("2.SignUp")
            print("3.Exit")
            print("Please choose the option Number")
            try:
                get_info=int(input())
                break
            except:
                print('Please enter the choice "number"')
                print("\nThe choice you entered is incorrect\n")
                continue

            #print(get_info)
        if get_info==1:
            #print("got in 1")
            #pass
            login()
        elif get_info==2:
            signUp()
            #pass
        elif get_info==3:
            break
        else:
            print("Please select appropriate option")

3

Menu()