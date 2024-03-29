class Stack:

   __gen_max_list = []
   gen_dict = {}
   gen_non_private_max_list = []

   def __init__(self):
     self.stack=[]
     self.dict={}
     self.max_list=[]

   def push(self, item):
       self.stack.append(item)
       self.update_dict(item)
       self.update_gen_dict(item)
       self.update_max_list(item)
       self.update_gen_max_list(item)

   def update_dict(self, item):
       if item in self.dict:
           self.dict[item]=self.dict[item]+1
       else:
           self.dict[item]=1

   def update_gen_dict(self, item):
       if item in self.gen_dict:
           self.gen_dict[item]=self.gen_dict[item]+1
       else:
           self.gen_dict[item]=1

   def update_max_list(self, item):
       if len(self.max_list)==0:
           self.max_list.append(item)
       elif item > self.max_list[-1]:
           self.max_list.append(item)

   def update_gen_max_list(self, item):
       if len(self.__gen_max_list)==0:
           self.__gen_max_list.append(item)
       elif item > self.__gen_max_list[-1]:
           self.__gen_max_list.append(item)

   def pop(self):
       if self.stack:
           y=self.stack[-1]
           del self.stack[-1]
           self.update_max_list_pop(y)
           self.update_dict_pop(y)
           self.update_gen_max_list_pop(y)
           self.update_gen_dict_pop(y)
           return y


   def update_max_list_pop(self,y):
       if y==self.max_list[-1] and self.dict[y]==1:
           del self.max_list[-1]

   def update_dict_pop(self, y):
       if self.dict[y]>1:
           self.dict[y]=self.dict[y]-1
       else:
           del self.dict[y]

   def update_gen_max_list_pop(self,y):
       if y in self.__gen_max_list and self.gen_dict[y]==1:
           del self.__gen_max_list[-1]

   def update_gen_dict_pop(self, y):
       if self.gen_dict[y]>1:
           self.gen_dict[y]=self.gen_dict[y]-1
       else:
           del self.gen_dict[y]

   def get_max(self):
       try:
           return self.max_list[-1]
       except IndexError:
           raise IndexError('Trying to get a maximum from an empty stack!')

   def get_gen_max(self):
       return self.__gen_max_list[-1]

   def get_max_list(self):
       self.gen_non_private_max_list = self.__gen_max_list

if __name__ == '__main__':
   Stack1 = Stack()
   Stack2 = Stack()

Stack1.push(1)
Stack1.push(5)
Stack2.push(10)
Stack1.pop()

Stack2.get_max_list()
print(Stack2.gen_non_private_max_list)
print(Stack.gen_dict)
print(Stack1.get_gen_max())
