class Node:
    def __init__(self,value=None):
        self.data=value
        self.next=None
        

class linked_list:
    def __init__(self):
        self.head=None
        self.size=0

    def insertBeg(self,value):
        newNode=Node(value)
        newNode.next=self.head
        self.head=newNode
        self.size+=1


    def insert(self,value,pos):
        if(pos==1):
            self.insertBeg(value)
        elif(pos<=self.size+1):
            temp=self.head
            newNode=Node(value)
            for i in range(2,pos):
                temp=temp.next
            newNode.next=temp.next
            temp.next=newNode
            self.size+=1
        else:
            print('Invalid position of element:{0}'.format(pos))

    def delete(self,pos):
        if pos<=self.size:
            prev=self.head
            cur=self.head
            if pos==1:
                self.head=cur.next
                  
            else:
                for i in range(2,pos):
                    prev=prev.next
                cur=prev.next
                prev.next=cur.next

            self.size-=1
        else:
            print("Delete: invalid position")

    def reverse(self):
        prev=None
        cur=self.head
        fut=cur.next
        while cur:
            cur.next=prev
            prev=cur
            cur=fut
            if fut!=None: fut=fut.next
        self.head=prev

    def makeloop(self,pos):             #connect last element with element at offset
        
        temp=self.head
        for i in range(2,self.size+1):
            temp=temp.next

        temp2=self.head
        for i in range(1,pos):
            temp2=temp2.next
        temp.next=temp2

    def isloop(self):                       #return true if there is a loop
        slow=self.head
        fast=self.head
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast: return True
        return False

    def LAF_loop(self):                     #return tuple of last and first element of loop
        slow=self.head
        fast=self.head
        isloop=False
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                isloop=True
                break

        if isloop:
            slow=self.head
            while 1:
                if slow.next==fast.next:
                   return (fast,slow.next)
                slow=slow.next
                fast=fast.next
        else:
            return ((),())
        
    def removeloop(self):               #remove loop
        (last,slow)=self.LAF_loop()
        print(last)
        if(last==()):
            print("removeloop: No loop")
            return
        last.next=None
        
        
    
    def display(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
        print()

    def printRev(self,temp):
        if temp==None:
            return 
        if temp.next==None:
            print(temp.data,end=" ")
            return
        self.printRev(temp.next)
        print(temp.data,end=" ")

    
         
            
        


