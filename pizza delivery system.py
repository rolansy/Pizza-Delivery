import pickle
import os


#function to display menu
def menu():
    g1=" "*7
    g2=" "*16
    g3=" "*3
    f=["FAMILY MEAL","KIDS MEAL  ","MY BOX     ","SUPER LIMO "]
    m=[5.5,1.5,3.0,8.0]
    x=["0010","0020","0030","0040"]
    print(" "*60 ,"╔"*1,"═"*58,"╗"*1,sep="")
    d=f"{'║':>61s}{'THANK YOU FOR VISITING PIZZA STATION':>48s}{'║':>11s}"
    c=f"{'║':>61s}{'MENU':>31s}{'║':>28s}" 
    h=f"{'║':>61s}{'SL':>3s} {g1} {'ITEMS':^3s} {g2} {'ITEMCODE':^6s} {g3} {'PRICE(KD)':^6s}{'║':>2s}"
    g2=" "*10
    g3=" "*9
    print(d)
    print(" "*59 ,"║"*1," "*56 ,"║"*1)
    print(c)
    print(" "*59,"║","~"*56,"║")
    print(h)
    print(" "*59,"║","="*56,"║")
    for i in range(4):
          h=f"{'║':>61s}{i+1:>2d}{'.':<1s} {g1} {f[i]:^3s} {g2} {x[i]:>6s} {g3} {m[i]:>3.1f}{'║':>4s}"
          print(h)
    print(" "*60 ,"╚"*1,"═"*58 ,"╝"*1,sep="")
    
    
#function to create records   
def create():
    f=open('foods.dat','wb')
    ch='yes'
    c=1
    while ch.lower()=='yes' :
        print('\n')
        print('Enter details of the customers',c)
        while True:
            flag=0
            Itemcode=input('Enter the Itemcode                           :  ')
            for v in d.values():
                if Itemcode==v[0]:
                    pr=v[1]
                    flag=1
            if not Itemcode.isdigit() or len(Itemcode)!= 4 :
                flag=0
            if flag==0:
                print('Enter valid Itemcode')
            else:
                break
        flag=True    
        try:
            Qtytno=int(input('Enter the number of quantities               :  '))
            Custfrstname=input('Enter the customer\'s first name              :  ')
            Custlstname=input('Enter the customer\'s last name               :  ')
            Are=str(input('Enter the Area name                          :  '))
            Blokno=int(input('Enter the block number                       :  '))
            Stretno=int(input('Enter the street number                      :  '))
            Bludno=int(input('Enter the building number                    :  '))
            Flono=int(input('Enter the floor number                       :  '))
            Romno=int(input('Enter the flat number                        :  '))
            Cstprc=pr*Qtytno
            print('                   Price=',Cstprc,'Kd')
            print('                     ---THE END---   ')
            c+=1
    
            l=[Itemcode , Qtytno, Custfrstname, Custlstname, Are, Blokno, Stretno, Bludno, Flono, Romno,Cstprc]
            pickle.dump(l,f)
            
        except:
            print("error")
            flag=False
        if flag==False:
            ch=input('Enter again? [Yes/No] : ')
        else:
            ch=input('Would you like to enter more? [Yes/No] : ')
            

#function to search a record
def search():
    ne=input("Enter Customer\'s first Name                  :  ")
    na=input("Enter Customer\'s last Name                   :  ")
    file=open("foods.dat","rb")
    l=[]
    try:
        while True:
            l=pickle.load(file)
            if ne.lower()==l[2].lower() and na.lower()==l[3].lower():
                print(' '*58,'╔','═'*43,'╗',sep='')
                print(' '*57,' ',' '*14,'SEARCH FOUND',' '*13,' ')
                print(' '*57,f"{' ':>1s}{'Itemcode':<27s}{':':^1s}{l[0]:>15s}{' ':>1s}")
                print(' '*57,f"{' ':>1s}{'Quantities':<27s}{':':^1s}{l[1]:>15d}{' ':>1s}")             
                print(' '*57,f"{' ':>1s}{'Customer first name':<27s}{':':^1s}{l[2].lower().capitalize():>15s}{' ':>1s}")
                print(' '*57,f"{' ':>1s}{'Customer last name ':<27s}{':':^1s}{l[3].lower().capitalize():>15s}{' ':>1s}")
                print(' '*57,f"{' ':>1s}{'Area name':<27s}{':':^1s}{l[4].lower().capitalize():>15s}{' ':>1s}")
                print(' '*57,f"{' ':>1s}{'Block number':<27s}{':':^1s}{l[5]:>15d}{' ':>1s}")
                print(' '*57,f"{' ':>1s}{'Street number':<27s}{':':^1s}{l[6]:>15d}{' ':>1s}")
                print(' '*57,f"{' ':>1s}{'Building number':<27s}{':':^1s}{l[7]:>15d}{' ':>1s}")
                print(' '*57,f"{' ':>1s}{'Floor number':<27s}{':':^1s}{l[8]:>15d}{' ':>1s}")
                print(' '*57,f"{' ':>1s}{'Room number':<27s}{':':^1s}{l[9]:>15d}{' ':>1s}")
                print(' '*57,f"{' ':>1s}{'Price of the order in Kd':<27s}{':':^1s}{l[10]:>13.3f}{'KD':<1s}{' ':>1s}")
                print(' '*57,' ',' '*18,'-END- ',' '*15,' ')
                print(' '*58,'╚','═'*43,'╝',sep='')
                break

    except EOFError:
        print(" "*64,"Error : Customer Name not Found!!!")

    
    file.close()
       
 
