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

    def circular(self):
        
        temp=self.head
        for i in range(2,self.size+1):
            temp=temp.next
                
        temp.next=self.head

    def isCircular(self):
        temp=self.head
        if temp==None:
            return True
        while temp:
            if temp.next==self.head:
                return True
            temp=temp.next
        return False

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
         
            
        


