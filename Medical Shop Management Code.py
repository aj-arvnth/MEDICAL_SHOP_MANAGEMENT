from prettytable import PrettyTable
x=PrettyTable()

class Node:

    def __init__(self,mn,mno,mrp,md,ed):

        self.left = None
        self.right = None
        self.mn = mn
        self.mno = mno
        self.mrp = mrp
        self.md = md
        self.ed = ed

    def insert(self,mn,mno,mrp,md,ed):
        if self.mno:
            if mno < self.mno:
                if self.left is None:
                    self.left = Node(mn,mno,mrp,md,ed)
                else:
                    self.left.insert(mn,mno,mrp,md,ed)
            elif mno > self.mno:
                if self.right is None:
                    self.right = Node(mn,mno,mrp,md,ed)
                else:
                    self.right.insert(mn,mno,mrp,md,ed)
        else:
            self.mno = mno

    def search(self,key):
        x=PrettyTable()
        x.field_names = ['medicine name','medicine number','maximum retail price','manufacturing date','expiry date']
        if key < self.mno:
            return self.left.search(key)
        elif key > self.mno:
            return self.right.search(key)
        else:
            x.add_row([ self.mn,self.mno,self.mrp,self.md,self.ed])
        return x
        del(x)

# Print the tree
    def PrintTree(self):
        x.field_names = ['medicine_name','medicine_number','maximum_retail_price','manufacturing_date','expiry_date']
        if self.left:
            self.left.PrintTree()
        x.add_row([ self.mn,self.mno,self.mrp,self.md,self.ed]),
        if self.right:
            self.right.PrintTree()
        return x


medi_name=[]
medi_no=[]
mrp=[]
mfd_date=[]
exp_date=[]
    
def medientry():
    global n
    n=int(input("Enter the no. of medicines to be added: "))
    for i in range(0,n):
        medi_name.append(input("Enter Medicine Name : "))                     
        medi_no.append(int(input("Enter Medicine Number : ")))
        mrp.append(float(input("Enter Maximum Retail Price : ")))
        mfd_date.append(str(input("Enter Manufacturing Date : ")))
        exp_date.append(str(input("Enter Expiry Date : ")))
      
    global root  
    root=Node(medi_name[0],medi_no[0],mrp[0],mfd_date[0],exp_date[0])
    for i in range(0,n):
        root.insert(medi_name[i],medi_no[i],mrp[i],mfd_date[i],exp_date[i])
       

def showmedi():
    
    print(root.PrintTree())

def searchmedi():
    a=medi_no[0]
    b=medi_no[n-1]
    #print(root.search(2006))
    find_mno=float(input("Enter a year between {}-{}:".format(a,b)))
    print(root.search(find_mno))


def menu():
    print("********************MAIN MENU***********************")
    print()

    choice = input("""
                 A: Add medecine
                 B: Show medicines
                 C: Search for a medecine
                 D: Quit
                 Please enter your choice: """)

    while True:
        if choice == "A" or choice =="a":
            medientry()
            menu()
        elif choice =="B" or choice=="b":
            showmedi()
            menu()
        elif choice =="C" or choice =="c":
            searchmedi()
            menu()
        elif choice=="D" or choice=="d":
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Thank You!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            exit(1)
        else:
            print("You must only select either A,B,C,or D")
            print("Please try again")
            menu()

menu()
