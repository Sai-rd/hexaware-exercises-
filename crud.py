class myarray:
    def __init__(self,size):
        self.size=size
        self.data=[None]*size
    
    def create(self,index,value):
        if 0<=index<self.size:
            self.data[index]=value 
        else:
            print("Index out of range")
    
    def read(self,index):
        if 0 <= index < self.size:
            return self.data[index]
        else:
            print("Element not in array")
            return None
    
    def update(self,index,value):
        self.data[index]=value
    
    def delete(self,element):
        if element in self.data:
            self.data.remove(element)
        else:
            return None
    
    def display(self):
        print(self.data)


arr=myarray(5)
'''create operation'''
arr.create(0,10)
arr.create(1,20)
arr.create(2,30)
arr.create(3,40)
arr.create(4,50)
arr.display()


'''read operation'''
print(arr.read(3))

'''update operation'''
arr.update(2,100)
arr.display()

'''delete operation'''

arr.delete(50)
arr.display()

