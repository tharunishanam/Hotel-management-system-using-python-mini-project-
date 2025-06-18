n=[]
p=[]
a=[]
d=[]
cin=[]
cout=[]
room=[]
price=[]
f=[]
class Hotel:
    def booking(self):
        self.name=input("name")
        self.phnno=int(input("phnno"))
        self.address=input("address")
        self.checkin=input("checkin")
        self.checkout=input("checkout")
        self.days=int(input("enter no of days"))
        n.append(self.name)
        p.append(self.phnno)
        a.append(self.address)
        cin.append(self.checkin)
        cout.append(self.checkout)
        d.append(self.days)
        f=open("record.txt","a")
        f.write("Name="+self.name+"\t")
        f.write("Phn no="+str(self.phnno)+"\t")
        f.write("Address="+self.address+"\t")
        f.write("Checkin="+self.checkin+"\t")
        f.write("Checkout="+self.checkout+"\n")
        f.close()
    def info(self):
        file=open("info.txt","r")
        print(file.read())
        file.close()
    def allotment(self):
        self.ch=int(input("1.STANDARD AC,2.STANDARD NON AC,3.LUXURY AC,4.LUXURY NON AC"))
        if self.ch==1:
            global c
            with open("file1.txt","r") as file:
                fp=file.read()
                c=int(fp[-1])
                file.close()
            if c>0:
              print("Room booked successfully,Room no:[10",c,"]")
              q=str(10)+str(c)
              f=open("record.txt","a")
              f.write("Room no="+q+"\n")
              f.close()
              room.append("standard ac")
              price.append(4000)
              c=c-1
              with open("file1.txt","a") as f:
                  f.write(str(c))
            else:
                print("room not available")
        elif self.ch==2:
             global d
             with open("file2.txt","r") as file:
                 fp=file.read()
                 d=int(fp[-1])
                 file.close()
             if d>0:
                 print("Room booked successfully,Room no:[10",d,"]")
                 room.append("standard non ac")
                 q=str(10)+str(d)
                 f=open("record.txt","a")
                 f.write("Room no="+q+"\n")
                 f.close()
                 price.append(3500)
                 d=d-1
                 with open("file2.txt","a") as f:
                     f.write(str(d))
             else:
                print("room not available")
        elif self.ch==3:
             global e
             with open("file3.txt","r") as file:
                 fp=file.read()
                 e=int(fp[-1])
                 file.close()
             if e>0:
                 print("Room booked successfully,Room no:[10",e,"]")
                 q=str(10)+str(e)
                 f=open("record.txt","a")
                 f.write("Room no="+q+"\n")
                 f.close()
                 room.append("luxury ac")
                 price.append(5000)
                 e=e-1
                 with open("file3.txt","a") as f:
                     f.write(str(e))
             else:
                print("room not available")
        elif self.ch==4:
             global g
             with open("file4.txt","r") as file:
                 fp=file.read()
                 g=int(fp[-1])
                 file.close()
             if g>0:
                 print("Room booked successfully,Room no:[10",g,"]")
                 q=str(10)+str(f)
                 f=open("record.txt","a")
                 f.write("Room no="+q+"\n")
                 f.close()
                 room.append("luxury non ac")
                 price.append(4500)
                 g=g-1
                 with open("file4.txt","a") as f:
                     f.write(str(g))
             else:
                print("room not available")
        else:
            print("wrong choice")
    def food(self):
        print("--MENU--")
        print("1)Chicken Starters +biryani + dessert---- 1200.00")
        print("2)Butter panneer + biryani + dessert----- 1000.00")
        print("3)Cold drinks ---- 50.00")
        c=1
        s=0
        while c!=0:
            x=int(input("enter your choice"))
            if x==1:
                s=s+1200
            elif x==2:
                s=s+1000
            elif x==3:
                s=s+50
            c=int(input("do you want to order more?1-yes,0-no"))
        print("Total bill= ",s)
        f.append(s)
    def bill(self):
        if len(f)!=0:
            print(" --------------------------------")
            print("              Bill")
            print(" --------------------------------")
            print(" Name: ",n[0],"\t\n Phone No.: ",p[0],"\t\n Address: ",a[0],"\t")
            print("\n Check-In: ",cin[0],"\t\n Check-Out: ",cout[0],"\t")
            print("\n Room Type: ",room[0],"\t\n Room Charges: ",price[0]*d[0],"\t")
            print(" Restaurant Charges: \t",f[0])
            print(" --------------------------------")
            print("\n Total Amount: ",(price[0]*d[0])+f[0],"\t")
            print(" --------------------------------")
        else:
            print(" --------------------------------")
            print("              Bill")
            print(" --------------------------------")
            print(" Name: ",n[0],"\t\n Phone No.: ",p[0],"\t\n Address: ",a[0],"\t")
            print("\n Check-In: ",cin[0],"\t\n Check-Out: ",cout[0],"\t")
            print("\n Room Type: ",room[0],"\t\n Room Charges: ",price[0]*d[0],"\t")
            print(" --------------------------------")
            print("\n Total Amount: ",(price[0]*d[0]),"\t")
            print(" --------------------------------")
    def checkout(self):
        print("1.STANDARD AC,2.STANDARD NON AC,3,LUXURY AC,4.LUXURY NON AC")
        self.a=int(input("enter room type"))
        if self.a==1:
            global b
            with open("file1.txt","r") as file:
                fp=file.read()
                b=int(fp[-1])
                file.close()
            b=b+1
            with open("file1.txt","a") as f:
                f.write(str(b))
        elif self.a==2:
            global w
            with open("file2.txt","r") as file:
                fp=file.read()
                w=int(fp[-1])
                file.close()
            w=w+1
            with open("file2.txt","a") as f:
                f.write(str(w))
        elif self.a==3:
            global x
            with open("file3.txt","r") as file:
                fp=file.read()
                x=int(fp[-1])
                file.close()
            x=x+1
            with open("file3.txt","a") as f:
                f.write(str(x))
        elif self.a==4:
            global y
            with open("file4.txt","r") as file:
                fp=file.read()
                y=int(fp[-1])
                file.close()
            y=y+1
            with open("file4.txt","a") as f:
                f.write(str(y))
g=1
while(g!=0):
    print("1 Booking\n")
    print("2 Rooms Info\n")
    print("3 Menu Card\n")
    print("4 Payment\n")
    print("5 Checkout\n")
    print("6 Record\n")
    print("0 Exit\n")
    t=int(input("enter your choice"))
    if t==1:
        h=Hotel()
        h.booking()
        h.allotment()
    elif t==2:
        h=Hotel()
        h.info()
    elif t==3:
        h=Hotel()
        h.food()
    elif t==4:
        h=Hotel()
        h.bill()
    elif t==5:
        h=Hotel()
        h.checkout()
    elif t==6:
        h=Hotel()
        h.record()
    elif t==0:
        break
