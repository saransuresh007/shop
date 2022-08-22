registereduser = {'rithi':'rithi@12','dhilip':'dlp23','priya':'pri89'}
registeredadmin= {'peter':'peter34','saranya':'saran290','sanju':'sanju987'}
class Login():     
    def  userlogin(*args):
        print("NEW USER") 
        username=input("Enter username :")
        password=input("Enter passsword :")   
        print("name :",username,"\npassword:",password)    
        if username in registereduser and password in registereduser[username]:
            return 1
        else:
            return 2

    def adminlogin(*args):
        print("Admin") 
        username=input("Enter username :")
        password=input("Enter passsword :")   
        print("name :",username,"\npassword:",password)
        if username in registeredadmin and password in registeredadmin[username]:
            return 1
        else:
            return 1

    def loginchoise(*args):
        print("Enter user name")
        print("1.userlogin\n","2.adminlogin\n")
        usertype= (int(input("select type of user:")))
        
        if usertype==1:
            return (Login.userlogin())
        elif usertype==2:
            return  (Login.adminlogin())
        else:
            print("invalid")