#function to delete a record
def delete():
    ne=input("Enter Customer\'s first Name                  :  ")
    na=input("Enter Customer\'s last Name                   :  ")
    file1=open("foods.dat","rb")
    file2=open("temp.dat","wb")
    l=[]
    flag=False
    try:
        while True:
            l=pickle.load(file1)
            if ne.lower()!=l[2].lower() and na.lower()!=l[3].lower():
                pickle.dump(l,file2)
            else:
                flag=True            

    except EOFError:
        if flag==True:
            print("    SUCCESSFULLY: Customer Account deleted")        
    if flag==False:
        print("     Error : Customer Account not found")
    
    file1.close()
    file2.close()
    os.remove("foods.dat")
    os.rename("temp.dat","foods.dat")


#function to display all records
def display():
    file=open("foods.dat","rb")
    l=[]
    flag=0
    try:
        while True:
            l=pickle.load(file)
            print(' '*58,'╔','═'*43,'╗',sep='')
            print(' '*57,' ',' '*13,'DISPLAY FOUND',' '*13,' ')
            print(' '*57,f"{' ':>1s}{'Itemcode':<27s}{':':^1s}{l[0]:>15s}{' ':>1s}")
            print(' '*57,f"{' ':>1s}{'Quantities':<27s}{':':^1s}{l[1]:>15d}{' ':>1s}")             
            print(' '*57,f"{' ':>1s}{'Customer first name':<27s}{':':^1s}{l[2].lower().capitalize():>15s}{' ':>1s}")
            print(' '*57,f"{' ':>1s}{'Customer last name ':<27s}{':':^1s}{l[3].lower().capitalize():>15s}{' ':>1s}")
            print(' '*57,f"{' ':>1s}{'Area name':<27s}{':':^1s}{l[4].lower().capitalize():>15s}{' ':>1s}")
            print(' '*57,f"{' ':>1s}{'Block number':<27s}{':':^1s}{l[5]:>15d}{' ':>1s}")
            print(' '*57,f"{' ':>1s}{'Street number':<27s}{':':^1s}{l[6]:>15d}{' ':>1s}")
            print(' '*57,f"{' ':>1s}{'Building number':<27s}{':':^1s}{l[7]:>15d}{' ':>1s}")
            print(' '*57,f"{' ':>1s}{'Floor number':<27s}{':':^1s}{l[8]:>15d}{' ':>1s}")
            print(' '*57,f"{' ':>1s}{'Room number':<27s}{':':^1s}{l[9]:>15d}{' ':>1s}")
            print(' '*57,f"{' ':>1s}{'Price of the order in Kd':<27s}{':':^1s}{l[10]:>13.3f}{'KD':<1s}{' ':>1s}")
            print(' '*57,' ',' '*18,'-END- ',' '*15,' ')
            print(' '*58,'╚','═'*43,'╝',sep='')
            flag=1
            
    except EOFError:
        print("\n")
    if flag==0:
        print(" "*79,"No Customer Account Found")
        
    print(" "*84,"-- THANK YOU --")
    
    file.close()
 
 
#function to modify a record 
def modify():
    file1=open("foods.dat","rb")
    file2=open("temp.dat","wb")
    ne=input("Enter the Customer\'s first Name                  :  ")
    na=input("Enter the Customer\'s last Name                   :  ")
    while True:
                    f=0
                    i=input(" Enter New Item Code : ")
                    for v in d.values():
                        if i==v[0]:
                            pr=v[1]
                            f=1
                    if not i.isdigit() or len(i)!= 4 :
                        f=0
                    if f==0:
                        print('Enter Valid Itemcode : ')
                    else:
                        break   
    l=[]
    q=int(input(" Enter New Quantity : "))
    Cstprc=pr*q
    flag=False
    try:
        while True:
            l=pickle.load(file1)
            if ne.lower()==l[2].lower() and na.lower()==l[3].lower():
                l[0]=i
                l[1]=q
                l[10]=Cstprc
                flag=True
                print("New Price : ",Cstprc,"KD")
            pickle.dump(l,file2)  

    except EOFError:
        print("over")
    if flag==False:
        print("Error : Customer not found")
    
    file1.close()
    file2.close()
    os.remove("foods.dat")
    os.rename("temp.dat","foods.dat")


#mainmenu
def mainmenu():
    choice=0
    print("**********WELCOME***********")
    while choice!=5:
        print("\n")
        print("*****************************")
        print("1. Add a new Customer Account")
        print("2. Search a Customer")
        print("3. Delete Existing Customer Account")
        print("4. Display all Customer account ")
        print("5. Modify ")
        print("6. View the Menu ")        
        print("7. Exit ")
        ch=input('Enter your choice                            :  ')
        if ch in '1234567':
            ch=int(ch)
            if ch==1:
                create()
            elif ch==2:
                search()
            elif ch==3:
                delete()
            elif ch==4:
                display()
            elif ch==5:
                modify()
            elif ch==6:
                menu()
            elif ch==7:
                print("THANK YOU")
                break
        else:
            print("ERROR\nEnter Valid Choice")


#main program
print(" "*68,'--ONLINE ORDERING SHOP--'," "*9)
print('\n\n')
print(" "*53,'***************WELCOME TO PIZZA STATION***************')
print('\n')

while True:
    ch=input('Would you like to see THE MENU ? [y/n] : ')
    if ch.lower()=='y':
        menu()
    break
d={'FAMILY MEAL':['0010',5.5],'KIDS MEAL':['0020',1.5],'MY BOX':['0030',3.0],'SUPER LIMO':['0040',8.0]} 
mainmenu()
