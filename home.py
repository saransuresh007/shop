
from re import S
import ssl
import login1
import register


class Customer_Bill:
   
    def __init__(self, Name, Address,Phone,Total_price):
            
        self.Name = Name
        self.Address = Address
        self.Phone = Phone
        self.Total_Price = Total_price

    def getAddress(self):
        return self.Address

    def getName(self):
        return self.Name 

    def getTotal_price(self):
        return self.Total_Price

    def getPhone(self):
        return self.Phone

    
       
class Item: 
    def __init__(self,id, name, price):
        self.id=id        
        self.name = name
        self.price = price

    def getPrice(self):
        return self.price

    def getName(self):
        return self.name

    def getid(self):
        return self.id


class Cart:
    def __init__(self, list):
        self.list = []

    def addItem(self, item):
        self.list.append(item)

    def getTotal(self):
        total = 0
        for j in self.list:
              # or price = item[1]
            total = total + j.price
        return total

    def getNumItems(self):
        count = 0
        for c in range(self.list):
            count = self.list + 1
            return count
    
    def Display(self):
        count=1
        for i in self.list:
            print(count,':',i.name,i.id,i.price)
            count=count+1
        print("Total Price:",self.getTotal())

    def removeItem(self, item):
        return 0
        



class Categories:
    
    def additem():
       
        Items.append(Item(1001,'Heels',500))
        Items.append(Item(1002,'Flats',200))
        Items.append(Item(1003,'Boots',1000))
        Items.append(Item(2001,'Flipflops',200))
        Items.append(Item(2002,'sports shoes',1250))
        Items.append(Item(2003,'casual shoes',2000))
        Items.append(Item(3001,'Girls',600))
        Items.append(Item(3002,'Boys',600))
        Items.append(Item(3003,'Infants',500))
        

    def Types(*args):
       
        usercart = Cart([])
        print('1.Women\n','2.Men\n','3.Kids\n')
        category={1:'Women',2:'Men',3:'Kids'}
        Women = ({'Id':1001,'Name':'Heels','Price':500},{'Id':1002,'Name':'Flats','Price':200},{'Id':1003,'Name':'Boots','Price':1000})
        Men= ({'Id':2001,'Name':'Flipflops','Price':200},{'Id':2002,'Name':'sports shoes','Price':1250},{'Id':2003,'Name':'casual shoes','Price':2000})
        Kids= ({'Id':3001,'Name':'Girls','Price':600},{'Id':3002,'Name':'Boys','Price':600},{'Id':3003,'Name':'Infants','Price':500})
        for key,value in category.items():
            print(key,") ",value)
        while 1:
            usertype= int(input("select type of categories or Enter 0 to payment"))  
            if(usertype ==1 ):
                for i in Women:
                    print(i)
                id=int(input("Enter id:"))  
                for j in Items:
                    if (j.getid() == id):
                        print("added:",j.name,j.id)
                        usercart.addItem(j)
            elif(usertype ==2 ):
                
                for i in Men:
                    print(i)
                id=int(input("Enter id:"))  
                for j in Items:
                    if (j.getid() == id):
                        print("added:",j.name,j.id)
                        usercart.addItem(j)
            elif(usertype ==3 ):
                for i in Kids:
                    print(i)
                id=int(input("Enter id:"))  
                for j in Items:
                    if (j.getid() == id):
                        print("added:",j.name,j.id)
                        usercart.addItem(j)
            else:
                print("********** Checkout Cart **********")
                usercart.Display()
                TPrice = usercart.getTotal()

                check=int(input("Enter 1 for Payment \n  Enter 2 for add more :"))
                if(check == 1):
                    Name = input("Enter the Customer Name:")
                    Address = input("Enter the Customer Address :")
                    Phone = input("Enter the Customer Phone_Number:")
                    Customer.append(Customer_Bill(Name,Address,Phone,TPrice))

                    for i in Customer:

                        if(i.getPhone() == Phone):
                            print("\n ********************** BILL *************************")
                            print("Customer Name:",i.Name) 
                            print("Customer Address :",i.Address)
                            print("Customer Phone_Number:",i.Phone)
                            print("Total Amount:",TPrice)
                            print("\n ********************** BILL *************************\n")
                            check = 3
                            break
                            

                elif(check == 2):
                    continue
                break
        
        


        

   

        


ch=0
k=0
while 1:
    Items = []  
    usercart=[]
    Customer=[]
    UserBill=[]

    
    print("******************** Loading......Categories_Items")
    Categories.additem()
    print("********** Login System **********")
    if(ch == 1 or ch == 2 or k == 0):
        print("1.Signup")
        print("2.Login")
    if(k == 1 ):
        print("3.Logout")
        print("Press 5 to contine")
    if(k != 0 or ch ==0 ):
        ch = int(input("Enter your choice: "))
    if ch == 1:
       signup=register.NewRegister()
       signup.userselection()
       ch=4
    elif ch == 2:
       login=login1.Login()
       value = login.loginchoise()
       if(value == 1 ):
           print("Successfully Logged In")
           cart = Categories.Types()
           k=1
           ch=0
       elif(value == 2):
           print("Incorrect password Try again ")
           ch=0
    elif ch == 3:
        break
    elif ch == 5 :
        k=0
        ch=0
    else:
        print("worng Choice")
    
    
