class NewRegister:
       
    def newuser(*args):
        print("NEW USER")
        username=input("Enter username :")
        password=input("Enter passsword :")
        Emailid=input("Enter Emailid:")
        phonenumber=input("Enter phonenumber :")

        print("name :",username,"\npassword:",password,"\nEmailid:",Emailid,"\nphonenumer",phonenumber)

    def newadmin(*args):

        print("NEW ADMIN")
        username=input("Enter username :")
        password=input("Enter passsword :")
        Emailid=input("Enter Emailid:")
        phonenumber=input("Enter phonenumber :")
        print("name :",username,"\npassword:",password,"\nEmailid:",Emailid,"\nphonenumer",phonenumber)

    def userselection(*args):
        print("-----WHICH TYPE OF USER ARE YOU ?-------")

        new_user=int(input("\nSELECT TYPE OF USER : 1.new user \n 2.admin")) 
        if new_user==1:
            NewRegister.newuser()
        elif new_user==2:
            NewRegister.newadmin()
        else:
            print("invalid") 
