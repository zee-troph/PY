class Student:
 def __init__(self,id,name,email,address):
       self.id =id
       self.name =name 
       self.email =email
       self.address =address
       
        
 def display(self):
       print(self.id, self.name, self.email, self.address)
 def show(self):
     print(self.id, self.name)      
             
        
stud= Student(101, "Tinubu", "tgmail.com", "Aso rock")
stud.display()
stud.show()
         