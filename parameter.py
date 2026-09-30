class calculator:
    def add(self,n1, n2):
        result=n1+n2
        print(result)  
           
    def sub(self,n1, n2):
        result=n1-n2
        print(result)

    def mul(self, n1, n2):
        result=n1*n2
        print(result)
        return result

    def div(self,n1, n2):
        result=n1/n2
        print(result)
        return result
    
    def hello(self):
      return "Hello welcome to the world of ai"
  
calc=calculator()
print(calc.add(10,20))  
print(calc.hello())

