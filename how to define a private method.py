# Python program to  
# demonstrate private methods 

   
# Creating a class  

class test:  

    # Declaring public method 

    def public(self): 

        print("Public method") 

   

    # Declaring private method 

    def __private(self): 

        print("Private method") 

      

    # Calling private method via 

    # another method 

    def Help(self): 

        self.public() 

        self.__private() 

          

instance = test() 

instance.Help() 